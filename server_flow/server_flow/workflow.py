import os

from dotenv import load_dotenv

from dotflow import Config, DotFlow

from server_flow.server import ServerAPI
from server_flow.actions import fetch_all_endpoints, aggregate_results, generate_report

load_dotenv()

ENDPOINTS = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/users/1",
    "https://jsonplaceholder.typicode.com/users/2",
]

server = ServerAPI(
    base_url=os.getenv("SERVER_BASE_URL", "http://localhost:8000"),
    user_token=os.getenv("SERVER_USER_TOKEN", ""),
)
config = Config(server=server)


def main():
    workflow = DotFlow(config=config)

    workflow.task.add(
        step=[
            fetch_all_endpoints,
            aggregate_results,
            generate_report
        ],
        initial_context=ENDPOINTS,
    )

    workflow.start()

    return workflow.result()


if __name__ == "__main__":
    print(main())
