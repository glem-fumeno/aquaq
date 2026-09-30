from __future__ import annotations

import textwrap
from collections.abc import Iterable
from dataclasses import asdict, is_dataclass
from datetime import datetime, timedelta
from functools import total_ordering
from typing import Any, cast

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

    def __eq__(self, other: Time, /) -> bool:
        return self.value == other.value


@total_ordering
class TimeDelta:
    def __init__(self, delta: timedelta) -> None:
        self.delta = delta

    @classmethod
    def from_minutes(cls, value: int):
        return cls(timedelta(minutes=value))

    def minutes(self) -> int:
        return int(self.delta.total_seconds()) // 60

    def __repr__(self) -> str:
        return f"+{self.delta.total_seconds() // 60}"

    def __lt__(self, other: TimeDelta) -> bool:
        return self.delta < other.delta

    def __eq__(self, other: TimeDelta, /) -> bool:
        return self.delta == other.delta


def pretty_print(obj: Any, max_depth: int | None = None):
    result = format_object(obj, 0, max_depth)
    print("\n" + result)


def indent(values: Iterable[str], p: str) -> str:
    text = textwrap.indent("\n".join(values), "  ", lambda _: True)
    return f"{p[0]}\n{text}\n{p[1]}"


def format_object(obj: Any, depth: int, max_depth: int | None):
    if max_depth is not None and depth > max_depth:
        return f"{obj}"
    if is_dataclass(obj):
        o: Any = obj
        obj = asdict(o)

    def fmt(value: Any) -> str:
        return format_object(value, depth + 1, max_depth)

    match obj:
        case dict():
            obj = cast(dict[Any, Any], obj)
            return indent((f"{k}: {fmt(v)}" for k, v in obj.items()), "{}")
        case list():
            obj = cast(list[Any], obj)
            return indent((fmt(v) for v in obj), "[]")
        case tuple():
            obj = cast(tuple[Any, ...], obj)
            return indent((fmt(v) for v in obj), "()")
        case set():
            obj = cast(set[Any], obj)
            return indent((fmt(v) for v in obj), "{}")
        case _:
            return f"{obj}"
