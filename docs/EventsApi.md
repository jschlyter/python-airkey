# airkey.EventsApi

All URIs are relative to *https://integration.api.airkey.evva.com:443/cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event**](EventsApi.md#get_event) | **GET** /v1/events/{eventId} | Gets a specific event.
[**get_events**](EventsApi.md#get_events) | **GET** /v1/events | Gets a list of events.

# **get_event**
> Event get_event(event_id)

Gets a specific event.

Returns information about a specific event.

### Example
```python
from __future__ import print_function
import time
import airkey
from airkey.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-API-Key
configuration = airkey.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = airkey.EventsApi(airkey.ApiClient(configuration))
event_id = 789 # int | Unique identifier of the event

try:
    # Gets a specific event.
    api_response = api_instance.get_event(event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| Unique identifier of the event | 

### Return type

[**Event**](Event.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events**
> EventPagingList get_events(created_after, type=type, offset=offset, limit=limit)

Gets a list of events.

Returns a list of events (only returns events that are max. 7 days old), sorted by event creation timestamp in descending order. Integration environment: 7 day restriction is not enforced, use '2019-04-28T00:00Z' as 'createdAfter' query parameter to get all events.

### Example
```python
from __future__ import print_function
import time
import airkey
from airkey.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-API-Key
configuration = airkey.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = airkey.EventsApi(airkey.ApiClient(configuration))
created_after = 'created_after_example' # str | Filter events that were created after this timestamp (ISO 8601-format compliant date with time in UTC, milliseconds precision: yyyy-mm-ddThh:mm:ss.SSSZ). Query parameter is required because clients are encouraged to make a choice what data is actually needed (e.g. when polling this resource with an interval of 10 minutes: (createdAfter = now - 10 minutes) retrieves events which were created in the last 10 minutes.
type = 'type_example' # str | Filter events by event type (optional)
offset = 56 # int | Offset for paging (optional)
limit = 56 # int | Limit of result size (optional)

try:
    # Gets a list of events.
    api_response = api_instance.get_events(created_after, type=type, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_after** | **str**| Filter events that were created after this timestamp (ISO 8601-format compliant date with time in UTC, milliseconds precision: yyyy-mm-ddThh:mm:ss.SSSZ). Query parameter is required because clients are encouraged to make a choice what data is actually needed (e.g. when polling this resource with an interval of 10 minutes: (createdAfter &#x3D; now - 10 minutes) retrieves events which were created in the last 10 minutes. | 
 **type** | **str**| Filter events by event type | [optional] 
 **offset** | **int**| Offset for paging | [optional] 
 **limit** | **int**| Limit of result size | [optional] 

### Return type

[**EventPagingList**](EventPagingList.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

