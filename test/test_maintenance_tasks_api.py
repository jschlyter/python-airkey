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
from airkey_client.api.maintenance_tasks_api import MaintenanceTasksApi  # noqa: E501
from airkey_client.rest import ApiException


class TestMaintenanceTasksApi(unittest.TestCase):
    """MaintenanceTasksApi unit test stubs"""

    def setUp(self):
        self.api = MaintenanceTasksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_maintenance_tasks(self):
        """Test case for get_maintenance_tasks

        Gets all maintenance tasks.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
