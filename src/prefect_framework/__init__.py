"""Prefect Framework Library.

A flexible Prefect orchestration library with registry pattern for managing flows and tasks.
"""

from .prefect_app import PrefectApp
from .flows.flow_registry import FlowRegistry
from .tasks.task_registry import TaskRegistry
from .prefect_connection import PrefectConnection

__all__ = [
    "PrefectApp",
    "FlowRegistry",
    "TaskRegistry",
    "PrefectConnection",
]

__version__ = "1.0.0"