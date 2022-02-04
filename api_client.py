import xml.etree.ElementTree

from requests.structures import CaseInsensitiveDict
from datetime import datetime
from model.timetable.timetable import TimeTable
from mapping.mapper import map_to_train_station, map_to_timetable

import requests
import os
import logging

logger = logging.getLogger(__name__)


class DbApiClient:
    """ API Client for the Deutsche Bahn APIs. """

    def __init__(self, base_url: str):
        """
        Constructor.

        :param base_url: the base URL of the Deutsche Bahn APIs.
        """
        self.base_url = base_url

    def get_stations(self, station_name: str, max_results: int = 50) -> list:
        """
        Returns the train stations that either partially or fully match the given `station_name`.

        This method queries the Deutsche Bahn StaDa API.\n
        See more at https://developer.deutschebahn.com/store/apis/info?name=StaDa-Station_Data&version=v2&provider=DBOpenData

        :param station_name: a fraction or the full name of a train station.
                             Multiple stations can be included by seperating them with a comma.
                             May contain wildcards (*).
        :param max_results: the maximum amount of results to be fetched from the API.

        :return: a list of `TrainStation` objects or an empty list if train stations matched the criteria.
        """
        url_parameters = {
            "searchstring": station_name,
            "limit": max_results
        }

        request_url = f"{self.base_url}/stada/v2/stations"
        response = self.__get_request(request_url, params=url_parameters)

        if not response.ok:
            logger.error("HTTP Status Code {}: There was an error on the server side: {})".format(response.status_code,
                                                                                                  response.json()))
            return list()

        logger.debug("Response: {}".format(response.json()))
        return [map_to_train_station(station_json) for station_json in response.json().get("result")]

    def get_departures(self, station_id: int) -> TimeTable:
        """
        Retrieves the departures for the train station matching the given `station_id`.

        This method queries the Deutsche Bahn TimeTable API.\n
        See more at https://developer.deutschebahn.com/store/apis/info?name=Timetables&version=v1&provider=DBOpenData

        :param station_id: the ID of the specific train station.
        :type station_id: int

        :return: a JSON-Array containing the departures for the train station.
        """
        current_date = datetime.now()
        YYMMDD = current_date.strftime('%y') + current_date.strftime('%m') + current_date.strftime('%d')
        current_hour = current_date.strftime('%H')

        request_url = f"{self.base_url}/timetables/v1/plan/{station_id}/{YYMMDD}/{current_hour}"
        response = self.__get_request(request_url)

        if not response.ok:
            logger.error("HTTP Status Code {}: There was an error on the server side: {})".format(response.status_code,
                                                                                                 response.content))
            return None

        logger.debug("Response: {}".format(response.content))

        xml_response = response.content.decode('utf-8')
        return map_to_timetable(xml.etree.ElementTree.fromstring(xml_response))

    def __get_request(self, request_url: str, params: dict = None, headers: dict = None) -> requests.Response:
        """
        Makes an HTTP GET Request to the specified `request_url` and returns the response.

        :param request_url: the URL for the GET request.
        :param params: the URL parameters for the request.
        :param headers: the headers to set in the request.

        :return: the retrieved response.
        """
        logger.debug("HTTP GET Request to {}".format(request_url))
        try:
            response = requests.get(request_url, params=params, headers=self.__get_headers() if headers is None else headers)
            logger.debug("Response (HTTP Status Code: {}): {}".format(response.status_code, response.content))
            return response
        except requests.exceptions.RequestException as err:
            logger.error("Error upon HTTP Request: {}".format(err))
            raise SystemExit(1)

    def __get_headers(self, accept_data: str = "application/json") -> CaseInsensitiveDict:
        """
        Returns the basic necessary headers needed for querying the Deutsche Bahn APIs.

        :param accept_data: the accepted type of data to set as the Accept Header. Assumes application/json per default.

        :return: a dictionary containing the headers.
        """
        headers = CaseInsensitiveDict()
        headers["Accept"] = accept_data
        headers["Authorization"] = "Bearer {}".format(os.environ["DB_API_KEY"])
        return headers

