#!/usr/bin/env python

from dotflow import Config, DotFlow
from dotflow.providers import StorageFile

from tasks.aggregate import aggregate_results
from tasks.check import check_endpoint
from tasks.constants import ENDPOINTS
from tasks.report import generate_report
from tasks.validate import validate_results


def main():
    config = Config(storage=StorageFile())

    checks = DotFlow(config=config)
    for url in ENDPOINTS:
        checks.task.add(step=check_endpoint, initial_context=url)
    checks.start(mode="parallel")

    results = {"results": [
        {**task.current_context.storage, "response_time_ms": round(task.duration * 1000, 2)}
        for task in checks.task.queue
        if task.current_context.storage
    ]}

    report = DotFlow(config=config)
    report.task.add(
        step=[aggregate_results, validate_results, generate_report],
        initial_context=results,
    )
    report.start()

    return report


if __name__ == "__main__":
    workflow = main()
    print(workflow.result())
