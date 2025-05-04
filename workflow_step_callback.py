#!/usr/bin/env python

from dotflow import DotFlow, action
from dotflow.core.types.status import TypeStatus


def callback(task):  # HERE
    assert task
    assert task.current_context.storage == "ok"
    assert task.status is TypeStatus.COMPLETED

    print(task.task_id, task.status, task.current_context.storage)
    print(task.__dict__)


@action
def simple_step():
    return "ok"


def main():
    workflow = DotFlow()

    workflow.task.add(step=simple_step, callback=callback)
    workflow.start()

    return workflow


if __name__ == "__main__":
    main()
