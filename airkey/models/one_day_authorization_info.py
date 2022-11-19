# coding: utf-8

"""
    EVVA AirKey Cloud API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v16.20.7
    Contact: office-wien@evva.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from airkey.models.authorization_info import AuthorizationInfo  # noqa: F401,E501

class OneDayAuthorizationInfo(AuthorizationInfo):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'valid_at_date': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }
    if hasattr(AuthorizationInfo, "swagger_types"):
        swagger_types.update(AuthorizationInfo.swagger_types)

    attribute_map = {
        'type': 'type',
        'valid_at_date': 'validAtDate',
        'start_time': 'startTime',
        'end_time': 'endTime'
    }
    if hasattr(AuthorizationInfo, "attribute_map"):
        attribute_map.update(AuthorizationInfo.attribute_map)

    def __init__(self, type=None, valid_at_date=None, start_time=None, end_time=None, *args, **kwargs):  # noqa: E501
        """OneDayAuthorizationInfo - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._valid_at_date = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None
        self.type = type
        self.valid_at_date = valid_at_date
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        AuthorizationInfo.__init__(self, *args, **kwargs)

    @property
    def type(self):
        """Gets the type of this OneDayAuthorizationInfo.  # noqa: E501

        One day type of authorization  # noqa: E501

        :return: The type of this OneDayAuthorizationInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneDayAuthorizationInfo.

        One day type of authorization  # noqa: E501

        :param type: The type of this OneDayAuthorizationInfo.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["ONE_DAY"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def valid_at_date(self):
        """Gets the valid_at_date of this OneDayAuthorizationInfo.  # noqa: E501

        Date when the authorization is valid regardless of the time zone (ISO 8601-format compliant date without time zone: yyyy-mm-dd)  # noqa: E501

        :return: The valid_at_date of this OneDayAuthorizationInfo.  # noqa: E501
        :rtype: str
        """
        return self._valid_at_date

    @valid_at_date.setter
    def valid_at_date(self, valid_at_date):
        """Sets the valid_at_date of this OneDayAuthorizationInfo.

        Date when the authorization is valid regardless of the time zone (ISO 8601-format compliant date without time zone: yyyy-mm-dd)  # noqa: E501

        :param valid_at_date: The valid_at_date of this OneDayAuthorizationInfo.  # noqa: E501
        :type: str
        """
        if valid_at_date is None:
            raise ValueError("Invalid value for `valid_at_date`, must not be `None`")  # noqa: E501

        self._valid_at_date = valid_at_date

    @property
    def start_time(self):
        """Gets the start_time of this OneDayAuthorizationInfo.  # noqa: E501

        Starting time on the day specified by validAtDate, not necessary when the authorization should be valid for the whole day (format: hh:mm)  # noqa: E501

        :return: The start_time of this OneDayAuthorizationInfo.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this OneDayAuthorizationInfo.

        Starting time on the day specified by validAtDate, not necessary when the authorization should be valid for the whole day (format: hh:mm)  # noqa: E501

        :param start_time: The start_time of this OneDayAuthorizationInfo.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this OneDayAuthorizationInfo.  # noqa: E501

        Ending time on the day specified by validAtDate, max value: 24:00, not necessary when authorization should be valid for the whole day (format: hh:mm)  # noqa: E501

        :return: The end_time of this OneDayAuthorizationInfo.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this OneDayAuthorizationInfo.

        Ending time on the day specified by validAtDate, max value: 24:00, not necessary when authorization should be valid for the whole day (format: hh:mm)  # noqa: E501

        :param end_time: The end_time of this OneDayAuthorizationInfo.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(OneDayAuthorizationInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OneDayAuthorizationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
