from dataclasses import dataclass, field
from uuid import UUID, uuid4

import structlog
from structlog.types import EventDict, FilteringBoundLogger


default_logger: FilteringBoundLogger = structlog.wrap_logger(
    structlog.PrintLogger(),
    processors=[
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso", utc=True),
        structlog.processors.dict_tracebacks,
        structlog.processors.JSONRenderer(),
    ],
)


@dataclass(kw_only=True, frozen=True, slots=True)
class AddRequestId:
    request_id: UUID = field(default_factory=uuid4)

    def __call__(self, _: object, __: str, event_dict: EventDict) -> EventDict:
        event_dict["request_id"] = self.request_id.hex
        return event_dict
