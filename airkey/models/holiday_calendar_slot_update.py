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

class HolidayCalendarSlotUpdate(object):
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
        'slot_name': 'str',
        'valid_from': 'str',
        'valid_to': 'str',
        'series': 'HolidayCalendarSeries',
        'series_sequence_number': 'int',
        'modify_future_slots': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'slot_name': 'slotName',
        'valid_from': 'validFrom',
        'valid_to': 'validTo',
        'series': 'series',
        'series_sequence_number': 'seriesSequenceNumber',
        'modify_future_slots': 'modifyFutureSlots'
    }

    def __init__(self, id=None, version=None, slot_name=None, valid_from=None, valid_to=None, series=None, series_sequence_number=None, modify_future_slots=None):  # noqa: E501
        """HolidayCalendarSlotUpdate - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._version = None
        self._slot_name = None
        self._valid_from = None
        self._valid_to = None
        self._series = None
        self._series_sequence_number = None
        self._modify_future_slots = None
        self.discriminator = None
        self.id = id
        self.version = version
        self.slot_name = slot_name
        self.valid_from = valid_from
        self.valid_to = valid_to
        if series is not None:
            self.series = series
        if series_sequence_number is not None:
            self.series_sequence_number = series_sequence_number
        self.modify_future_slots = modify_future_slots

    @property
    def id(self):
        """Gets the id of this HolidayCalendarSlotUpdate.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The id of this HolidayCalendarSlotUpdate.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HolidayCalendarSlotUpdate.

        Unique identifier  # noqa: E501

        :param id: The id of this HolidayCalendarSlotUpdate.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def version(self):
        """Gets the version of this HolidayCalendarSlotUpdate.  # noqa: E501

        Current version number of the holiday calendar slot  # noqa: E501

        :return: The version of this HolidayCalendarSlotUpdate.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this HolidayCalendarSlotUpdate.

        Current version number of the holiday calendar slot  # noqa: E501

        :param version: The version of this HolidayCalendarSlotUpdate.  # noqa: E501
        :type: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def slot_name(self):
        """Gets the slot_name of this HolidayCalendarSlotUpdate.  # noqa: E501

        Name of the holiday calendar slot (max. 50 characters)  # noqa: E501

        :return: The slot_name of this HolidayCalendarSlotUpdate.  # noqa: E501
        :rtype: str
        """
        return self._slot_name

    @slot_name.setter
    def slot_name(self, slot_name):
        """Sets the slot_name of this HolidayCalendarSlotUpdate.

        Name of the holiday calendar slot (max. 50 characters)  # noqa: E501

        :param slot_name: The slot_name of this HolidayCalendarSlotUpdate.  # noqa: E501
        :type: str
        """
        if slot_name is None:
            raise ValueError("Invalid value for `slot_name`, must not be `None`")  # noqa: E501

        self._slot_name = slot_name

    @property
    def valid_from(self):
        """Gets the valid_from of this HolidayCalendarSlotUpdate.  # noqa: E501

        Holiday calendar slot start time regardless of the time zone (ISO 8601-format compliant date with time, without time zone: yyyy-mm-ddThh:mm)  # noqa: E501

        :return: The valid_from of this HolidayCalendarSlotUpdate.  # noqa: E501
        :rtype: str
        """
        return self._valid_from

    @valid_from.setter
    def valid_from(self, valid_from):
        """Sets the valid_from of this HolidayCalendarSlotUpdate.

        Holiday calendar slot start time regardless of the time zone (ISO 8601-format compliant date with time, without time zone: yyyy-mm-ddThh:mm)  # noqa: E501

        :param valid_from: The valid_from of this HolidayCalendarSlotUpdate.  # noqa: E501
        :type: str
        """
        if valid_from is None:
            raise ValueError("Invalid value for `valid_from`, must not be `None`")  # noqa: E501

        self._valid_from = valid_from

    @property
    def valid_to(self):
        """Gets the valid_to of this HolidayCalendarSlotUpdate.  # noqa: E501

        Holiday calendar slot end time regardless of the time zone (ISO 8601-format compliant date with time, without time zone: yyyy-mm-ddThh:mm)  # noqa: E501

        :return: The valid_to of this HolidayCalendarSlotUpdate.  # noqa: E501
        :rtype: str
        """
        return self._valid_to

    @valid_to.setter
    def valid_to(self, valid_to):
        """Sets the valid_to of this HolidayCalendarSlotUpdate.

        Holiday calendar slot end time regardless of the time zone (ISO 8601-format compliant date with time, without time zone: yyyy-mm-ddThh:mm)  # noqa: E501

        :param valid_to: The valid_to of this HolidayCalendarSlotUpdate.  # noqa: E501
        :type: str
        """
        if valid_to is None:
            raise ValueError("Invalid value for `valid_to`, must not be `None`")  # noqa: E501

        self._valid_to = valid_to

    @property
    def series(self):
        """Gets the series of this HolidayCalendarSlotUpdate.  # noqa: E501


        :return: The series of this HolidayCalendarSlotUpdate.  # noqa: E501
        :rtype: HolidayCalendarSeries
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this HolidayCalendarSlotUpdate.


        :param series: The series of this HolidayCalendarSlotUpdate.  # noqa: E501
        :type: HolidayCalendarSeries
        """

        self._series = series

    @property
    def series_sequence_number(self):
        """Gets the series_sequence_number of this HolidayCalendarSlotUpdate.  # noqa: E501

        Sequence number of this holiday calendar slot in the time series  # noqa: E501

        :return: The series_sequence_number of this HolidayCalendarSlotUpdate.  # noqa: E501
        :rtype: int
        """
        return self._series_sequence_number

    @series_sequence_number.setter
    def series_sequence_number(self, series_sequence_number):
        """Sets the series_sequence_number of this HolidayCalendarSlotUpdate.

        Sequence number of this holiday calendar slot in the time series  # noqa: E501

        :param series_sequence_number: The series_sequence_number of this HolidayCalendarSlotUpdate.  # noqa: E501
        :type: int
        """

        self._series_sequence_number = series_sequence_number

    @property
    def modify_future_slots(self):
        """Gets the modify_future_slots of this HolidayCalendarSlotUpdate.  # noqa: E501

        Updating this holiday calendar slot only or also all future slots in the series  # noqa: E501

        :return: The modify_future_slots of this HolidayCalendarSlotUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._modify_future_slots

    @modify_future_slots.setter
    def modify_future_slots(self, modify_future_slots):
        """Sets the modify_future_slots of this HolidayCalendarSlotUpdate.

        Updating this holiday calendar slot only or also all future slots in the series  # noqa: E501

        :param modify_future_slots: The modify_future_slots of this HolidayCalendarSlotUpdate.  # noqa: E501
        :type: bool
        """
        if modify_future_slots is None:
            raise ValueError("Invalid value for `modify_future_slots`, must not be `None`")  # noqa: E501

        self._modify_future_slots = modify_future_slots

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
        if issubclass(HolidayCalendarSlotUpdate, dict):
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
        if not isinstance(other, HolidayCalendarSlotUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other