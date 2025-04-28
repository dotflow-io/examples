#!/usr/bin/env python

import sys

from dotflow import DotFlow, Config
from dotflow.storage import StorageFile

from tasks.extract import extract
from tasks.load import load
from tasks.transform import Transform


def main():
    workflow = DotFlow()

    if len(sys.argv) == 2 and sys.argv[1] == "file":
        config = Config(storage=StorageFile())
        workflow = DotFlow(config=config)

    workflow.task.add(
        step=[extract, Transform, load],
        initial_context="https://pythonfluente.com"
    )

    workflow.start()

    return workflow


def lambda_handler(event, context):
    workflow = main()
    return workflow.result()


if __name__ == "__main__":
    workflow = main()
