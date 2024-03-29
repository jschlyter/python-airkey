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

class SimpleLock(object):
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
        'lock_type': 'str',
        'lock_identifier': 'str',
        'name': 'str',
        'additional_information': 'str'
    }

    attribute_map = {
        'id': 'id',
        'lock_type': 'lockType',
        'lock_identifier': 'lockIdentifier',
        'name': 'name',
        'additional_information': 'additionalInformation'
    }

    def __init__(self, id=None, lock_type=None, lock_identifier=None, name=None, additional_information=None):  # noqa: E501
        """SimpleLock - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._lock_type = None
        self._lock_identifier = None
        self._name = None
        self._additional_information = None
        self.discriminator = None
        self.id = id
        if lock_type is not None:
            self.lock_type = lock_type
        if lock_identifier is not None:
            self.lock_identifier = lock_identifier
        if name is not None:
            self.name = name
        if additional_information is not None:
            self.additional_information = additional_information

    @property
    def id(self):
        """Gets the id of this SimpleLock.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The id of this SimpleLock.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SimpleLock.

        Unique identifier  # noqa: E501

        :param id: The id of this SimpleLock.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def lock_type(self):
        """Gets the lock_type of this SimpleLock.  # noqa: E501

        Type of lock  # noqa: E501

        :return: The lock_type of this SimpleLock.  # noqa: E501
        :rtype: str
        """
        return self._lock_type

    @lock_type.setter
    def lock_type(self, lock_type):
        """Sets the lock_type of this SimpleLock.

        Type of lock  # noqa: E501

        :param lock_type: The lock_type of this SimpleLock.  # noqa: E501
        :type: str
        """
        allowed_values = ["CYLINDER", "WALLREADER"]  # noqa: E501
        if lock_type not in allowed_values:
            raise ValueError(
                "Invalid value for `lock_type` ({0}), must be one of {1}"  # noqa: E501
                .format(lock_type, allowed_values)
            )

        self._lock_type = lock_type

    @property
    def lock_identifier(self):
        """Gets the lock_identifier of this SimpleLock.  # noqa: E501

        Identifier of the lock  # noqa: E501

        :return: The lock_identifier of this SimpleLock.  # noqa: E501
        :rtype: str
        """
        return self._lock_identifier

    @lock_identifier.setter
    def lock_identifier(self, lock_identifier):
        """Sets the lock_identifier of this SimpleLock.

        Identifier of the lock  # noqa: E501

        :param lock_identifier: The lock_identifier of this SimpleLock.  # noqa: E501
        :type: str
        """

        self._lock_identifier = lock_identifier

    @property
    def name(self):
        """Gets the name of this SimpleLock.  # noqa: E501

        Name of the lock  # noqa: E501

        :return: The name of this SimpleLock.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SimpleLock.

        Name of the lock  # noqa: E501

        :param name: The name of this SimpleLock.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def additional_information(self):
        """Gets the additional_information of this SimpleLock.  # noqa: E501

        Additional information about the lock  # noqa: E501

        :return: The additional_information of this SimpleLock.  # noqa: E501
        :rtype: str
        """
        return self._additional_information

    @additional_information.setter
    def additional_information(self, additional_information):
        """Sets the additional_information of this SimpleLock.

        Additional information about the lock  # noqa: E501

        :param additional_information: The additional_information of this SimpleLock.  # noqa: E501
        :type: str
        """

        self._additional_information = additional_information

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
        if issubclass(SimpleLock, dict):
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
        if not isinstance(other, SimpleLock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
