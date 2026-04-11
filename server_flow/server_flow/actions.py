import json
import asyncio
from datetime import datetime, timezone

import httpx

from dotflow import action


@action(timeout=30)
async def fetch_all_endpoints(initial_context):
    endpoints = initial_context.storage

    async with httpx.AsyncClient() as http_client:
        requests = [http_client.get(endpoint, timeout=5) for endpoint in endpoints]
        responses = await asyncio.gather(*requests)

    return {"endpoints": [response.json() for response in responses]}


@action
def aggregate_results(previous_context):
    fetched_data = previous_context.storage["endpoints"]

    return {
        "total": len(fetched_data),
        "results": fetched_data,
    }


@action
def generate_report(previous_context):
    aggregated = previous_context.storage

    report = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "total": aggregated["total"],
        "results": aggregated["results"],
    }

    with open("/tmp/server_report.json", "w") as output_file:
        json.dump(report, output_file, indent=2)

    return report
