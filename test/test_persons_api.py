# coding: utf-8

"""
    EVVA AirKey Cloud API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v14.40.2
    Contact: office-wien@evva.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import airkey_client
from airkey_client.api.persons_api import PersonsApi  # noqa: E501
from airkey_client.rest import ApiException


class TestPersonsApi(unittest.TestCase):
    """PersonsApi unit test stubs"""

    def setUp(self):
        self.api = PersonsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_persons(self):
        """Test case for create_persons

        Adds list of new persons.  # noqa: E501
        """
        pass

    def test_delete_persons(self):
        """Test case for delete_persons

        Deletes provided persons.  # noqa: E501
        """
        pass

    def test_get_person(self):
        """Test case for get_person

        Gets a specific person.  # noqa: E501
        """
        pass

    def test_get_persons(self):
        """Test case for get_persons

        Gets all persons.  # noqa: E501
        """
        pass

    def test_update_persons(self):
        """Test case for update_persons

        Updates list of persons.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
