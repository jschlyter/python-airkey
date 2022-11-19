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
from airkey.models.event_details import EventDetails  # noqa: F401,E501

class UnlockingEventDetails(EventDetails):
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
        'unlocking_timestamp': 'str'
    }
    if hasattr(EventDetails, "swagger_types"):
        swagger_types.update(EventDetails.swagger_types)

    attribute_map = {
        'lock_id': 'lockId',
        'medium_id': 'mediumId',
        'unlocking_timestamp': 'unlockingTimestamp'
    }
    if hasattr(EventDetails, "attribute_map"):
        attribute_map.update(EventDetails.attribute_map)

    def __init__(self, lock_id=None, medium_id=None, unlocking_timestamp=None, *args, **kwargs):  # noqa: E501
        """UnlockingEventDetails - a model defined in Swagger"""  # noqa: E501
        self._lock_id = None
        self._medium_id = None
        self._unlocking_timestamp = None
        self.discriminator = None
        if lock_id is not None:
            self.lock_id = lock_id
        if medium_id is not None:
            self.medium_id = medium_id
        if unlocking_timestamp is not None:
            self.unlocking_timestamp = unlocking_timestamp
        EventDetails.__init__(self, *args, **kwargs)

    @property
    def lock_id(self):
        """Gets the lock_id of this UnlockingEventDetails.  # noqa: E501

        Unique identifier of the unlocked locking component  # noqa: E501

        :return: The lock_id of this UnlockingEventDetails.  # noqa: E501
        :rtype: int
        """
        return self._lock_id

    @lock_id.setter
    def lock_id(self, lock_id):
        """Sets the lock_id of this UnlockingEventDetails.

        Unique identifier of the unlocked locking component  # noqa: E501

        :param lock_id: The lock_id of this UnlockingEventDetails.  # noqa: E501
        :type: int
        """

        self._lock_id = lock_id

    @property
    def medium_id(self):
        """Gets the medium_id of this UnlockingEventDetails.  # noqa: E501

        Unique identifier of the medium which was used to unlock the locking component. Not set for anonymized events.  # noqa: E501

        :return: The medium_id of this UnlockingEventDetails.  # noqa: E501
        :rtype: int
        """
        return self._medium_id

    @medium_id.setter
    def medium_id(self, medium_id):
        """Sets the medium_id of this UnlockingEventDetails.

        Unique identifier of the medium which was used to unlock the locking component. Not set for anonymized events.  # noqa: E501

        :param medium_id: The medium_id of this UnlockingEventDetails.  # noqa: E501
        :type: int
        """

        self._medium_id = medium_id

    @property
    def unlocking_timestamp(self):
        """Gets the unlocking_timestamp of this UnlockingEventDetails.  # noqa: E501

        Unlocking timestamp, usually different than the event (server) timestamp (ISO 8601-format compliant date with time in UTC, milliseconds precision)  # noqa: E501

        :return: The unlocking_timestamp of this UnlockingEventDetails.  # noqa: E501
        :rtype: str
        """
        return self._unlocking_timestamp

    @unlocking_timestamp.setter
    def unlocking_timestamp(self, unlocking_timestamp):
        """Sets the unlocking_timestamp of this UnlockingEventDetails.

        Unlocking timestamp, usually different than the event (server) timestamp (ISO 8601-format compliant date with time in UTC, milliseconds precision)  # noqa: E501

        :param unlocking_timestamp: The unlocking_timestamp of this UnlockingEventDetails.  # noqa: E501
        :type: str
        """

        self._unlocking_timestamp = unlocking_timestamp

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
        if issubclass(UnlockingEventDetails, dict):
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
        if not isinstance(other, UnlockingEventDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
