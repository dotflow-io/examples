import os

os.environ.setdefault("DOTFLOW_OUTPUT_PATH", "/tmp/.output")

from etl_flow.workflow import main


def handler(event, context):
    """Invoked by EventBridge on a schedule."""
    workflow = main()

    return {
        "statusCode": 200,
        "body": workflow.result()
    }
