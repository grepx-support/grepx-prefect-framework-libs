"""Prefect App - Main application class."""

import logging
from typing import Dict, Any, Optional
from .flows.flow_registry import FlowRegistry
from .tasks.task_registry import TaskRegistry


class PrefectApp:
    """Main Prefect application class."""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.logger = logging.getLogger(self.__class__.__name__)
        self.flow_registry = FlowRegistry()
        self.task_registry = TaskRegistry()
        self.logger.debug("PrefectApp initialized")
    
    def register_flow(self, name: str, flow_func):
        """Register a flow with the flow registry."""
        self.flow_registry.register(name, flow_func)
        self.logger.info(f"Registered flow: {name}")
    
    def register_task(self, name: str, task_func):
        """Register a task with the task registry."""
        self.task_registry.register(name, task_func)
        self.logger.info(f"Registered task: {name}")
    
    def get_flow(self, name: str):
        """Get a registered flow by name."""
        return self.flow_registry.get(name)
    
    def get_task(self, name: str):
        """Get a registered task by name."""
        return self.task_registry.get(name)
    
    def list_flows(self):
        """List all registered flows."""
        return self.flow_registry.list_items()
    
    def list_tasks(self):
        """List all registered tasks."""
        return self.task_registry.list_items()