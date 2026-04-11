import unittest
from unittest.mock import patch, MagicMock

from dotflow import Config, DotFlow, action
from dotflow.core.types.status import TypeStatus


@action
def mock_extract(initial_context):
    return "<html><title>Test</title></html>"


class TestWorkflow(unittest.TestCase):

    def test_workflow_completes_with_mock_step(self):
        workflow = DotFlow()
        workflow.task.add(step=mock_extract, initial_context="http://test.com")
        workflow.start()

        tasks = workflow.result_task()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].status, TypeStatus.COMPLETED)
