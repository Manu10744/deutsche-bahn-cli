from datetime import datetime


def parse_datetime(datetime_string):
    """
    Converts the datetime string from the TimeTable API into a `datetime`.


    :param datetime_string: the string representing the datetime of arrival / departure in the format of
                            YYMMDDhhmm which is used by the TimeTable API.

                            Example: '202201011322' for 2022-01-01 13:22
    :return: the obtained `datetime`.
    :rtype: datetime
    """
    datetime_format = '%y%m%d%H%M'
    return datetime.strptime(datetime_string, datetime_format)
