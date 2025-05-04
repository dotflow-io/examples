#!/usr/bin/env python

import os

from dotenv import load_dotenv

from dotflow import Config, DotFlow, action
from dotflow.types import TypeStatus
from dotflow.notify import NotifyTelegram


@action
def simple_step():
    return "ok"


def main():
    load_dotenv()

    notify = NotifyTelegram(
        token=os.getenv("TOKEN"),
        chat_id=os.getenv("CHAT_ID"),
        notification_type=TypeStatus.FAILED,
    )

    workflow = DotFlow(config=Config(notify=notify))

    workflow.task.add(step=simple_step)
    workflow.start()

    return workflow


if __name__ == "__main__":
    main()
