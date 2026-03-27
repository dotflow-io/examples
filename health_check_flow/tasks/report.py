from __future__ import annotations

import json
from datetime import datetime, timezone

from dotflow import action


@action
def generate_report(previous_context):
    data = previous_context.storage

    report = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "summary": {
            "total": data["total"],
            "ok_count": data["ok_count"],
            "fail_count": data["fail_count"],
            "avg_response_time_ms": data["avg_response_time_ms"],
        },
        "results": data["results"],
    }

    with open("health_report.json", "w") as f:
        json.dump(report, f)

    return report
