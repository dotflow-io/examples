from bs4 import BeautifulSoup
from pydantic import BaseModel
from requests import get

from dotflow import action


class Book(BaseModel):
    title: str
    author: str


@action(retry=5)
def extract(initial_context):
    return get(initial_context.storage).text


@action
class Transform:
    @action(retry=1)
    def text_html_parser(self, previous_context):
        soup = BeautifulSoup(previous_context.storage, features="html.parser")

        return soup

    @action(retry=1)
    def transform_to_dict(self, previous_context):
        html = previous_context.storage
        new_dict = {
            "title": html.title.text,
            "author": html.find(id="author").text,
        }

        return new_dict

    @action
    def transform_model(self, previous_context):
        return Book(**previous_context.storage).model_dump_json()


@action
def load(previous_context):
    import os

    output_dir = os.environ.get("DOTFLOW_OUTPUT_PATH", ".")
    filepath = os.path.join(output_dir, "book.json")
    os.makedirs(output_dir, exist_ok=True)

    with open(file=filepath, mode="w", encoding="utf-8") as file:
        file.write(previous_context.storage[2].storage)
