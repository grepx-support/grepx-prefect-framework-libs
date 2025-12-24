"""Task Registry - Manages Prefect tasks."""

import logging
from typing import Dict, Any


class TaskRegistry:
    """Registry for managing Prefect tasks."""
    
    def __init__(self):
        self._tasks: Dict[str, Any] = {}
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug("TaskRegistry initialized")
    
    def register(self, name: str, task_func):
        """Register a task."""
        self._tasks[name] = task_func
        self.logger.debug(f"Registered task: {name}")
    
    def get(self, name: str):
        """Get a registered task by name."""
        task = self._tasks.get(name)
        if task:
            self.logger.debug(f"Retrieved task: {name}")
        else:
            self.logger.warning(f"Task not found: {name}")
        return task
    
    def has(self, name: str) -> bool:
        """Check if a task is registered."""
        exists = name in self._tasks
        self.logger.debug(f"Task '{name}' exists: {exists}")
        return exists
    
    def list_items(self):
        """List all registered tasks."""
        task_names = list(self._tasks.keys())
        self.logger.debug(f"Listing {len(task_names)} tasks")
        return task_names
    
    def clear(self):
        """Clear all registered tasks."""
        count = len(self._tasks)
        self._tasks.clear()
        self.logger.info(f"Cleared {count} tasks")