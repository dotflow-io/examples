import os

os.environ.setdefault("DOTFLOW_OUTPUT_PATH", "/tmp/.output")

from server_flow.workflow import main


def handler(event, context):
    """Invoked by EventBridge on a schedule."""
    result = main()

    return {
        "statusCode": 200,
        "body": result
    }
