# server_flow

A workflow built with [dotflow](https://github.com/dotflow-io/dotflow) demonstrating a custom Server API provider.

## Configuration

| Option | Value |
|--------|-------|
| Storage | default |
| Server | Custom `ServerAPI` (extends `Server` ABC) |
| Execution mode | parallel + sequential |

## Getting Started

```bash
cp .env-example .env
pip install -e ".[dev]"
python -m server_flow.workflow
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `SERVER_BASE_URL` | dotflow-api base URL (e.g. `http://localhost:8000`) |
| `SERVER_USER_TOKEN` | API token for authentication (`X-User-Token`) |

## Running Tests

```bash
pytest
```

## How It Works

This example implements a `ServerAPI` that extends the `Server` ABC from dotflow. It sends workflow and task lifecycle events to a remote [dotflow-api](https://github.com/dotflow-io/dotflow-api) instance via HTTP.

### Server ABC Methods

| Method | Endpoint | When Called |
|--------|----------|------------|
| `create_workflow` | `POST /api/v1/workflows` | When a new `DotFlow` instance is created |
| `update_workflow` | `PATCH /api/v1/workflows/{id}` | When workflow starts, completes, or fails |
| `create_task` | `POST /api/v1/workflows/{id}/tasks` | When a task is added to the queue |
| `update_task` | `PATCH /api/v1/workflows/{id}/tasks/{id}` | When a task finishes execution |
