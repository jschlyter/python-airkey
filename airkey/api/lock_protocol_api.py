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


class LockProtocolApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_lock_protocol(self, **kwargs):  # noqa: E501
        """Gets protocol of locks.  # noqa: E501

        Returns a list of protocols of all locks in the access control system.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_lock_protocol(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: Offset for paging
        :param int limit: Limit of result size
        :param int area_id: Filter protocols by area id
        :param int lock_id: Filter protocols by lock id
        :param str _from: Timestamp from when the protocols need to be considered (ISO 8601-format compliant date with time in UTC, milliseconds precision)
        :param str to: Timestamp until when the protocols need to be considered (ISO 8601-format compliant date with time in UTC, milliseconds precision)
        :param str language: Language codes as a comma-separated list of IETF (bcp47) language tags (e.g. de-DE, en-UK) or \"all\" for all possible languages used for translations
        :return: LockProtocolPagingList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_lock_protocol_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_lock_protocol_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_lock_protocol_with_http_info(self, **kwargs):  # noqa: E501
        """Gets protocol of locks.  # noqa: E501

        Returns a list of protocols of all locks in the access control system.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_lock_protocol_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: Offset for paging
        :param int limit: Limit of result size
        :param int area_id: Filter protocols by area id
        :param int lock_id: Filter protocols by lock id
        :param str _from: Timestamp from when the protocols need to be considered (ISO 8601-format compliant date with time in UTC, milliseconds precision)
        :param str to: Timestamp until when the protocols need to be considered (ISO 8601-format compliant date with time in UTC, milliseconds precision)
        :param str language: Language codes as a comma-separated list of IETF (bcp47) language tags (e.g. de-DE, en-UK) or \"all\" for all possible languages used for translations
        :return: LockProtocolPagingList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit', 'area_id', 'lock_id', '_from', 'to', 'language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_lock_protocol" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'area_id' in params:
            query_params.append(('areaId', params['area_id']))  # noqa: E501
        if 'lock_id' in params:
            query_params.append(('lockId', params['lock_id']))  # noqa: E501
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('to', params['to']))  # noqa: E501
        if 'language' in params:
            query_params.append(('language', params['language']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-API-Key']  # noqa: E501

        return self.api_client.call_api(
            '/v1/lock-protocol', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LockProtocolPagingList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)