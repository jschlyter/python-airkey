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

class HolidayCalendarSlotCreate(object):
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
        'slot_name': 'str',
        'valid_from': 'str',
        'valid_to': 'str',
        'series': 'HolidayCalendarSeriesCreate'
    }

    attribute_map = {
        'slot_name': 'slotName',
        'valid_from': 'validFrom',
        'valid_to': 'validTo',
        'series': 'series'
    }

    def __init__(self, slot_name=None, valid_from=None, valid_to=None, series=None):  # noqa: E501
        """HolidayCalendarSlotCreate - a model defined in Swagger"""  # noqa: E501
        self._slot_name = None
        self._valid_from = None
        self._valid_to = None
        self._series = None
        self.discriminator = None
        self.slot_name = slot_name
        self.valid_from = valid_from
        self.valid_to = valid_to
        if series is not None:
            self.series = series

    @property
    def slot_name(self):
        """Gets the slot_name of this HolidayCalendarSlotCreate.  # noqa: E501

        Name of the holiday calendar slot (max. 50 characters)  # noqa: E501

        :return: The slot_name of this HolidayCalendarSlotCreate.  # noqa: E501
        :rtype: str
        """
        return self._slot_name

    @slot_name.setter
    def slot_name(self, slot_name):
        """Sets the slot_name of this HolidayCalendarSlotCreate.

        Name of the holiday calendar slot (max. 50 characters)  # noqa: E501

        :param slot_name: The slot_name of this HolidayCalendarSlotCreate.  # noqa: E501
        :type: str
        """
        if slot_name is None:
            raise ValueError("Invalid value for `slot_name`, must not be `None`")  # noqa: E501

        self._slot_name = slot_name

    @property
    def valid_from(self):
        """Gets the valid_from of this HolidayCalendarSlotCreate.  # noqa: E501

        Holiday calendar slot start time regardless of the time zone (ISO 8601-format compliant date with time, without time zone: yyyy-mm-ddThh:mm)  # noqa: E501

        :return: The valid_from of this HolidayCalendarSlotCreate.  # noqa: E501
        :rtype: str
        """
        return self._valid_from

    @valid_from.setter
    def valid_from(self, valid_from):
        """Sets the valid_from of this HolidayCalendarSlotCreate.

        Holiday calendar slot start time regardless of the time zone (ISO 8601-format compliant date with time, without time zone: yyyy-mm-ddThh:mm)  # noqa: E501

        :param valid_from: The valid_from of this HolidayCalendarSlotCreate.  # noqa: E501
        :type: str
        """
        if valid_from is None:
            raise ValueError("Invalid value for `valid_from`, must not be `None`")  # noqa: E501

        self._valid_from = valid_from

    @property
    def valid_to(self):
        """Gets the valid_to of this HolidayCalendarSlotCreate.  # noqa: E501

        Holiday calendar slot end time regardless of the time zone (ISO 8601-format compliant date with time, without time zone: yyyy-mm-ddThh:mm)  # noqa: E501

        :return: The valid_to of this HolidayCalendarSlotCreate.  # noqa: E501
        :rtype: str
        """
        return self._valid_to

    @valid_to.setter
    def valid_to(self, valid_to):
        """Sets the valid_to of this HolidayCalendarSlotCreate.

        Holiday calendar slot end time regardless of the time zone (ISO 8601-format compliant date with time, without time zone: yyyy-mm-ddThh:mm)  # noqa: E501

        :param valid_to: The valid_to of this HolidayCalendarSlotCreate.  # noqa: E501
        :type: str
        """
        if valid_to is None:
            raise ValueError("Invalid value for `valid_to`, must not be `None`")  # noqa: E501

        self._valid_to = valid_to

    @property
    def series(self):
        """Gets the series of this HolidayCalendarSlotCreate.  # noqa: E501


        :return: The series of this HolidayCalendarSlotCreate.  # noqa: E501
        :rtype: HolidayCalendarSeriesCreate
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this HolidayCalendarSlotCreate.


        :param series: The series of this HolidayCalendarSlotCreate.  # noqa: E501
        :type: HolidayCalendarSeriesCreate
        """

        self._series = series

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
        if issubclass(HolidayCalendarSlotCreate, dict):
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
        if not isinstance(other, HolidayCalendarSlotCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other