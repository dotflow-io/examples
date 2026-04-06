#!/usr/bin/env python

from dotflow import DotFlow, action


@action(retry=3, retry_delay=1)
def unreliable_step():
    raise ValueError("Something went wrong")


def main():
    workflow = DotFlow()
    workflow.task.add(step=unreliable_step)
    workflow.start()

    task = workflow.result_task()[0]
    print(f"Status: {task.status}")
    print(f"Retry count: {task.retry_count}")
    print(f"Total errors: {len(task.errors)}")

    for error in task.errors:
        print(f"  Attempt {error.attempt}: [{error.exception}] {error.message}")

    return workflow


if __name__ == "__main__":
    main()
