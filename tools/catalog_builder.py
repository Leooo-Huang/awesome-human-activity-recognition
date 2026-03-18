"""
Catalog Builder
---------------

Parses dataset cards to produce machine-readable summaries (JSON/CSV).

Capabilities:
- Enumerates Markdown files under datasets/ grouped by modality.
- Extracts key-value metadata from the bullet-list header in each card.
- Outputs JSON or CSV format.
- Prints a summary report of dataset counts per modality.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

DATASET_ROOT = Path(__file__).resolve().parents[1] / "datasets"
MODALITIES = ["vision", "skeleton", "wearable", "multimodal", "emerging"]
CSV_COLUMNS = ["modality", "title", "primary tasks", "scale", "license", "access"]


def collect_dataset_files() -> Dict[str, List[Path]]:
    """Return mapping of modality -> list of dataset Markdown files."""
    catalog: Dict[str, List[Path]] = defaultdict(list)
    for modality in MODALITIES:
        folder = DATASET_ROOT / modality
        if not folder.exists():
            continue
        for md_file in sorted(folder.glob("*.md")):
            if md_file.name.startswith("_"):
                continue
            catalog[modality].append(md_file)
    return dict(catalog)


def extract_title(markdown: Path) -> str:
    """Grab the first level-1 heading as the dataset title."""
    for line in markdown.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return markdown.stem.replace("-", " ").title()


HEADER_PATTERN = re.compile(r"^- \*\*(?P<key>[^*:\n]+):\*\*\s*(?P<value>.+)$")


def extract_metadata(markdown: Path) -> Dict[str, str]:
    """
    Extract simple key/value metadata from the bullet list in each card.

    Example:
    - **Modality:** RGB video
    """
    metadata: Dict[str, str] = {}
    for line in markdown.read_text(encoding="utf-8").splitlines():
        text = line.strip()
        match = HEADER_PATTERN.match(text)
        if match:
            metadata[match.group("key").strip().lower()] = match.group("value").strip()
        # stop at the first blank line after metadata block
        if metadata and not text:
            break
    metadata.setdefault("title", extract_title(markdown))
    return metadata


def build_catalog() -> Dict[str, List[Dict[str, str]]]:
    catalog = {}
    for modality, files in collect_dataset_files().items():
        entries = []
        for md in files:
            meta = extract_metadata(md)
            meta["modality_group"] = modality
            meta["file"] = str(md.relative_to(DATASET_ROOT.parent))
            entries.append(meta)
        catalog[modality] = entries
    return catalog


def catalog_to_csv(catalog: Dict[str, List[Dict[str, str]]]) -> str:
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=CSV_COLUMNS, extrasaction="ignore")
    writer.writeheader()
    for modality, entries in catalog.items():
        for entry in entries:
            row = {col: entry.get(col, "") for col in CSV_COLUMNS}
            row["modality"] = modality
            writer.writerow(row)
    return buf.getvalue()


def print_summary(catalog: Dict[str, List[Dict[str, str]]]) -> None:
    total = 0
    print("\n--- Dataset Catalog Summary ---")
    for modality in MODALITIES:
        count = len(catalog.get(modality, []))
        total += count
        print(f"  {modality:<12} {count:>3} datasets")
    print(f"  {'TOTAL':<12} {total:>3} datasets")
    print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate dataset catalog exports.")
    parser.add_argument(
        "--format",
        choices=["json", "csv"],
        default="json",
        help="Output format (default: json).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional output path. Defaults to stdout.",
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Print a summary of dataset counts per modality.",
    )
    args = parser.parse_args()

    catalog = build_catalog()

    if args.format == "csv":
        output = catalog_to_csv(catalog)
    else:
        output = json.dumps(catalog, indent=2, sort_keys=True, ensure_ascii=False)

    if args.output:
        args.output.write_text(output, encoding="utf-8")
        print(f"Wrote {args.format.upper()} to {args.output}")
    else:
        print(output)

    if args.summary:
        print_summary(catalog)


if __name__ == "__main__":
    main()
