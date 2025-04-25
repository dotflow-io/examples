#!/usr/bin/env python

from time import sleep

from dotflow import DotFlow, action


@action
def task_foo(initial_context):
    sleep(2)
    value = initial_context.storage
    return value * value * value


@action
def task_bar(initial_context):
    sleep(1)
    value = initial_context.storage
    return value * value * value


def main():
    workflow = DotFlow()

    workflow.task.add(step=task_foo, initial_context=10)
    workflow.task.add(step=task_bar, initial_context=10)

    workflow.start(mode="sequential")

    return workflow


if __name__ == "__main__":
    main()
