#!/usr/bin/env python

from dotflow import DotFlow, action


@action
def extract_task():
    print("extract")
    return "extract"


@action
def transform_task(previous_context):  # HERE
    print(previous_context.storage, "transform")
    assert previous_context.storage == "extract"

    return "transform"


@action
def load_task(previous_context):  # HERE
    print(previous_context.storage, "load")
    assert previous_context.storage == "transform"

    return "load"


def main():
    workflow = DotFlow()

    workflow.task.add(step=extract_task)
    workflow.task.add(step=transform_task)
    workflow.task.add(step=load_task)

    workflow.start()

    return workflow


if __name__ == "__main__":
    main()
