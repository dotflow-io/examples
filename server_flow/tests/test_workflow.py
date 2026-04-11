import unittest
from unittest.mock import patch, MagicMock

from dotflow.core.dotflow import DotFlow
from dotflow.core.types.status import TypeStatus
from dotflow import Config

from server_flow.server import ServerAPI
from server_flow.actions import aggregate_results


class TestServerAPI(unittest.TestCase):

    @patch("server_flow.server.post")
    def test_create_workflow(self, mock_post):
        server = ServerAPI(base_url="http://localhost:8000", user_token="test-token")
        server.create_workflow(workflow="test-wf-id")

        mock_post.assert_called_once()
        args, kwargs = mock_post.call_args
        self.assertIn("/workflows", args[0])
        self.assertEqual(kwargs["json"]["workflow_id"], "test-wf-id")
        self.assertEqual(kwargs["headers"]["X-User-Token"], "test-token")

    @patch("server_flow.server.patch")
    def test_update_workflow(self, mock_patch):
        server = ServerAPI(base_url="http://localhost:8000", user_token="test-token")
        server.update_workflow(workflow="test-wf-id", status="In progress")

        mock_patch.assert_called_once()
        args, kwargs = mock_patch.call_args
        self.assertIn("/workflows/test-wf-id", args[0])
        self.assertEqual(kwargs["json"]["status"], "In progress")


class TestWorkflow(unittest.TestCase):

    @patch("server_flow.server.patch")
    @patch("server_flow.server.post")
    def test_workflow_with_server(self, mock_post, mock_patch):
        server = ServerAPI(base_url="http://localhost:8000", user_token="test-token")
        config = Config(server=server)

        workflow = DotFlow(config=config)
        workflow.task.add(
            step=aggregate_results,
            initial_context={"results": [
                {"url": "http://test.com", "status_code": 200, "data": {}},
            ]},
        )
        workflow.start()

        tasks = workflow.result_task()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].status, TypeStatus.COMPLETED)
        self.assertTrue(mock_post.called)
