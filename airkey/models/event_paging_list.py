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

class EventPagingList(object):
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
        'offset': 'int',
        'total': 'int',
        'events': 'list[Event]'
    }

    attribute_map = {
        'offset': 'offset',
        'total': 'total',
        'events': 'events'
    }

    def __init__(self, offset=None, total=None, events=None):  # noqa: E501
        """EventPagingList - a model defined in Swagger"""  # noqa: E501
        self._offset = None
        self._total = None
        self._events = None
        self.discriminator = None
        if offset is not None:
            self.offset = offset
        if total is not None:
            self.total = total
        if events is not None:
            self.events = events

    @property
    def offset(self):
        """Gets the offset of this EventPagingList.  # noqa: E501

        Offset for paging  # noqa: E501

        :return: The offset of this EventPagingList.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this EventPagingList.

        Offset for paging  # noqa: E501

        :param offset: The offset of this EventPagingList.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def total(self):
        """Gets the total of this EventPagingList.  # noqa: E501

        Total size of result set  # noqa: E501

        :return: The total of this EventPagingList.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this EventPagingList.

        Total size of result set  # noqa: E501

        :param total: The total of this EventPagingList.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def events(self):
        """Gets the events of this EventPagingList.  # noqa: E501

        List of events  # noqa: E501

        :return: The events of this EventPagingList.  # noqa: E501
        :rtype: list[Event]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this EventPagingList.

        List of events  # noqa: E501

        :param events: The events of this EventPagingList.  # noqa: E501
        :type: list[Event]
        """

        self._events = events

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
        if issubclass(EventPagingList, dict):
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
        if not isinstance(other, EventPagingList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
