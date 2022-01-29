from requests.structures import CaseInsensitiveDict
from datetime import datetime

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

    def get_request(self, request_url, params=None, headers=None):
        """
        Makes an HTTP GET Request to the specified `request_url` and returns the response.

        :param request_url: the URL for the GET Request.
        :return: the retrieved response.
        """
        logger.debug("HTTP GET Request to {}".format(request_url))
        try:
            response = requests.get(request_url, params=params, headers=self.__get_headers() if headers is None else headers)
            logger.debug("Response (HTTP Status Code: {}): {}".format(response.status_code, response.json()))
            return response
        except requests.exceptions.RequestException as err:
            logger.error("Error upon HTTP Request: {}".format(err))
            raise SystemExit(1)

    def get_stations(self, station_name):
        """
        Retrieves the IDs of the train station(s) that either partially or fully match(es) the given `station_name`.

        :param station_name: a fraction or the full name of a train station.
        :type station_name: str

        :return: a JSON-Array containing name, id, longitude and latitude of all train stations that matched the
                 given name. An empty dictionary is returned if no train stations could be found.
        :rtype: list
        """
        request_url = f"{self.base_url}/freeplan/v1/location/{station_name}"
        response = self.get_request(request_url)

        if not response.ok:
            logger.error("HTTP Status Code {}: There was an error on the server side: {})".format(response.status_code,
                                                                                                 response.json()))
            return list()

        logging.debug("Response: {}".format(response.json()))
        return response.json()

    def get_departures(self, station_id, start_datetime=None):
        """
        Retrieves the departures for the train station matching the given `station_id`, starting from `start_datetime`.

        :param station_id: the ID of the specific train station.
        :type station_id: int
        :param start_datetime: the beginning of the time interval that is used to retrieve departures.
                               Has to be date and time according to the ISO-8601 format (YYYY-MM-DDThh:mm:ss)
        :type start_datetime: datetime

        :return: a JSON-Array containing the departures for the train station.
        :rtype: list
        """
        request_url = f"{self.base_url}/freeplan/v1/departureBoard/{station_id}"
        params = {"date": datetime.now().isoformat() if start_datetime is None else start_datetime}

        response = self.get_request(request_url, params=params)

        if not response.ok:
            logger.error("HTTP Status Code {}: There was an error on the server side: {})".format(response.status_code,
                                                                                                 response.json()))
            return list()

        logging.debug("Response: {}".format(response.json()))
        return response.json()

    def get_journey_details(self, journey_id):
        """
        Retrieves the details for the journey matching the given `journey_id`.

        :param journey_id: the ID of the specific journey.
        :type journey_id: int

        :return: a JSON-Array containing the details of the specified journey.
        :rtype: list
        """
        request_url = f"{self.base_url}/freeplan/v1/journeyDetails/{journey_id}"
        response = self.get_request(request_url)

        if not response.ok:
            logger.error("HTTP Status Code {}: There was an error on the server side: {})".format(response.status_code,
                                                                                                 response.json()))
            return list()

        logging.debug("Response: {}".format(response.json()))
        return response.json()

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
