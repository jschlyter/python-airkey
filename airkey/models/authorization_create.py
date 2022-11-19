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

class AuthorizationCreate(object):
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
        'medium_id': 'int',
        'area_id': 'int',
        'lock_id': 'int',
        'authorization_info_list': 'list[AuthorizationInfo]'
    }

    attribute_map = {
        'medium_id': 'mediumId',
        'area_id': 'areaId',
        'lock_id': 'lockId',
        'authorization_info_list': 'authorizationInfoList'
    }

    def __init__(self, medium_id=None, area_id=None, lock_id=None, authorization_info_list=None):  # noqa: E501
        """AuthorizationCreate - a model defined in Swagger"""  # noqa: E501
        self._medium_id = None
        self._area_id = None
        self._lock_id = None
        self._authorization_info_list = None
        self.discriminator = None
        self.medium_id = medium_id
        if area_id is not None:
            self.area_id = area_id
        if lock_id is not None:
            self.lock_id = lock_id
        self.authorization_info_list = authorization_info_list

    @property
    def medium_id(self):
        """Gets the medium_id of this AuthorizationCreate.  # noqa: E501

        Medium to which this authorization should be defined  # noqa: E501

        :return: The medium_id of this AuthorizationCreate.  # noqa: E501
        :rtype: int
        """
        return self._medium_id

    @medium_id.setter
    def medium_id(self, medium_id):
        """Sets the medium_id of this AuthorizationCreate.

        Medium to which this authorization should be defined  # noqa: E501

        :param medium_id: The medium_id of this AuthorizationCreate.  # noqa: E501
        :type: int
        """
        if medium_id is None:
            raise ValueError("Invalid value for `medium_id`, must not be `None`")  # noqa: E501

        self._medium_id = medium_id

    @property
    def area_id(self):
        """Gets the area_id of this AuthorizationCreate.  # noqa: E501

        Area for which the given medium should be authorized. Required when no lock id is set.  # noqa: E501

        :return: The area_id of this AuthorizationCreate.  # noqa: E501
        :rtype: int
        """
        return self._area_id

    @area_id.setter
    def area_id(self, area_id):
        """Sets the area_id of this AuthorizationCreate.

        Area for which the given medium should be authorized. Required when no lock id is set.  # noqa: E501

        :param area_id: The area_id of this AuthorizationCreate.  # noqa: E501
        :type: int
        """

        self._area_id = area_id

    @property
    def lock_id(self):
        """Gets the lock_id of this AuthorizationCreate.  # noqa: E501

        Lock for which the given medium should be authorized. Required when no area id is set.  # noqa: E501

        :return: The lock_id of this AuthorizationCreate.  # noqa: E501
        :rtype: int
        """
        return self._lock_id

    @lock_id.setter
    def lock_id(self, lock_id):
        """Sets the lock_id of this AuthorizationCreate.

        Lock for which the given medium should be authorized. Required when no area id is set.  # noqa: E501

        :param lock_id: The lock_id of this AuthorizationCreate.  # noqa: E501
        :type: int
        """

        self._lock_id = lock_id

    @property
    def authorization_info_list(self):
        """Gets the authorization_info_list of this AuthorizationCreate.  # noqa: E501

        List of authorization details  # noqa: E501

        :return: The authorization_info_list of this AuthorizationCreate.  # noqa: E501
        :rtype: list[AuthorizationInfo]
        """
        return self._authorization_info_list

    @authorization_info_list.setter
    def authorization_info_list(self, authorization_info_list):
        """Sets the authorization_info_list of this AuthorizationCreate.

        List of authorization details  # noqa: E501

        :param authorization_info_list: The authorization_info_list of this AuthorizationCreate.  # noqa: E501
        :type: list[AuthorizationInfo]
        """
        if authorization_info_list is None:
            raise ValueError("Invalid value for `authorization_info_list`, must not be `None`")  # noqa: E501

        self._authorization_info_list = authorization_info_list

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
        if issubclass(AuthorizationCreate, dict):
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
        if not isinstance(other, AuthorizationCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
