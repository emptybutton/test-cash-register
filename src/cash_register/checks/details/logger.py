from structlog import wrap_logger
from structlog.types import FilteringBoundLogger

from cash_register.monitoring.structlog import AddRequestId, default_logger


type Logger = FilteringBoundLogger


def logger() -> Logger:
    return wrap_logger(default_logger, processors=[AddRequestId()])
