"""Prefect Framework."""

from grepx_connection_registry import ConnectionFactory
from .src.prefect_framework.prefect_connection import PrefectConnection

# Comment out the registration since it's already handled by the price_app version
# ConnectionFactory.register('prefect', PrefectConnection)

__all__ = ["PrefectConnection"]