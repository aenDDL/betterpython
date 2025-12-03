from enum import StrEnum, auto
from typing import Callable
from collections import defaultdict


class EventTypes(StrEnum):
    REGISTRATION = auto()
    PASSWORD_CHANGE = auto()
    PLAN_UPGRADE = auto()


def on_event(event_type):
    def decorator(func):
        subscribe(event_type, func)
        return func
    return decorator


events: dict[str, list[Callable]] = defaultdict(list)
    
def publish(event_type: EventTypes, data) -> None:
    if event_type not in events:
        raise ValueError(f"{event_type} not in valid event types.")
    for event in events[event_type]:
        event(data)


def subscribe(event_type: EventTypes, func: Callable) -> None:
    events[event_type].append(func) if func not in events[event_type] else None

