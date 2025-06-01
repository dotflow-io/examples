<div align="center">
  <a aria-label="Serverless.com" href="https://dotflow.io">Website</a>
  &nbsp;•&nbsp;
  <a aria-label="Dotglow Documentation" href="
dotflow-io.github.io/dotflow/">Documentation</a>
  &nbsp;•&nbsp;
  <a aria-label="Pypi" href="https://pypi.org/project/dotflow/">Pypi</a>
</div>

<br/>

<div align="center">

![](https://raw.githubusercontent.com/FernandoCelmer/dotflow/master/docs/assets/dotflow.gif)

![GitHub Org's stars](https://img.shields.io/github/stars/dotflow-io?label=Dotflow&style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/dotflow-io/dotflow?style=flat-square)
![PyPI](https://img.shields.io/pypi/v/dotflow?style=flat-square)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dotflow?style=flat-square)
![PyPI - Downloads](https://img.shields.io/pypi/dm/dotflow?style=flat-square)
[![❤️ Test Flow](https://github.com/dotflow-io/examples/actions/workflows/python-app-flow.yml/badge.svg)](https://github.com/dotflow-io/examples/actions/workflows/python-app-flow.yml)
[![⚙️ ETL Flow](https://github.com/dotflow-io/examples/actions/workflows/python-etl-flow.yml/badge.svg)](https://github.com/dotflow-io/examples/actions/workflows/python-etl-flow.yml)
</div>

# Dotflow Examples

Start with the basics [here](https://dotflow-io.github.io/dotflow/nav/getting-started/).

---

| Example                                                                                                                          |                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------- |--------------------------------------------------------------------------------------------|
| [cli_with_callback](https://github.com/dotflow-io/examples/blob/master/cli_with_callback.py)                                     | `dotflow start --step cli_with_callback.simple_step --callback cli_with_callback.callback` |
| [cli_with_initial_context](https://github.com/dotflow-io/examples/blob/master/cli_with_initial_context.py)                       | `dotflow start --step cli_with_initial_context.simple_step --initial-context abc`          |
| [cli_with_mode](https://github.com/dotflow-io/examples/blob/master/cli_with_mode.py)                                             | `dotflow start --step cli_with_mode.simple_step --mode sequential`                         |
| [cli_with_output_context](https://github.com/dotflow-io/examples/blob/master/cli_with_output_context.py)                         | `dotflow start --step cli_with_output_context.simple_step --storage file`                  |
| [cli_with_path](https://github.com/dotflow-io/examples/blob/master/cli_with_path.py)                                             | `dotflow start --step cli_with_path.simple_step --path .storage --storage file`            |
| [simple_cli](https://github.com/dotflow-io/examples/blob/master/simple_cli.py)                                                   | `dotflow start --step simple_cli.simple_step`                                              |
| [simple_class_workflow](https://github.com/dotflow-io/examples/blob/master/simple_class_workflow.py)                             | `python simple_class_workflow.py`                                                          |
| [simple_function_workflow_with_error](https://github.com/dotflow-io/examples/blob/master/simple_function_workflow_with_error.py) | `python simple_function_workflow_with_error.py`                                            |
| [simple_function_workflow](https://github.com/dotflow-io/examples/blob/master/simple_function_workflow.py)                       | `python simple_function_workflow.py`                                                       |
| [step_class_result_context](https://github.com/dotflow-io/examples/blob/master/step_class_result_context.py)                     | `python step_class_result_context.py`                                                      |
| [step_class_result_storage](https://github.com/dotflow-io/examples/blob/master/step_class_result_storage.py)                     | `python step_class_result_storage.py`                                                      |
| [step_class_result_task](https://github.com/dotflow-io/examples/blob/master/step_class_result_task.py)                           | `python step_class_result_task.py`                                                         |
| [step_function_result_context](https://github.com/dotflow-io/examples/blob/master/step_function_result_context.py)               | `python step_function_result_context.py`                                                   |
| [step_function_result_storage](https://github.com/dotflow-io/examples/blob/master/step_function_result_storage.py)               | `python step_function_result_storage.py`                                                   |
| [step_function_result_task](https://github.com/dotflow-io/examples/blob/master/step_function_result_task.py)                     | `python step_function_result_task.py`                                                      |
| [step_with_initial_context](https://github.com/dotflow-io/examples/blob/master/step_with_initial_context.py)                     | `python step_with_initial_context.py`                                                      |
| [step_with_many_contexts](https://github.com/dotflow-io/examples/blob/master/step_with_many_contexts.py)                         | `python step_with_many_contexts.py`                                                        |
| [step_with_previous_context](https://github.com/dotflow-io/examples/blob/master/step_with_previous_context.py)                   | `python step_with_previous_context.py`                                                     |
| [workflow_keep_going_true](https://github.com/dotflow-io/examples/blob/master/workflow_keep_going_true.py)                       | `python workflow_keep_going_true.py`                                                       |
| [workflow_step_callback](https://github.com/dotflow-io/examples/blob/master/workflow_step_callback.py)                           | `python workflow_step_callback.py`                                                         |
| [workflow_with_callback_failure](https://github.com/dotflow-io/examples/blob/master/workflow_with_callback_failure.py)           | `python workflow_with_callback_failure.py`                                                 |
| [workflow_with_callback_success](https://github.com/dotflow-io/examples/blob/master/workflow_with_callback_success.py)           | `python workflow_with_callback_success.py`                                                 |
| [workflow_with_retry](https://github.com/dotflow-io/examples/blob/master/workflow_with_retry.py)                                 | `python workflow_with_retry.py`                                                            |
| [step_with_groups](https://github.com/dotflow-io/examples/blob/master/step_with_groups.py)                                       | `python step_with_groups.py`                                                               |
| [workflow_background_mode](https://github.com/dotflow-io/examples/blob/master/workflow_background_mode.py)                       | `python workflow_background_mode.py`                                                       |
| [workflow_parallel_mode](https://github.com/dotflow-io/examples/blob/master/workflow_parallel_mode.py)                           | `python workflow_parallel_mode.py`                                                         |
| [workflow_sequential_group_mode](https://github.com/dotflow-io/examples/blob/master/workflow_sequential_group_mode.py)           | `python workflow_sequential_group_mode.py`                                                 |
| [workflow_sequential_mode](https://github.com/dotflow-io/examples/blob/master/workflow_sequential_mode.py)                       | `python workflow_sequential_mode.py`                                                       |


## Commit Style

- ⚙️ FEATURE
- 📝 PEP8
- 📌 ISSUE
- 🪲 BUG
- 📘 DOCS
- 📦 PyPI
- ❤️️ TEST
- ⬆️ CI/CD
- ⚠️ SECURITY

## License
![GitHub License](https://img.shields.io/github/license/dotflow-io/dotflow)

This project is licensed under the terms of the MIT License.