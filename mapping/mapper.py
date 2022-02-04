from model.station.train_station import TrainStation


def map_to_train_station(train_station_json: dict) -> TrainStation:
    """
    Maps a JSON object representing a train station from the StaDa API to a `TrainStation`.

    :param train_station_json: the JSON representation of a train station, according to the StaDa API.

    :return: the mapped `TrainStation`.
    """
    eva_numbers = [eva_object["number"] for eva_object in train_station_json["evaNumbers"]]
    return TrainStation(name=train_station_json["name"], eva_numbers=eva_numbers)
