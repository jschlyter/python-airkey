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

class BlacklistEntry(object):
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
        'lock_id': 'int',
        'medium_id': 'int',
        'synchronized_on_lock': 'bool'
    }

    attribute_map = {
        'lock_id': 'lockId',
        'medium_id': 'mediumId',
        'synchronized_on_lock': 'synchronizedOnLock'
    }

    def __init__(self, lock_id=None, medium_id=None, synchronized_on_lock=None):  # noqa: E501
        """BlacklistEntry - a model defined in Swagger"""  # noqa: E501
        self._lock_id = None
        self._medium_id = None
        self._synchronized_on_lock = None
        self.discriminator = None
        if lock_id is not None:
            self.lock_id = lock_id
        if medium_id is not None:
            self.medium_id = medium_id
        if synchronized_on_lock is not None:
            self.synchronized_on_lock = synchronized_on_lock

    @property
    def lock_id(self):
        """Gets the lock_id of this BlacklistEntry.  # noqa: E501

        Lock for which the medium was added to the blacklist  # noqa: E501

        :return: The lock_id of this BlacklistEntry.  # noqa: E501
        :rtype: int
        """
        return self._lock_id

    @lock_id.setter
    def lock_id(self, lock_id):
        """Sets the lock_id of this BlacklistEntry.

        Lock for which the medium was added to the blacklist  # noqa: E501

        :param lock_id: The lock_id of this BlacklistEntry.  # noqa: E501
        :type: int
        """

        self._lock_id = lock_id

    @property
    def medium_id(self):
        """Gets the medium_id of this BlacklistEntry.  # noqa: E501

        Medium which was added to the blacklist  # noqa: E501

        :return: The medium_id of this BlacklistEntry.  # noqa: E501
        :rtype: int
        """
        return self._medium_id

    @medium_id.setter
    def medium_id(self, medium_id):
        """Sets the medium_id of this BlacklistEntry.

        Medium which was added to the blacklist  # noqa: E501

        :param medium_id: The medium_id of this BlacklistEntry.  # noqa: E501
        :type: int
        """

        self._medium_id = medium_id

    @property
    def synchronized_on_lock(self):
        """Gets the synchronized_on_lock of this BlacklistEntry.  # noqa: E501

        Signals if the lock needs to be synchronized to consider this blacklist entry appropriately  # noqa: E501

        :return: The synchronized_on_lock of this BlacklistEntry.  # noqa: E501
        :rtype: bool
        """
        return self._synchronized_on_lock

    @synchronized_on_lock.setter
    def synchronized_on_lock(self, synchronized_on_lock):
        """Sets the synchronized_on_lock of this BlacklistEntry.

        Signals if the lock needs to be synchronized to consider this blacklist entry appropriately  # noqa: E501

        :param synchronized_on_lock: The synchronized_on_lock of this BlacklistEntry.  # noqa: E501
        :type: bool
        """

        self._synchronized_on_lock = synchronized_on_lock

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
        if issubclass(BlacklistEntry, dict):
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
        if not isinstance(other, BlacklistEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
