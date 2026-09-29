from __future__ import annotations

from datetime import datetime, timedelta
from functools import total_ordering

today = datetime.today()


@total_ordering
class Time:
    value: datetime

    def __init__(self, value: datetime) -> None:
        self.value = value

    @classmethod
    def from_str(cls, time: str):
        h, m = time.split(":")
        return cls(today.replace(hour=int(h), minute=int(m), second=0, microsecond=0))

    def __repr__(self) -> str:
        return self.value.strftime("%H:%M")

    def __add__(self, other: TimeDelta) -> Time:
        return Time(self.value + other.delta)

    def __sub__(self, other: Time) -> TimeDelta:
        return TimeDelta(self.value - other.value)

    def __lt__(self, other: Time) -> bool:
        return self.value < other.value


class TimeDelta:
    def __init__(self, delta: timedelta) -> None:
        self.delta = delta

    @classmethod
    def from_minutes(cls, value: int):
        return cls(timedelta(minutes=value))

    def __repr__(self) -> str:
        return f"+{self.delta.total_seconds() // 60}"
