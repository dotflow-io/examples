from __future__ import annotations

from dotflow import action

from tasks.constants import ENDPOINTS


@action
def validate_results(previous_context):
    data = previous_context.storage

    assert data, "No aggregated data received"
    assert data["total"] == len(ENDPOINTS), f"Expected {len(ENDPOINTS)} results, got {data['total']}"
    assert data["ok_count"] > 0, "No successful checks"

    checked_urls = {r["url"] for r in data["results"]}
    missing = set(ENDPOINTS) - checked_urls
    assert not missing, f"Missing results for: {missing}"

    return data
