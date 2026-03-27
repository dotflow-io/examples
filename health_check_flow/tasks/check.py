from __future__ import annotations

from dotflow import action
from requests import get


@action(retry=2, timeout=6)
def check_endpoint(initial_context):
    url = initial_context.storage
    try:
        response = get(url, timeout=5)
        return {
            "url": url,
            "ok": response.ok,
            "status_code": response.status_code,
        }
    except Exception as error:
        return {
            "url": url,
            "ok": False,
            "status_code": None,
            "error": str(error),
        }
