from collections import defaultdict
from dataclasses import dataclass
from functools import cached_property, total_ordering
from typing import ClassVar

from aquaq.utils import Time, TimeDelta, format_object, pretty_print

Train = str
Station = str


@dataclass
@total_ordering
class _Event:
    ORDER: ClassVar[int]
    train: Train
    time: Time

    @property
    def sort_by(self):
        return (self.time, self.train, self.ORDER)

    def __lt__(self, other: Event) -> bool:
        if self.time != other.time:
            return self.time < other.time
        match self, other:
            case DepartEvent(), DepartEvent():
                if self.train != other.train:
                    return self.train < other.train
                if self.origin != other.origin:
                    return self.origin < other.origin
                return self.destination < other.destination
            case EnqueueEvent(), EnqueueEvent():
                if self.origin != other.origin:
                    return self.origin < other.origin
                if self.train != other.train:
                    return self.train < other.train
                return self.destination < other.destination
            case ArriveEvent(), ArriveEvent():
                if self.train != other.train:
                    return self.train < other.train
                return self.station < other.station
            case _:
                if self.ORDER != other.ORDER:
                    return self.ORDER < other.ORDER
                return self.train < other.train


@dataclass
class DepartEvent(_Event):
    ORDER = 2
    origin: Station
    destination: Station

    def __repr__(self) -> str:
        return f"{self.time} - {self.train} leaves {self.origin} for {self.destination}"


@dataclass
class EnqueueEvent(_Event):
    ORDER = 1
    origin: Station
    destination: Station

    def __repr__(self) -> str:
        return f"{self.time} - {self.train} parks outside {self.destination}"


@dataclass
class ArriveEvent(_Event):
    ORDER = 3
    station: Station

    def __repr__(self) -> str:
        return f"{self.time} - {self.train} enters {self.station}"


Event = DepartEvent | EnqueueEvent | ArriveEvent


class Schedule:
    def __init__(self, file: str) -> None:
        self.file = file

    @cached_property
    def times_by_train(self) -> dict[Train, list[tuple[Time, Station]]]:
        trains, *schedule = self.file.splitlines()
        trains = trains.split(",")[1:]
        times_by_train: dict[Train, list[tuple[Time, Station]]] = defaultdict(list)
        for station in schedule:
            station_name, *times = station.split(",")
            for time, train in zip(times, trains):
                if time == "":
                    continue
                times_by_train[train].append((Time.from_str(time), station_name))
        return times_by_train

    @cached_property
    def delta_by_train_station(self) -> dict[Train, dict[Station, TimeDelta]]:
        deltas_by_train: dict[Train, dict[Station, TimeDelta]] = defaultdict(dict)
        for train, schedule in self.times_by_train.items():
            for (ts, _), (te, se) in zip(schedule[:-1], schedule[1:]):
                deltas_by_train[train][se] = te - ts
        return deltas_by_train

    @cached_property
    def start_by_train(self) -> dict[Train, tuple[Time, Station]]:
        return {t: s[0] for t, s in self.times_by_train.items()}

    @cached_property
    def stations(self) -> set[Station]:
        return {s for times in self.times_by_train.values() for (_, s) in times}

    @cached_property
    def next_stations(self) -> dict[Train, dict[Station, Station]]:
        return {
            train: {
                source: destination
                for (_, source), (_, destination) in zip(schedule[:-1], schedule[1:])
            }
            for train, schedule in self.times_by_train.items()
        }

    @cached_property
    def fixed_departures(self) -> dict[Train, list[tuple[Time, Station]]]:
        future_events: list[Event] = [
            EnqueueEvent(train, time, "", station)
            for train, (time, station) in self.start_by_train.items()
        ]
        queue_by_station: dict[Station, list[tuple[Station, Train]]] = {
            s: [] for s in self.stations
        }
        departures: dict[Train, list[tuple[Time, Station]]] = defaultdict(list)
        while len(future_events) > 0:
            future_events.sort()
            event = future_events.pop(0)
            match event:
                case EnqueueEvent():
                    queue_by_station[event.destination].append(
                        (event.origin, event.train)
                    )
                    if len(queue_by_station[event.destination]) <= 1:
                        future_events.append(
                            ArriveEvent(
                                train=event.train,
                                time=event.time,
                                station=event.destination,
                            )
                        )
                case ArriveEvent():
                    destination = ""
                    if event.station in self.next_stations[event.train]:
                        destination = self.next_stations[event.train][event.station]
                    future_events.append(
                        DepartEvent(
                            train=event.train,
                            time=event.time + TimeDelta.from_minutes(5),
                            origin=event.station,
                            destination=destination,
                        )
                    )
                case DepartEvent():
                    departures[event.train].append((event.time, event.origin))
                    if event.destination in self.delta_by_train_station[event.train]:
                        delta = self.delta_by_train_station[event.train][
                            event.destination
                        ]
                        future_events.append(
                            EnqueueEvent(
                                train=event.train,
                                time=event.time + delta,
                                origin=event.origin,
                                destination=event.destination,
                            )
                        )
                    queue_by_station[event.origin].pop(0)
                    if len(queue_by_station[event.origin]) > 0:
                        queue_by_station[event.origin].sort()
                        _, train = queue_by_station[event.origin][0]
                        future_events.append(
                            ArriveEvent(
                                train=train, time=event.time, station=event.origin
                            )
                        )
            # print(event)
        return departures

    def __repr__(self) -> str:
        return "" + "\nstarts:\n" + format_object(self.start_by_train, 0, 0)


def solve_34(file: str) -> int:
    schedule = Schedule(file)
    departures = schedule.fixed_departures
    runtimes: dict[Train, TimeDelta] = {}
    for train, times in departures.items():
        runtimes[train] = times[-1][0] - schedule.start_by_train[train][0]
    pretty_print(runtimes, 1)
    return max(runtimes.values()).minutes()
