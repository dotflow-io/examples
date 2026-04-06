#!/usr/bin/env python

from dotflow import Config, DotFlow, action
from dotflow.providers import StorageFile


@action
def step_one():
    return {"extracted": True}


@action
def step_two(previous_context):
    return {"transformed": previous_context.storage}


@action
def step_three(previous_context):
    return {"loaded": previous_context.storage}


def main():
    config = Config(storage=StorageFile())

    workflow = DotFlow(config=config, workflow_id="my-pipeline")
    workflow.task.add(step=step_one)
    workflow.task.add(step=step_two)
    workflow.task.add(step=step_three)
    workflow.start(resume=True)

    return workflow


if __name__ == "__main__":
    main()
