from __future__ import annotations

from dotflow import action


@action
def aggregate_results(initial_context):
    data = initial_context.storage
    results = data.get("results", []) if isinstance(data, dict) else []

    ok = [r for r in results if r.get("ok")]
    failed = [r for r in results if not r.get("ok")]
    times = [r["response_time_ms"] for r in ok if r.get("response_time_ms")]

    return {
        "total": len(results),
        "ok_count": len(ok),
        "fail_count": len(failed),
        "avg_response_time_ms": round(sum(times) / len(times), 2) if times else None,
        "results": results,
    }
