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

class PeriodicalAuthorizationInfo(AuthorizationInfo):
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
        'periodical_periods': 'list[PeriodicalPeriod]',
        'valid_from_date': 'str',
        'valid_to_date': 'str'
    }
    if hasattr(AuthorizationInfo, "swagger_types"):
        swagger_types.update(AuthorizationInfo.swagger_types)

    attribute_map = {
        'type': 'type',
        'periodical_periods': 'periodicalPeriods',
        'valid_from_date': 'validFromDate',
        'valid_to_date': 'validToDate'
    }
    if hasattr(AuthorizationInfo, "attribute_map"):
        attribute_map.update(AuthorizationInfo.attribute_map)

    def __init__(self, type=None, periodical_periods=None, valid_from_date=None, valid_to_date=None, *args, **kwargs):  # noqa: E501
        """PeriodicalAuthorizationInfo - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._periodical_periods = None
        self._valid_from_date = None
        self._valid_to_date = None
        self.discriminator = None
        self.type = type
        self.periodical_periods = periodical_periods
        self.valid_from_date = valid_from_date
        if valid_to_date is not None:
            self.valid_to_date = valid_to_date
        AuthorizationInfo.__init__(self, *args, **kwargs)

    @property
    def type(self):
        """Gets the type of this PeriodicalAuthorizationInfo.  # noqa: E501

        Periodical type of authorization  # noqa: E501

        :return: The type of this PeriodicalAuthorizationInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PeriodicalAuthorizationInfo.

        Periodical type of authorization  # noqa: E501

        :param type: The type of this PeriodicalAuthorizationInfo.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["PERIODICAL"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def periodical_periods(self):
        """Gets the periodical_periods of this PeriodicalAuthorizationInfo.  # noqa: E501

        List of periodical periods in which the medium is authorized for a lock or area (max. 28 entries - 4 per week day)  # noqa: E501

        :return: The periodical_periods of this PeriodicalAuthorizationInfo.  # noqa: E501
        :rtype: list[PeriodicalPeriod]
        """
        return self._periodical_periods

    @periodical_periods.setter
    def periodical_periods(self, periodical_periods):
        """Sets the periodical_periods of this PeriodicalAuthorizationInfo.

        List of periodical periods in which the medium is authorized for a lock or area (max. 28 entries - 4 per week day)  # noqa: E501

        :param periodical_periods: The periodical_periods of this PeriodicalAuthorizationInfo.  # noqa: E501
        :type: list[PeriodicalPeriod]
        """
        if periodical_periods is None:
            raise ValueError("Invalid value for `periodical_periods`, must not be `None`")  # noqa: E501

        self._periodical_periods = periodical_periods

    @property
    def valid_from_date(self):
        """Gets the valid_from_date of this PeriodicalAuthorizationInfo.  # noqa: E501

        Date from when the authorization is valid regardless of the time zone (ISO 8601-format compliant date without time zone: yyyy-mm-dd)  # noqa: E501

        :return: The valid_from_date of this PeriodicalAuthorizationInfo.  # noqa: E501
        :rtype: str
        """
        return self._valid_from_date

    @valid_from_date.setter
    def valid_from_date(self, valid_from_date):
        """Sets the valid_from_date of this PeriodicalAuthorizationInfo.

        Date from when the authorization is valid regardless of the time zone (ISO 8601-format compliant date without time zone: yyyy-mm-dd)  # noqa: E501

        :param valid_from_date: The valid_from_date of this PeriodicalAuthorizationInfo.  # noqa: E501
        :type: str
        """
        if valid_from_date is None:
            raise ValueError("Invalid value for `valid_from_date`, must not be `None`")  # noqa: E501

        self._valid_from_date = valid_from_date

    @property
    def valid_to_date(self):
        """Gets the valid_to_date of this PeriodicalAuthorizationInfo.  # noqa: E501

        Date until when the authorization is valid regardless of the time zone, not necessary if there should be no limit (ISO 8601-format compliant date without time zone: yyyy-mm-dd)  # noqa: E501

        :return: The valid_to_date of this PeriodicalAuthorizationInfo.  # noqa: E501
        :rtype: str
        """
        return self._valid_to_date

    @valid_to_date.setter
    def valid_to_date(self, valid_to_date):
        """Sets the valid_to_date of this PeriodicalAuthorizationInfo.

        Date until when the authorization is valid regardless of the time zone, not necessary if there should be no limit (ISO 8601-format compliant date without time zone: yyyy-mm-dd)  # noqa: E501

        :param valid_to_date: The valid_to_date of this PeriodicalAuthorizationInfo.  # noqa: E501
        :type: str
        """

        self._valid_to_date = valid_to_date

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
        if issubclass(PeriodicalAuthorizationInfo, dict):
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
        if not isinstance(other, PeriodicalAuthorizationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other