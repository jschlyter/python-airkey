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

class SystemProtocolEntry(object):
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
        'event': 'SystemProtocolEvent',
        'details': 'SystemProtocolDetails',
        'timestamp': 'str',
        'lock_identifier': 'str',
        'lock_id': 'int',
        'medium_identifier': 'str',
        'medium_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'event': 'event',
        'details': 'details',
        'timestamp': 'timestamp',
        'lock_identifier': 'lockIdentifier',
        'lock_id': 'lockId',
        'medium_identifier': 'mediumIdentifier',
        'medium_id': 'mediumId'
    }

    def __init__(self, id=None, event=None, details=None, timestamp=None, lock_identifier=None, lock_id=None, medium_identifier=None, medium_id=None):  # noqa: E501
        """SystemProtocolEntry - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._event = None
        self._details = None
        self._timestamp = None
        self._lock_identifier = None
        self._lock_id = None
        self._medium_identifier = None
        self._medium_id = None
        self.discriminator = None
        self.id = id
        if event is not None:
            self.event = event
        if details is not None:
            self.details = details
        if timestamp is not None:
            self.timestamp = timestamp
        if lock_identifier is not None:
            self.lock_identifier = lock_identifier
        if lock_id is not None:
            self.lock_id = lock_id
        if medium_identifier is not None:
            self.medium_identifier = medium_identifier
        if medium_id is not None:
            self.medium_id = medium_id

    @property
    def id(self):
        """Gets the id of this SystemProtocolEntry.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The id of this SystemProtocolEntry.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SystemProtocolEntry.

        Unique identifier  # noqa: E501

        :param id: The id of this SystemProtocolEntry.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def event(self):
        """Gets the event of this SystemProtocolEntry.  # noqa: E501


        :return: The event of this SystemProtocolEntry.  # noqa: E501
        :rtype: SystemProtocolEvent
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this SystemProtocolEntry.


        :param event: The event of this SystemProtocolEntry.  # noqa: E501
        :type: SystemProtocolEvent
        """

        self._event = event

    @property
    def details(self):
        """Gets the details of this SystemProtocolEntry.  # noqa: E501


        :return: The details of this SystemProtocolEntry.  # noqa: E501
        :rtype: SystemProtocolDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this SystemProtocolEntry.


        :param details: The details of this SystemProtocolEntry.  # noqa: E501
        :type: SystemProtocolDetails
        """

        self._details = details

    @property
    def timestamp(self):
        """Gets the timestamp of this SystemProtocolEntry.  # noqa: E501

        Timestamp of the event (ISO 8601-format compliant date with time in UTC, milliseconds precision)  # noqa: E501

        :return: The timestamp of this SystemProtocolEntry.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this SystemProtocolEntry.

        Timestamp of the event (ISO 8601-format compliant date with time in UTC, milliseconds precision)  # noqa: E501

        :param timestamp: The timestamp of this SystemProtocolEntry.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

    @property
    def lock_identifier(self):
        """Gets the lock_identifier of this SystemProtocolEntry.  # noqa: E501

        Identifier of the locking component which was involved in the event, otherwise empty if no locking component was involved  # noqa: E501

        :return: The lock_identifier of this SystemProtocolEntry.  # noqa: E501
        :rtype: str
        """
        return self._lock_identifier

    @lock_identifier.setter
    def lock_identifier(self, lock_identifier):
        """Sets the lock_identifier of this SystemProtocolEntry.

        Identifier of the locking component which was involved in the event, otherwise empty if no locking component was involved  # noqa: E501

        :param lock_identifier: The lock_identifier of this SystemProtocolEntry.  # noqa: E501
        :type: str
        """

        self._lock_identifier = lock_identifier

    @property
    def lock_id(self):
        """Gets the lock_id of this SystemProtocolEntry.  # noqa: E501

        Unique id of the locking component which was involved in the event if it still exists in the access control system, otherwise empty  # noqa: E501

        :return: The lock_id of this SystemProtocolEntry.  # noqa: E501
        :rtype: int
        """
        return self._lock_id

    @lock_id.setter
    def lock_id(self, lock_id):
        """Sets the lock_id of this SystemProtocolEntry.

        Unique id of the locking component which was involved in the event if it still exists in the access control system, otherwise empty  # noqa: E501

        :param lock_id: The lock_id of this SystemProtocolEntry.  # noqa: E501
        :type: int
        """

        self._lock_id = lock_id

    @property
    def medium_identifier(self):
        """Gets the medium_identifier of this SystemProtocolEntry.  # noqa: E501

        Identifier of the medium which was involved in the event, otherwise empty if no medium was involved,   # noqa: E501

        :return: The medium_identifier of this SystemProtocolEntry.  # noqa: E501
        :rtype: str
        """
        return self._medium_identifier

    @medium_identifier.setter
    def medium_identifier(self, medium_identifier):
        """Sets the medium_identifier of this SystemProtocolEntry.

        Identifier of the medium which was involved in the event, otherwise empty if no medium was involved,   # noqa: E501

        :param medium_identifier: The medium_identifier of this SystemProtocolEntry.  # noqa: E501
        :type: str
        """

        self._medium_identifier = medium_identifier

    @property
    def medium_id(self):
        """Gets the medium_id of this SystemProtocolEntry.  # noqa: E501

        Unique id of the medium which was involved in the event if it still exists in the access control system, otherwise empty  # noqa: E501

        :return: The medium_id of this SystemProtocolEntry.  # noqa: E501
        :rtype: int
        """
        return self._medium_id

    @medium_id.setter
    def medium_id(self, medium_id):
        """Sets the medium_id of this SystemProtocolEntry.

        Unique id of the medium which was involved in the event if it still exists in the access control system, otherwise empty  # noqa: E501

        :param medium_id: The medium_id of this SystemProtocolEntry.  # noqa: E501
        :type: int
        """

        self._medium_id = medium_id

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
        if issubclass(SystemProtocolEntry, dict):
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
        if not isinstance(other, SystemProtocolEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
