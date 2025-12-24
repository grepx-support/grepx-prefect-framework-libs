"""Flow Registry - Manages Prefect flows."""

import logging
from typing import Dict, Any


class FlowRegistry:
    """Registry for managing Prefect flows."""
    
    def __init__(self):
        self._flows: Dict[str, Any] = {}
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug("FlowRegistry initialized")
    
    def register(self, name: str, flow_func):
        """Register a flow."""
        self._flows[name] = flow_func
        self.logger.debug(f"Registered flow: {name}")
    
    def get(self, name: str):
        """Get a registered flow by name."""
        flow = self._flows.get(name)
        if flow:
            self.logger.debug(f"Retrieved flow: {name}")
        else:
            self.logger.warning(f"Flow not found: {name}")
        return flow
    
    def has(self, name: str) -> bool:
        """Check if a flow is registered."""
        exists = name in self._flows
        self.logger.debug(f"Flow '{name}' exists: {exists}")
        return exists
    
    def list_items(self):
        """List all registered flows."""
        flow_names = list(self._flows.keys())
        self.logger.debug(f"Listing {len(flow_names)} flows")
        return flow_names
    
    def clear(self):
        """Clear all registered flows."""
        count = len(self._flows)
        self._flows.clear()
        self.logger.info(f"Cleared {count} flows")