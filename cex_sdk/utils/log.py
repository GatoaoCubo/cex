"""
cex_sdk.utils.log -- Logging utilities.

Absorbed from: agno/utils/log.py
CEX version: 7.0.0
"""

import logging
import os

logger = logging.getLogger("cex_sdk")

_LOG_LEVEL = os.environ.get("CEX_LOG_LEVEL", "WARNING").upper()
logger.setLevel(getattr(logging, _LOG_LEVEL, logging.WARNING))

if not logger.handlers:
    _handler = logging.StreamHandler()
    _handler.setFormatter(logging.Formatter("[CEX] %(levelname)s %(message)s"))
    logger.addHandler(_handler)


def log_debug(msg: str, **kw) -> None:
    logger.debug(msg, **kw)

def log_info(msg: str, **kw) -> None:
    logger.info(msg, **kw)

def log_warning(msg: str, **kw) -> None:
    logger.warning(msg, **kw)

def log_error(msg: str, **kw) -> None:
    logger.error(msg, **kw)

def set_log_level_to_debug() -> None:
    logger.setLevel(logging.DEBUG)

def set_log_level_to_info() -> None:
    logger.setLevel(logging.INFO)
