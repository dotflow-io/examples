#!/usr/bin/env python

from dotflow import DotFlow, action


@action
def simple_step():
    return "ok"


def main():
    workflow = DotFlow()

    workflow.task.add(step=simple_step)
    workflow.start()

    return workflow


if __name__ == "__main__":
    main()
