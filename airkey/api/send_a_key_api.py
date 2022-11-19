# coding: utf-8

"""
    EVVA AirKey Cloud API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v16.20.7
    Contact: office-wien@evva.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from airkey.api_client import ApiClient


class SendAKeyApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def send_a_key(self, body, **kwargs):  # noqa: E501
        """Sends a registration code to the phone and creates all necessary prerequisites if needed.  # noqa: E501

        Based on the given phone number this request sends a registration link via SMS for easy installation of the AirKey app. It simplifies the task of creating new mobile app users by implicitly creating new persons, phones and authorizations of type 'SIMPLE' if needed, i.e. it reuses an existing person if found. Please check before if a phone already exists with the given phone number to prevent duplicates (GET /media/phones using the filter phoneNumber). The reason why duplicates are allowed is to be able to create a new phone with an already existing phone number so it is not mandatory to delete an old phone before creating the new phone with the same phone number. <br/>Authorization creation mirrors the behaviour of POST /authorizations/simple. If you need more control consider creating a phone and person with this call and using the advanced authorization interface for creating authorizations. <br/>Either lockId or areaId needs to be set for an authorization. It's not possible to set both IDs at the same time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_a_key(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SendAKeyRequest body: Send-A-Key request wrapper (required)
        :return: SendAKeyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.send_a_key_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.send_a_key_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def send_a_key_with_http_info(self, body, **kwargs):  # noqa: E501
        """Sends a registration code to the phone and creates all necessary prerequisites if needed.  # noqa: E501

        Based on the given phone number this request sends a registration link via SMS for easy installation of the AirKey app. It simplifies the task of creating new mobile app users by implicitly creating new persons, phones and authorizations of type 'SIMPLE' if needed, i.e. it reuses an existing person if found. Please check before if a phone already exists with the given phone number to prevent duplicates (GET /media/phones using the filter phoneNumber). The reason why duplicates are allowed is to be able to create a new phone with an already existing phone number so it is not mandatory to delete an old phone before creating the new phone with the same phone number. <br/>Authorization creation mirrors the behaviour of POST /authorizations/simple. If you need more control consider creating a phone and person with this call and using the advanced authorization interface for creating authorizations. <br/>Either lockId or areaId needs to be set for an authorization. It's not possible to set both IDs at the same time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_a_key_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SendAKeyRequest body: Send-A-Key request wrapper (required)
        :return: SendAKeyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_a_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `send_a_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-API-Key']  # noqa: E501

        return self.api_client.call_api(
            '/v1/send-a-key', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SendAKeyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
