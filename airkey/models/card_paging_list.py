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

class CardPagingList(object):
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
        'medium_list': 'list[Card]'
    }

    attribute_map = {
        'offset': 'offset',
        'total': 'total',
        'medium_list': 'mediumList'
    }

    def __init__(self, offset=None, total=None, medium_list=None):  # noqa: E501
        """CardPagingList - a model defined in Swagger"""  # noqa: E501
        self._offset = None
        self._total = None
        self._medium_list = None
        self.discriminator = None
        if offset is not None:
            self.offset = offset
        if total is not None:
            self.total = total
        if medium_list is not None:
            self.medium_list = medium_list

    @property
    def offset(self):
        """Gets the offset of this CardPagingList.  # noqa: E501

        Offset for paging  # noqa: E501

        :return: The offset of this CardPagingList.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this CardPagingList.

        Offset for paging  # noqa: E501

        :param offset: The offset of this CardPagingList.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def total(self):
        """Gets the total of this CardPagingList.  # noqa: E501

        Total size of result set  # noqa: E501

        :return: The total of this CardPagingList.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CardPagingList.

        Total size of result set  # noqa: E501

        :param total: The total of this CardPagingList.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def medium_list(self):
        """Gets the medium_list of this CardPagingList.  # noqa: E501

        List of cards  # noqa: E501

        :return: The medium_list of this CardPagingList.  # noqa: E501
        :rtype: list[Card]
        """
        return self._medium_list

    @medium_list.setter
    def medium_list(self, medium_list):
        """Sets the medium_list of this CardPagingList.

        List of cards  # noqa: E501

        :param medium_list: The medium_list of this CardPagingList.  # noqa: E501
        :type: list[Card]
        """

        self._medium_list = medium_list

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
        if issubclass(CardPagingList, dict):
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
        if not isinstance(other, CardPagingList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
