#!/usr/bin/env python

import asyncio

from dotflow import DotFlow, action


@action
async def async_step_one():
    await asyncio.sleep(0.1)
    return {"async": True}


@action
async def async_step_two(previous_context):
    await asyncio.sleep(0.1)
    return {"result": previous_context.storage}


@action
def sync_step():
    return {"sync": True}


def main():
    workflow = DotFlow()
    workflow.task.add(step=async_step_one)
    workflow.task.add(step=async_step_two)
    workflow.task.add(step=sync_step)
    workflow.start()

    for task in workflow.result_task():
        print(f"Task {task.task_id}: {task.status}")

    return workflow


if __name__ == "__main__":
    main()
