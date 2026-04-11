# etl_flow

A workflow built with [dotflow](https://github.com/dotflow-io/dotflow) demonstrating an ETL pipeline.

## Configuration

| Option | Value |
|--------|-------|
| Storage | default |
| Execution mode | sequential |
| Retry | yes (extract: 5, transform: 1) |

## Getting Started

```bash
cp .env-example .env
pip install -e ".[dev]"
python -m etl_flow.workflow
```

## Running Tests

```bash
pytest
```

## How It Works

### Pipeline

```
extract → Transform → load
```

1. **extract** — fetches HTML from a URL
2. **Transform** — class-based action with 3 steps:
   - `text_html_parser` — parses HTML with BeautifulSoup
   - `transform_to_dict` — extracts title and author
   - `transform_model` — validates with Pydantic Book model
3. **load** — writes the result to `book.json`

### Docker

```bash
docker build -t etl-flow --file dockerfile.python .
docker run etl-flow
```

### AWS Lambda

```bash
docker build -t etl-flow --file dockerfile.lambda .
docker run -p 9000:8080 etl-flow
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```
