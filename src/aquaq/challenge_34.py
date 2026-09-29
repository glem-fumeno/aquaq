from __future__ import annotations

import csv
from collections import defaultdict
from dataclasses import dataclass
from functools import total_ordering
from typing import Literal

from aquaq.utils import Time, TimeDelta

Train = str
Station = str
event_type_weight = {
    "enqueues": 1,
    "enters": 2,
    "leaves": 3,
}


@dataclass
@total_ordering
class Event:
    time: Time
    train: Train
    station: Station
    type: Literal["enqueues", "enters", "leaves"]

    def __repr__(self) -> str:
        return f"{self.time}: {self.train} {self.type} {self.station}"

    def __lt__(self, other: Event) -> bool:
        if self.time != other.time:
            return self.time < other.time
        if self.train != other.train:
            return self.train < other.train
        if self.station != other.station:
            return self.station < other.station
        match (self.type, other.type):
            case ("enters", "leaves"):
                return True
            case ("leaves", "enters"):
                return False
            case _:
                return False


def solve_34(file: str) -> int:
    reader = csv.DictReader(file.splitlines())
    assert reader.fieldnames is not None
    stations_by_train: dict[Train, list[Station]] = defaultdict(list)
    times_by_train: dict[Train, list[Time]] = defaultdict(list)
    for row in reader:
        station = row.pop("station")
        for train, time in row.items():
            if time == "":
                continue
            times_by_train[train].append(Time.from_str(time))
            stations_by_train[train].append(station)
    print(stations_by_train)
    print(times_by_train)
    deltas_by_train = {
        k: [te - ts for ts, te in zip(times[:-1], times[1:])]
        for k, times in times_by_train.items()
    }
    unique_stations = {
        station for stations in stations_by_train.values() for station in stations
    }
    events = []
    future_events = [
        Event(times[0], train, stations_by_train[train][0], "enqueues")
        for train, times in times_by_train.items()
    ]
    train_queue_by_station: dict[Station, list[Train]] = {
        station: [] for station in unique_stations
    }
    while len(future_events) > 0:
        future_events.sort()
        event = future_events.pop(0)
        print(event)
        match event.type:
            case "enqueues":
                train_queue_by_station[event.station].append(event.train)
                if len(train_queue_by_station[event.station]) <= 1:
                    future_events.append(
                        Event(
                            event.time,
                            train_queue_by_station[event.station].pop(0),
                            event.station,
                            "enters",
                        )
                    )
            case "enters":
                future_events.append(
                    Event(
                        event.time + TimeDelta.from_minutes(5),
                        event.train,
                        event.station,
                        "leaves",
                    )
                )
            case "leaves":
                waiting_train = train_queue_by_station[event.station].pop(0)
                stations_by_train[event.train].pop(0)
                if len(deltas_by_train[event.train]) > 0:
                    delta = deltas_by_train[event.train].pop(0)
                    future_events.append(
                        Event(
                            event.time + delta,
                            waiting_train,
                            stations_by_train[event.train][0],
                            "enqueues",
                        )
                    )
                if len(train_queue_by_station[event.station]) > 0:
                    future_events.append(
                        Event(
                            event.time,
                            train_queue_by_station[event.station].pop(0),
                            event.station,
                            "enters",
                        )
                    )
        events.append(event)
    return 0
