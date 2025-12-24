# Prefect Framework Library

A flexible Prefect orchestration library with registry pattern for managing flows and tasks.

## Features

- **Registry Pattern**: Register and manage different flows and tasks dynamically
- **Factory Pattern**: Create flow and task instances based on configuration
- **Base Classes**: Extensible base classes for creating custom flows and tasks
- **Flow Caching**: Automatic flow instance caching and reuse
- **Task Management**: Centralized task registration and retrieval

## Installation

```bash
# Install from local development
pip install -e libs/prefect_framework

# Or add to requirements.txt
-e libs/prefect_framework
```

## Quick Start

### Define a Custom Flow

```python
from prefect_framework import PrefectApp

# Create app instance
app = PrefectApp()

# Register flows
from my_flows import my_etl_flow
app.register_flow("etl", my_etl_flow)

# Get flows
flow = app.get_flow("etl")
```

### Define a Custom Task

```python
from prefect_framework import PrefectApp

# Create app instance
app = PrefectApp()

# Register tasks
from my_tasks import fetch_data_task
app.register_task("fetch_data", fetch_data_task)

# Get tasks
task = app.get_task("fetch_data")
```

## License

MIT