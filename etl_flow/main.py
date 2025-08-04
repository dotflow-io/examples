#!/usr/bin/env python

import os

from dotenv import load_dotenv

from dotflow.types import TypeStatus
from dotflow import DotFlow, Config
from dotflow.providers.notify_telegram import NotifyTelegram

from tasks.extract import extract
from tasks.load import load
from tasks.transform import Transform


def main():
    load_dotenv()

    bot_token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")

    workflow = DotFlow()
    if bot_token and chat_id:
        notify = NotifyTelegram(
            token=bot_token,
            chat_id=chat_id,
            notification_type=TypeStatus.COMPLETED,
        )

        workflow = DotFlow(
            config=Config(notify=notify)
        )

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
