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

class SimpleMedium(object):
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
        'name': 'str',
        'medium_identifier': 'str',
        'medium_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'medium_identifier': 'mediumIdentifier',
        'medium_type': 'mediumType'
    }

    def __init__(self, id=None, name=None, medium_identifier=None, medium_type=None):  # noqa: E501
        """SimpleMedium - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._medium_identifier = None
        self._medium_type = None
        self.discriminator = None
        self.id = id
        if name is not None:
            self.name = name
        if medium_identifier is not None:
            self.medium_identifier = medium_identifier
        if medium_type is not None:
            self.medium_type = medium_type

    @property
    def id(self):
        """Gets the id of this SimpleMedium.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The id of this SimpleMedium.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SimpleMedium.

        Unique identifier  # noqa: E501

        :param id: The id of this SimpleMedium.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this SimpleMedium.  # noqa: E501

        Name of the medium  # noqa: E501

        :return: The name of this SimpleMedium.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SimpleMedium.

        Name of the medium  # noqa: E501

        :param name: The name of this SimpleMedium.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def medium_identifier(self):
        """Gets the medium_identifier of this SimpleMedium.  # noqa: E501

        Medium identifier  # noqa: E501

        :return: The medium_identifier of this SimpleMedium.  # noqa: E501
        :rtype: str
        """
        return self._medium_identifier

    @medium_identifier.setter
    def medium_identifier(self, medium_identifier):
        """Sets the medium_identifier of this SimpleMedium.

        Medium identifier  # noqa: E501

        :param medium_identifier: The medium_identifier of this SimpleMedium.  # noqa: E501
        :type: str
        """

        self._medium_identifier = medium_identifier

    @property
    def medium_type(self):
        """Gets the medium_type of this SimpleMedium.  # noqa: E501

        Type of medium  # noqa: E501

        :return: The medium_type of this SimpleMedium.  # noqa: E501
        :rtype: str
        """
        return self._medium_type

    @medium_type.setter
    def medium_type(self, medium_type):
        """Sets the medium_type of this SimpleMedium.

        Type of medium  # noqa: E501

        :param medium_type: The medium_type of this SimpleMedium.  # noqa: E501
        :type: str
        """
        allowed_values = ["PHONE", "CARD"]  # noqa: E501
        if medium_type not in allowed_values:
            raise ValueError(
                "Invalid value for `medium_type` ({0}), must be one of {1}"  # noqa: E501
                .format(medium_type, allowed_values)
            )

        self._medium_type = medium_type

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
        if issubclass(SimpleMedium, dict):
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
        if not isinstance(other, SimpleMedium):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
