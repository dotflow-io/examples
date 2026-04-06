#!/usr/bin/env python

import time

from dotflow import Config, DotFlow, action
from dotflow.providers import SchedulerCron


@action
def slow_task():
    time.sleep(30)
    return {"done": True}


def main():
    config = Config(
        scheduler=SchedulerCron(cron="*/1 * * * *", overlap="skip"),
    )

    workflow = DotFlow(config=config)
    workflow.task.add(step=slow_task)

    # workflow.schedule() blocks — run manually to start the cron loop

    return workflow


if __name__ == "__main__":
    main()
