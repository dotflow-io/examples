"""Integrations Test"""

from cli_with_callback import main as cli_with_callback
from cli_with_initial_context import main as cli_with_initial_context
from cli_with_mode import main as cli_with_mode
from cli_with_output_context import main as cli_with_output_context
from cli_with_path import main as cli_with_path
from simple_class_workflow import main as simple_class_workflow
from simple_cli import main as simple_cli
from simple_function_workflow import main as simple_function_workflow
from simple_function_workflow_with_error import main as simple_function_workflow_with_error
from step_class_result_context import main as step_class_result_context
from step_class_result_storage import main as step_class_result_storage
from step_class_result_task import main as step_class_result_task
from step_function_result_context import main as step_function_result_context
from step_function_result_storage import main as step_function_result_storage
from step_function_result_task import main as step_function_result_task
from step_with_groups import main as step_with_groups
from step_with_initial_context import main as step_with_initial_context
from step_with_many_contexts import main as step_with_many_contexts
from step_with_previous_context import main as step_with_previous_context
from step_with_storage_file import main as step_with_storage_file
from step_with_storage_mongodb import main as step_with_storage_mongodb
from workflow_background_mode import main as workflow_background_mode
from workflow_keep_going_true import main as workflow_keep_going_true
from workflow_parallel_mode import main as workflow_parallel_mode
from workflow_sequential_group_mode import main as workflow_sequential_group_mode
from workflow_sequential_mode import main as workflow_sequential_mode
from workflow_step_callback import main as workflow_step_callback
from workflow_with_callback_failure import main as workflow_with_callback_failure
from workflow_with_callback_success import main as workflow_with_callback_success
from workflow_with_retry import main as workflow_with_retry


def main():
    cli_with_callback()
    cli_with_initial_context()
    cli_with_mode()
    cli_with_output_context()
    cli_with_path()
    simple_class_workflow()
    simple_cli()
    simple_function_workflow()
    simple_function_workflow_with_error()
    step_class_result_context()
    step_class_result_storage()
    step_class_result_task()
    step_function_result_context()
    step_function_result_storage()
    step_function_result_task()
    step_with_groups()
    step_with_initial_context()
    step_with_many_contexts()
    step_with_previous_context()
    step_with_storage_file()
    step_with_storage_mongodb()
    workflow_background_mode()
    workflow_keep_going_true()
    workflow_parallel_mode()
    workflow_sequential_group_mode()
    workflow_sequential_mode()
    workflow_step_callback()
    workflow_with_callback_failure()
    workflow_with_callback_success()
    workflow_with_retry()


if __name__ == "__main__":
    main()
