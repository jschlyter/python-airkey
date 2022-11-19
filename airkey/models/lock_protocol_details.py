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

class LockProtocolDetails(object):
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
        'fields': 'JsonNode',
        'translations': 'dict(str, str)'
    }

    attribute_map = {
        'fields': 'fields',
        'translations': 'translations'
    }

    def __init__(self, fields=None, translations=None):  # noqa: E501
        """LockProtocolDetails - a model defined in Swagger"""  # noqa: E501
        self._fields = None
        self._translations = None
        self.discriminator = None
        if fields is not None:
            self.fields = fields
        if translations is not None:
            self.translations = translations

    @property
    def fields(self):
        """Gets the fields of this LockProtocolDetails.  # noqa: E501


        :return: The fields of this LockProtocolDetails.  # noqa: E501
        :rtype: JsonNode
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this LockProtocolDetails.


        :param fields: The fields of this LockProtocolDetails.  # noqa: E501
        :type: JsonNode
        """

        self._fields = fields

    @property
    def translations(self):
        """Gets the translations of this LockProtocolDetails.  # noqa: E501

        Event details translations comprising all requested languages (default only \"de-DE\")  # noqa: E501

        :return: The translations of this LockProtocolDetails.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._translations

    @translations.setter
    def translations(self, translations):
        """Sets the translations of this LockProtocolDetails.

        Event details translations comprising all requested languages (default only \"de-DE\")  # noqa: E501

        :param translations: The translations of this LockProtocolDetails.  # noqa: E501
        :type: dict(str, str)
        """

        self._translations = translations

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
        if issubclass(LockProtocolDetails, dict):
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
        if not isinstance(other, LockProtocolDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
