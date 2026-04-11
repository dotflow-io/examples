import os

from dotenv import load_dotenv

from dotflow import Config, DotFlow
from dotflow.types import TypeStatus
from dotflow.providers import NotifyTelegram

from etl_flow.actions import extract, Transform, load
from etl_flow.server import ServerAPI

load_dotenv()

INITIAL_URL = "https://pythonfluente.com"

server = ServerAPI(
    base_url=os.getenv("SERVER_BASE_URL", "http://localhost:8000"),
    user_token=os.getenv("SERVER_USER_TOKEN", ""),
)


def main():
    bot_token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")

    config = Config(server=server)
    if bot_token and chat_id:
        notify = NotifyTelegram(
            token=bot_token,
            chat_id=chat_id,
            notification_type=TypeStatus.COMPLETED,
        )
        config = Config(server=server, notify=notify)

    workflow = DotFlow(config=config)
    workflow.task.add(
        step=[extract, Transform, load],
        initial_context=INITIAL_URL,
    )
    workflow.start()

    return workflow


def lambda_handler(event, context):
    workflow = main()
    return workflow.result()


if __name__ == "__main__":
    workflow = main()
    print(workflow.result())
