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


class EventsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_event(self, event_id, **kwargs):  # noqa: E501
        """Gets a specific event.  # noqa: E501

        Returns information about a specific event.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_event(event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int event_id: Unique identifier of the event (required)
        :return: Event
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_event_with_http_info(event_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_event_with_http_info(event_id, **kwargs)  # noqa: E501
            return data

    def get_event_with_http_info(self, event_id, **kwargs):  # noqa: E501
        """Gets a specific event.  # noqa: E501

        Returns information about a specific event.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_event_with_http_info(event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int event_id: Unique identifier of the event (required)
        :return: Event
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['event_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_event" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'event_id' is set
        if ('event_id' not in params or
                params['event_id'] is None):
            raise ValueError("Missing the required parameter `event_id` when calling `get_event`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'event_id' in params:
            path_params['eventId'] = params['event_id']  # noqa: E501

        query_params = []

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
            '/v1/events/{eventId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Event',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_events(self, created_after, **kwargs):  # noqa: E501
        """Gets a list of events.  # noqa: E501

        Returns a list of events (only returns events that are max. 7 days old), sorted by event creation timestamp in descending order. Integration environment: 7 day restriction is not enforced, use '2019-04-28T00:00Z' as 'createdAfter' query parameter to get all events.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_events(created_after, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str created_after: Filter events that were created after this timestamp (ISO 8601-format compliant date with time in UTC, milliseconds precision: yyyy-mm-ddThh:mm:ss.SSSZ). Query parameter is required because clients are encouraged to make a choice what data is actually needed (e.g. when polling this resource with an interval of 10 minutes: (createdAfter = now - 10 minutes) retrieves events which were created in the last 10 minutes. (required)
        :param str type: Filter events by event type
        :param int offset: Offset for paging
        :param int limit: Limit of result size
        :return: EventPagingList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_events_with_http_info(created_after, **kwargs)  # noqa: E501
        else:
            (data) = self.get_events_with_http_info(created_after, **kwargs)  # noqa: E501
            return data

    def get_events_with_http_info(self, created_after, **kwargs):  # noqa: E501
        """Gets a list of events.  # noqa: E501

        Returns a list of events (only returns events that are max. 7 days old), sorted by event creation timestamp in descending order. Integration environment: 7 day restriction is not enforced, use '2019-04-28T00:00Z' as 'createdAfter' query parameter to get all events.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_events_with_http_info(created_after, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str created_after: Filter events that were created after this timestamp (ISO 8601-format compliant date with time in UTC, milliseconds precision: yyyy-mm-ddThh:mm:ss.SSSZ). Query parameter is required because clients are encouraged to make a choice what data is actually needed (e.g. when polling this resource with an interval of 10 minutes: (createdAfter = now - 10 minutes) retrieves events which were created in the last 10 minutes. (required)
        :param str type: Filter events by event type
        :param int offset: Offset for paging
        :param int limit: Limit of result size
        :return: EventPagingList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['created_after', 'type', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_events" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'created_after' is set
        if ('created_after' not in params or
                params['created_after'] is None):
            raise ValueError("Missing the required parameter `created_after` when calling `get_events`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'created_after' in params:
            query_params.append(('createdAfter', params['created_after']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/v1/events', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EventPagingList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
