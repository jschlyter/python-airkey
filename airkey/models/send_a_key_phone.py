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

class SendAKeyPhone(object):
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
        'phone_number': 'str',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'phone_number': 'phoneNumber',
        'name': 'name'
    }

    def __init__(self, id=None, phone_number=None, name=None):  # noqa: E501
        """SendAKeyPhone - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._phone_number = None
        self._name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if phone_number is not None:
            self.phone_number = phone_number
        if name is not None:
            self.name = name

    @property
    def id(self):
        """Gets the id of this SendAKeyPhone.  # noqa: E501

        Unique id of the phone for using an existing one  # noqa: E501

        :return: The id of this SendAKeyPhone.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SendAKeyPhone.

        Unique id of the phone for using an existing one  # noqa: E501

        :param id: The id of this SendAKeyPhone.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def phone_number(self):
        """Gets the phone_number of this SendAKeyPhone.  # noqa: E501

        Phone number of the phone to be created starting with '+' followed by 1-49 digits (incl. possible spaces), e.g. +436641234567)  # noqa: E501

        :return: The phone_number of this SendAKeyPhone.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this SendAKeyPhone.

        Phone number of the phone to be created starting with '+' followed by 1-49 digits (incl. possible spaces), e.g. +436641234567)  # noqa: E501

        :param phone_number: The phone_number of this SendAKeyPhone.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def name(self):
        """Gets the name of this SendAKeyPhone.  # noqa: E501

        Name of the phone to be created (max. 50 characters)  # noqa: E501

        :return: The name of this SendAKeyPhone.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SendAKeyPhone.

        Name of the phone to be created (max. 50 characters)  # noqa: E501

        :param name: The name of this SendAKeyPhone.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(SendAKeyPhone, dict):
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
        if not isinstance(other, SendAKeyPhone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
