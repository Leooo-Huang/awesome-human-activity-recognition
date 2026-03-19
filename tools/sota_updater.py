#!/usr/bin/env python3
"""
Fetch latest SOTA scores from Papers with Code for key HAR-related tasks
and save a snapshot to data/sota-snapshot.json.
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

# Papers with Code API base
API_BASE = "https://paperswithcode.com/api/v1"

# Task slugs we track (mapped to the datasets they cover)
TASK_SLUGS = [
    "action-recognition-in-videos",       # Kinetics, UCF-101, HMDB-51
    "skeleton-based-action-recognition",   # NTU RGB+D
    "activity-recognition",               # Wearable HAR
    "human-pose-estimation",              # Human3.6M
]

OUTPUT_PATH = Path(__file__).resolve().parent.parent / "data" / "sota-snapshot.json"

# Timeout for every HTTP request (seconds)
REQUEST_TIMEOUT = 30


def fetch_task_info(slug: str) -> dict | None:
    """Fetch task metadata from Papers with Code."""
    url = f"{API_BASE}/tasks/{slug}/"
    try:
        resp = requests.get(url, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as exc:
        print(f"  [WARN] Failed to fetch task info for '{slug}': {exc}")
        return None


def fetch_task_evaluations(slug: str) -> list | None:
    """Fetch evaluation results (top SOTA entries) for a task."""
    url = f"{API_BASE}/tasks/{slug}/evaluations/"
    try:
        resp = requests.get(url, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
        # The API may return paginated results with a "results" key,
        # or it may return a plain list. Handle both.
        if isinstance(data, dict):
            return data.get("results", [])
        if isinstance(data, list):
            return data
        return []
    except requests.RequestException as exc:
        print(f"  [WARN] Failed to fetch evaluations for '{slug}': {exc}")
        return None


def build_snapshot() -> dict:
    """Build the full SOTA snapshot for all tracked tasks."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    tasks: dict[str, dict] = {}

    for slug in TASK_SLUGS:
        print(f"Fetching: {slug} ...")
        info = fetch_task_info(slug)
        evaluations = fetch_task_evaluations(slug)

        task_name = info.get("name", slug) if info else slug
        description = info.get("description", "") if info else ""

        tasks[slug] = {
            "task_name": task_name,
            "description": description[:300] if description else "",
            "top_results": evaluations if evaluations is not None else [],
        }

        n_results = len(tasks[slug]["top_results"])
        print(f"  -> {task_name}: {n_results} evaluation entries")

    return {
        "updated_at": now,
        "tasks": tasks,
    }


def main() -> None:
    print("=== SOTA Snapshot Updater ===\n")

    snapshot = build_snapshot()

    # Ensure output directory exists
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        json.dump(snapshot, fh, indent=2, ensure_ascii=False)

    print(f"\nSnapshot saved to {OUTPUT_PATH}")
    print(f"Updated at: {snapshot['updated_at']}")
    print(f"Tasks tracked: {len(snapshot['tasks'])}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"[ERROR] Unhandled exception: {exc}", file=sys.stderr)
        sys.exit(1)
