from datetime import datetime
from xml.etree import ElementTree

from model.station.train_station import TrainStation
from model.timetable.timetable_entry import TimeTableEntry
from model.timetable.timetable import TimeTable


def map_to_train_station(train_station_json: dict) -> TrainStation:
    """
    Maps a JSON object representing a train station from the StaDa API to a `TrainStation`.

    :param train_station_json: the JSON representation of a train station, according to the StaDa API.

    :return: the mapped `TrainStation`.
    """
    eva_numbers = [eva_object["number"] for eva_object in train_station_json["evaNumbers"]]
    return TrainStation(name=train_station_json["name"], eva_numbers=eva_numbers)


def map_to_timetable(timetable_tree: ElementTree) -> TimeTable:
    """
    Maps an XML Tree representing a train station's time table from the TimeTable API to a `TimeTable`.
    
    :param timetable_tree: the xml string representing the timetable.
    
    :return: the mapped `TimeTable`.
    """
    table_train_station = timetable_tree.get("station")

    entries = list()
    for train_entry in timetable_tree:
        train_details = train_entry.find("tl")
        train_category = train_details.get("c")
        train_number = train_details.get("n")

        arrival = train_entry.find("ar")
        departure = train_entry.find("dp")

        route = list()
        if arrival is not None:
            path_before_arrival = arrival.get("ppth").split("|")
            for train_station in path_before_arrival:
                route.append(train_station)

        route.append(table_train_station)

        if departure is not None:
            path_after_departure = departure.get("ppth").split("|")
            for train_station in path_after_departure:
                route.append(train_station)

        entry = TimeTableEntry(
            train=f"{train_category} {train_number}",
            arrival_time=map_to_datetime(arrival.get("pt"), format='%y%m%d%H%M') if arrival is not None else None,
            departure_time=map_to_datetime(departure.get("pt"), format='%y%m%d%H%M') if departure is not None else None,
            route=route
        )
        entries.append(entry)

    return TimeTable(train_station=table_train_station, entries=entries)


def map_to_datetime(datetime_string: str, format: str) -> datetime:
    """
    Maps a string representing a datetime into a `datetime` using the given `format`.

    Example: '202201011322' for 2022-01-01 13:22

    :param datetime_string: the string representing the datetime.
    :param format: the format string to use for converting the datetime string.

    :return: the mapped `datetime`.
    """
    return datetime.strptime(datetime_string, format)
