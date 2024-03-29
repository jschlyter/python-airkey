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

class HolidayCalendar(object):
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
        'id': 'int',
        'version': 'int',
        'active': 'bool',
        'holiday_calendar_slots': 'list[HolidayCalendarSlot]'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'active': 'active',
        'holiday_calendar_slots': 'holidayCalendarSlots'
    }

    def __init__(self, id=None, version=None, active=None, holiday_calendar_slots=None):  # noqa: E501
        """HolidayCalendar - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._version = None
        self._active = None
        self._holiday_calendar_slots = None
        self.discriminator = None
        self.id = id
        self.version = version
        self.active = active
        if holiday_calendar_slots is not None:
            self.holiday_calendar_slots = holiday_calendar_slots

    @property
    def id(self):
        """Gets the id of this HolidayCalendar.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The id of this HolidayCalendar.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HolidayCalendar.

        Unique identifier  # noqa: E501

        :param id: The id of this HolidayCalendar.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def version(self):
        """Gets the version of this HolidayCalendar.  # noqa: E501

        Current version number of the holiday calendar  # noqa: E501

        :return: The version of this HolidayCalendar.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this HolidayCalendar.

        Current version number of the holiday calendar  # noqa: E501

        :param version: The version of this HolidayCalendar.  # noqa: E501
        :type: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def active(self):
        """Gets the active of this HolidayCalendar.  # noqa: E501

        Is the holiday calendar currently active or not  # noqa: E501

        :return: The active of this HolidayCalendar.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this HolidayCalendar.

        Is the holiday calendar currently active or not  # noqa: E501

        :param active: The active of this HolidayCalendar.  # noqa: E501
        :type: bool
        """
        if active is None:
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        self._active = active

    @property
    def holiday_calendar_slots(self):
        """Gets the holiday_calendar_slots of this HolidayCalendar.  # noqa: E501

        List of holiday calendar slots defining the time of the holidays  # noqa: E501

        :return: The holiday_calendar_slots of this HolidayCalendar.  # noqa: E501
        :rtype: list[HolidayCalendarSlot]
        """
        return self._holiday_calendar_slots

    @holiday_calendar_slots.setter
    def holiday_calendar_slots(self, holiday_calendar_slots):
        """Sets the holiday_calendar_slots of this HolidayCalendar.

        List of holiday calendar slots defining the time of the holidays  # noqa: E501

        :param holiday_calendar_slots: The holiday_calendar_slots of this HolidayCalendar.  # noqa: E501
        :type: list[HolidayCalendarSlot]
        """

        self._holiday_calendar_slots = holiday_calendar_slots

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
        if issubclass(HolidayCalendar, dict):
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
        if not isinstance(other, HolidayCalendar):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
