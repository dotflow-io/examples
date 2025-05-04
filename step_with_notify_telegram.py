#!/usr/bin/env python

import os
import time

from dotenv import load_dotenv

from dotflow import Config, DotFlow, action
from dotflow.notify import NotifyTelegram
from dotflow.types import TypeStatus


@action
def simple_step(initial_context):
    time.sleep(0.5)
    return "ok"


@action
def simple_step_raise():
    raise Exception("Fail!")


def main():
    load_dotenv()

    notify = NotifyTelegram(
        token=os.getenv("TOKEN"),
        chat_id=os.getenv("CHAT_ID"),
        notification_type=TypeStatus.FAILED
    )

    workflow = DotFlow(
        config=Config(notify=notify)
    )

    workflow.task.add(step=simple_step, initial_context={"foo": "bar"})
    workflow.task.add(step=simple_step_raise)
    workflow.start()

    return workflow


if __name__ == "__main__":
    main()
