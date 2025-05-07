#!/usr/bin/env python

import os
import sys

from dotenv import load_dotenv

from dotflow import DotFlow, Config
from dotflow.storage import StorageFile
from dotflow.notify import NotifyTelegram

from tasks.extract import extract
from tasks.load import load
from tasks.transform import Transform


def main():
    load_dotenv()

    notify = NotifyTelegram(
        token=os.getenv("BOT_TOKEN"),
        chat_id=os.getenv("CHAT_ID")
    )

    workflow = DotFlow(
        config=Config(notify=notify)
    )

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
