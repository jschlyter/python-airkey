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

class HolidayCalendarSeriesCreate(object):
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
        'repetition_type': 'str',
        'ends_after': 'int',
        'ends_on': 'str'
    }

    attribute_map = {
        'repetition_type': 'repetitionType',
        'ends_after': 'endsAfter',
        'ends_on': 'endsOn'
    }

    def __init__(self, repetition_type=None, ends_after=None, ends_on=None):  # noqa: E501
        """HolidayCalendarSeriesCreate - a model defined in Swagger"""  # noqa: E501
        self._repetition_type = None
        self._ends_after = None
        self._ends_on = None
        self.discriminator = None
        self.repetition_type = repetition_type
        if ends_after is not None:
            self.ends_after = ends_after
        if ends_on is not None:
            self.ends_on = ends_on

    @property
    def repetition_type(self):
        """Gets the repetition_type of this HolidayCalendarSeriesCreate.  # noqa: E501

        Type of the repetition  # noqa: E501

        :return: The repetition_type of this HolidayCalendarSeriesCreate.  # noqa: E501
        :rtype: str
        """
        return self._repetition_type

    @repetition_type.setter
    def repetition_type(self, repetition_type):
        """Sets the repetition_type of this HolidayCalendarSeriesCreate.

        Type of the repetition  # noqa: E501

        :param repetition_type: The repetition_type of this HolidayCalendarSeriesCreate.  # noqa: E501
        :type: str
        """
        if repetition_type is None:
            raise ValueError("Invalid value for `repetition_type`, must not be `None`")  # noqa: E501
        allowed_values = ["DAILY", "WEEKLY", "MONTHLY", "MONTHLY_SPECIFIC_WEEK_DAY", "YEARLY"]  # noqa: E501
        if repetition_type not in allowed_values:
            raise ValueError(
                "Invalid value for `repetition_type` ({0}), must be one of {1}"  # noqa: E501
                .format(repetition_type, allowed_values)
            )

        self._repetition_type = repetition_type

    @property
    def ends_after(self):
        """Gets the ends_after of this HolidayCalendarSeriesCreate.  # noqa: E501

        Number of repetitions  # noqa: E501

        :return: The ends_after of this HolidayCalendarSeriesCreate.  # noqa: E501
        :rtype: int
        """
        return self._ends_after

    @ends_after.setter
    def ends_after(self, ends_after):
        """Sets the ends_after of this HolidayCalendarSeriesCreate.

        Number of repetitions  # noqa: E501

        :param ends_after: The ends_after of this HolidayCalendarSeriesCreate.  # noqa: E501
        :type: int
        """

        self._ends_after = ends_after

    @property
    def ends_on(self):
        """Gets the ends_on of this HolidayCalendarSeriesCreate.  # noqa: E501

        Day until when the series is valid (ISO 8601-format compliant date without time zone: yyyy-mm-dd)  # noqa: E501

        :return: The ends_on of this HolidayCalendarSeriesCreate.  # noqa: E501
        :rtype: str
        """
        return self._ends_on

    @ends_on.setter
    def ends_on(self, ends_on):
        """Sets the ends_on of this HolidayCalendarSeriesCreate.

        Day until when the series is valid (ISO 8601-format compliant date without time zone: yyyy-mm-dd)  # noqa: E501

        :param ends_on: The ends_on of this HolidayCalendarSeriesCreate.  # noqa: E501
        :type: str
        """

        self._ends_on = ends_on

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
        if issubclass(HolidayCalendarSeriesCreate, dict):
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
        if not isinstance(other, HolidayCalendarSeriesCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
