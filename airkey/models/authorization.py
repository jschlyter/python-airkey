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

class Authorization(object):
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
        'version': 'int',
        'medium': 'SimpleMedium',
        'lock': 'SimpleLock',
        'area': 'SimpleArea',
        'person_id': 'int',
        'current_state': 'str',
        'created_on': 'str',
        'updated_on': 'str',
        'synchronized_on': 'str',
        'deletion_requested': 'bool',
        'authorization_info_list': 'list[AuthorizationInfo]',
        'custom': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'medium': 'medium',
        'lock': 'lock',
        'area': 'area',
        'person_id': 'personId',
        'current_state': 'currentState',
        'created_on': 'createdOn',
        'updated_on': 'updatedOn',
        'synchronized_on': 'synchronizedOn',
        'deletion_requested': 'deletionRequested',
        'authorization_info_list': 'authorizationInfoList',
        'custom': 'custom'
    }

    def __init__(self, id=None, version=None, medium=None, lock=None, area=None, person_id=None, current_state=None, created_on=None, updated_on=None, synchronized_on=None, deletion_requested=None, authorization_info_list=None, custom=None):  # noqa: E501
        """Authorization - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._version = None
        self._medium = None
        self._lock = None
        self._area = None
        self._person_id = None
        self._current_state = None
        self._created_on = None
        self._updated_on = None
        self._synchronized_on = None
        self._deletion_requested = None
        self._authorization_info_list = None
        self._custom = None
        self.discriminator = None
        self.id = id
        self.version = version
        self.medium = medium
        if lock is not None:
            self.lock = lock
        if area is not None:
            self.area = area
        if person_id is not None:
            self.person_id = person_id
        if current_state is not None:
            self.current_state = current_state
        if created_on is not None:
            self.created_on = created_on
        if updated_on is not None:
            self.updated_on = updated_on
        if synchronized_on is not None:
            self.synchronized_on = synchronized_on
        if deletion_requested is not None:
            self.deletion_requested = deletion_requested
        self.authorization_info_list = authorization_info_list
        if custom is not None:
            self.custom = custom

    @property
    def id(self):
        """Gets the id of this Authorization.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The id of this Authorization.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Authorization.

        Unique identifier  # noqa: E501

        :param id: The id of this Authorization.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def version(self):
        """Gets the version of this Authorization.  # noqa: E501

        Current version number of the authorization  # noqa: E501

        :return: The version of this Authorization.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Authorization.

        Current version number of the authorization  # noqa: E501

        :param version: The version of this Authorization.  # noqa: E501
        :type: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def medium(self):
        """Gets the medium of this Authorization.  # noqa: E501


        :return: The medium of this Authorization.  # noqa: E501
        :rtype: SimpleMedium
        """
        return self._medium

    @medium.setter
    def medium(self, medium):
        """Sets the medium of this Authorization.


        :param medium: The medium of this Authorization.  # noqa: E501
        :type: SimpleMedium
        """
        if medium is None:
            raise ValueError("Invalid value for `medium`, must not be `None`")  # noqa: E501

        self._medium = medium

    @property
    def lock(self):
        """Gets the lock of this Authorization.  # noqa: E501


        :return: The lock of this Authorization.  # noqa: E501
        :rtype: SimpleLock
        """
        return self._lock

    @lock.setter
    def lock(self, lock):
        """Sets the lock of this Authorization.


        :param lock: The lock of this Authorization.  # noqa: E501
        :type: SimpleLock
        """

        self._lock = lock

    @property
    def area(self):
        """Gets the area of this Authorization.  # noqa: E501


        :return: The area of this Authorization.  # noqa: E501
        :rtype: SimpleArea
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this Authorization.


        :param area: The area of this Authorization.  # noqa: E501
        :type: SimpleArea
        """

        self._area = area

    @property
    def person_id(self):
        """Gets the person_id of this Authorization.  # noqa: E501

        Owner of this authorization  # noqa: E501

        :return: The person_id of this Authorization.  # noqa: E501
        :rtype: int
        """
        return self._person_id

    @person_id.setter
    def person_id(self, person_id):
        """Sets the person_id of this Authorization.

        Owner of this authorization  # noqa: E501

        :param person_id: The person_id of this Authorization.  # noqa: E501
        :type: int
        """

        self._person_id = person_id

    @property
    def current_state(self):
        """Gets the current_state of this Authorization.  # noqa: E501

        Current state of authorization  # noqa: E501

        :return: The current_state of this Authorization.  # noqa: E501
        :rtype: str
        """
        return self._current_state

    @current_state.setter
    def current_state(self, current_state):
        """Sets the current_state of this Authorization.

        Current state of authorization  # noqa: E501

        :param current_state: The current_state of this Authorization.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNCHANGED", "MODIFIED", "CREATED", "DELETED", "CREATED_BLACKLISTED", "DEACTIVATED_RESTORABLE"]  # noqa: E501
        if current_state not in allowed_values:
            raise ValueError(
                "Invalid value for `current_state` ({0}), must be one of {1}"  # noqa: E501
                .format(current_state, allowed_values)
            )

        self._current_state = current_state

    @property
    def created_on(self):
        """Gets the created_on of this Authorization.  # noqa: E501

        Timestamp when the authorization was created (ISO 8601-format compliant date with time in UTC, milliseconds precision)  # noqa: E501

        :return: The created_on of this Authorization.  # noqa: E501
        :rtype: str
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Authorization.

        Timestamp when the authorization was created (ISO 8601-format compliant date with time in UTC, milliseconds precision)  # noqa: E501

        :param created_on: The created_on of this Authorization.  # noqa: E501
        :type: str
        """

        self._created_on = created_on

    @property
    def updated_on(self):
        """Gets the updated_on of this Authorization.  # noqa: E501

        Timestamp when the authorization was last updated (ISO 8601-format compliant date with time in UTC, milliseconds precision)  # noqa: E501

        :return: The updated_on of this Authorization.  # noqa: E501
        :rtype: str
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this Authorization.

        Timestamp when the authorization was last updated (ISO 8601-format compliant date with time in UTC, milliseconds precision)  # noqa: E501

        :param updated_on: The updated_on of this Authorization.  # noqa: E501
        :type: str
        """

        self._updated_on = updated_on

    @property
    def synchronized_on(self):
        """Gets the synchronized_on of this Authorization.  # noqa: E501

        Timestamp when the authorization was last synchronized with the medium (ISO 8601-format compliant date with time in UTC, milliseconds precision)  # noqa: E501

        :return: The synchronized_on of this Authorization.  # noqa: E501
        :rtype: str
        """
        return self._synchronized_on

    @synchronized_on.setter
    def synchronized_on(self, synchronized_on):
        """Sets the synchronized_on of this Authorization.

        Timestamp when the authorization was last synchronized with the medium (ISO 8601-format compliant date with time in UTC, milliseconds precision)  # noqa: E501

        :param synchronized_on: The synchronized_on of this Authorization.  # noqa: E501
        :type: str
        """

        self._synchronized_on = synchronized_on

    @property
    def deletion_requested(self):
        """Gets the deletion_requested of this Authorization.  # noqa: E501

        Is a deletion of the authorization requested or not  # noqa: E501

        :return: The deletion_requested of this Authorization.  # noqa: E501
        :rtype: bool
        """
        return self._deletion_requested

    @deletion_requested.setter
    def deletion_requested(self, deletion_requested):
        """Sets the deletion_requested of this Authorization.

        Is a deletion of the authorization requested or not  # noqa: E501

        :param deletion_requested: The deletion_requested of this Authorization.  # noqa: E501
        :type: bool
        """

        self._deletion_requested = deletion_requested

    @property
    def authorization_info_list(self):
        """Gets the authorization_info_list of this Authorization.  # noqa: E501

        List of authorization details  # noqa: E501

        :return: The authorization_info_list of this Authorization.  # noqa: E501
        :rtype: list[AuthorizationInfo]
        """
        return self._authorization_info_list

    @authorization_info_list.setter
    def authorization_info_list(self, authorization_info_list):
        """Sets the authorization_info_list of this Authorization.

        List of authorization details  # noqa: E501

        :param authorization_info_list: The authorization_info_list of this Authorization.  # noqa: E501
        :type: list[AuthorizationInfo]
        """
        if authorization_info_list is None:
            raise ValueError("Invalid value for `authorization_info_list`, must not be `None`")  # noqa: E501

        self._authorization_info_list = authorization_info_list

    @property
    def custom(self):
        """Gets the custom of this Authorization.  # noqa: E501

        Authorization combines different authorization types  # noqa: E501

        :return: The custom of this Authorization.  # noqa: E501
        :rtype: bool
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this Authorization.

        Authorization combines different authorization types  # noqa: E501

        :param custom: The custom of this Authorization.  # noqa: E501
        :type: bool
        """

        self._custom = custom

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
        if issubclass(Authorization, dict):
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
        if not isinstance(other, Authorization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
