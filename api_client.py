from requests.structures import CaseInsensitiveDict

import requests
import os
import logging


logger = logging.getLogger(__name__)


class DbApiClient:
    """
    API Client for the Deutsche Bahn APIs.
    """

    def __init__(self, base_url):
        """
        Constructor.

        :param base_url: the base URL of the Deutsche Bahn APIs.
        :type base_url: str
        """
        self.base_url = base_url

    def get_stations(self, station_name):
        """
        Retrieves the IDs of the train station(s) that either partially or fully match(es) the given `station_name`.

        :param station_name: a fraction or the full name of a train station.
        :type station_name: str

        :return: a dictionary containing name, id, longitude and latitude of all train_stations that matched the
                 given name. An empty dictionary is returned if no train stations could be found.
        :rtype: dict
        """
        query_url = f"{self.base_url}/freeplan/v1/location/{station_name}"
        logger.debug("HTTP Request to {}".format(query_url))
        try:
            response = requests.get(query_url, headers=self.__get_headers())
        except requests.exceptions.RequestException as err:
            logger.error("Error upon HTTP Request: {}".format(err))
            raise SystemExit(1)

        if not response.ok:
            logger.info("No train station could be found. (HTTP Status Code {})".format(response.status_code))
            return dict()
        else:
            logger.info("Response HTTP Status Code: {}".format(response.status_code))

            train_stations = response.json()
            logger.debug("Response: {}".format(train_stations))
            return train_stations

    def get_departures(self, station_id):
        """
        Retrieves the departures for the train station matching the given `id`.
        
        :param station_id: the ID of the specific train station.
        :type station_id: int
        
        :return:
        :rtype:
        """
        pass  # TODO

    def __get_headers(self):
        """
        Returns the basic necessary headers needed for querying the Deutsche Bahn APIs.

        :return: a dictionary containing the headers.
        :rtype: requests.CaseInsensitiveDict
        """
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Authorization"] = "Bearer {}".format(os.environ["DB_API_KEY"])
        return headers
