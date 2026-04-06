#!/usr/bin/env python

from dotflow import Config, DotFlow, action
from dotflow.providers import SchedulerCron, StorageFile


@action
def extract():
    return {"data": "fetched"}


@action
def transform(previous_context):
    return {"transformed": previous_context.storage}


@action
def load(previous_context):
    return {"saved": previous_context.storage}


def main():
    config = Config(
        storage=StorageFile(),
        scheduler=SchedulerCron(cron="0 6 * * *", overlap="skip"),
    )

    workflow = DotFlow(config=config, workflow_id="etl-daily")
    workflow.task.add(step=extract)
    workflow.task.add(step=transform)
    workflow.task.add(step=load)

    # workflow.schedule(resume=True) blocks — run manually to start the cron loop

    return workflow


if __name__ == "__main__":
    main()
