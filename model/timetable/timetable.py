from xml.etree import ElementTree
from model.timetable.timetable_entry import TimeTableEntry
from utils.time import parse_datetime

from dataclasses import dataclass


@dataclass
class TimeTable:
    """
    Data object representing a timetable of a train station.

    Attributes
    ----------

    train_station : str
        the name of the train station associated with this timetable.
    entires : list
        list of entries, each representing a train arriving and / or departing from `train_station`.
    """

    train_station: str
    entries: list

    def __repr__(self):
        return "Timetable({} - {} entries)".format(self.train_station, len(self.entries))

    @classmethod
    def from_xml_string(cls, xml_string):
        """
        Constructs a `TimeTable` from the given XML string.

        :param xml_string: the string representing the timetable in XML.
        :type xml_string: str

        :return: a corresponding `TimeTable`.
        """
        timetable_tree = ElementTree.fromstring(xml_string)
        table_train_station = timetable_tree.get("station")

        entries = list()
        for train_entry in timetable_tree:
            train_details = train_entry.find("tl")
            train_type = train_details.get("c")
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
                train=f"{train_type} {train_number}",
                arrival_time=parse_datetime(arrival.get("pt")) if arrival is not None else None,
                departure_time=parse_datetime(departure.get("pt")) if departure is not None else None,
                route=route
            )
            entries.append(entry)

        return cls(table_train_station, entries)
