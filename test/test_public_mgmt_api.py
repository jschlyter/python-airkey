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
from airkey_client.api.public_mgmt_api import PublicMgmtApi  # noqa: E501
from airkey_client.rest import ApiException


class TestPublicMgmtApi(unittest.TestCase):
    """PublicMgmtApi unit test stubs"""

    def setUp(self):
        self.api = PublicMgmtApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_reset_test_data(self):
        """Test case for reset_test_data

        Resets test data in the integration environment.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
