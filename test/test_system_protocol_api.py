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
from airkey_client.api.system_protocol_api import SystemProtocolApi  # noqa: E501
from airkey_client.rest import ApiException


class TestSystemProtocolApi(unittest.TestCase):
    """SystemProtocolApi unit test stubs"""

    def setUp(self):
        self.api = SystemProtocolApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_system_protocol(self):
        """Test case for get_system_protocol

        Gets system protocol.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
