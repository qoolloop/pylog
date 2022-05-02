"""Logging with specific configuration."""
from enum import IntEnum
import logging
from logging import (  # noqa: F401 # for export
    getLogger,
    Logger,
)

__all__ = (
    'getLogger',
    'Logger',  #FUTURE: Hide methods
    'INFO', 'WARNING', 'ERROR', 'DEBUG',
)


logging.basicConfig(
    format="\n@%(asctime)s:%(levelname)s:%(module)s(%(lineno)d)\n%(message)s",
    level=logging.INFO)


class Level(IntEnum):
    """Levels for logging."""
    
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    INFO = logging.INFO
    DEBUG = logging.DEBUG


#: ERROR logging level
ERROR = Level.ERROR

#: WARNING logging level
WARNING = Level.WARNING

#: INFO logging level
INFO = Level.INFO

#: DEBUG logging level
DEBUG = Level.DEBUG
