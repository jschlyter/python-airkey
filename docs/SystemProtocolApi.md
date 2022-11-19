# airkey.SystemProtocolApi

All URIs are relative to *https://integration.api.airkey.evva.com:443/cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_protocol**](SystemProtocolApi.md#get_system_protocol) | **GET** /v1/system-protocol | Gets system protocol.

# **get_system_protocol**
> SystemProtocolPagingList get_system_protocol(offset=offset, limit=limit, id=id, lock_id=lock_id, medium_id=medium_id, event=event, user_id=user_id, administrator=administrator, _from=_from, to=to, language=language)

Gets system protocol.

Returns the system protocol with all events that were conducted by the administrators of the access control system.

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
api_instance = airkey.SystemProtocolApi(airkey.ApiClient(configuration))
offset = 56 # int | Offset for paging (optional)
limit = 56 # int | Limit of result size (optional)
id = 789 # int | Filter events by unique protocol entry identifier (optional)
lock_id = 789 # int | Filter events by unique lock id (optional)
medium_id = 789 # int | Filter events by unique medium id (optional)
event = 'event_example' # str | Filter events by event type (optional)
user_id = 789 # int | Filter events by unique administrator user identifier (optional)
administrator = 'administrator_example' # str | Filter events by name of administrator (optional)
_from = '_from_example' # str | Timestamp from when the protocols need to be considered (ISO 8601-format compliant date with time in UTC, milliseconds precision: yyyy-mm-ddThh:mm:ss.SSSZ) (optional)
to = 'to_example' # str | Timestamp until when the protocol need to be considered (ISO 8601-format compliant date with time in UTC, milliseconds precision: yyyy-mm-ddThh:mm:ss.SSSZ) (optional)
language = 'de-DE' # str | Language codes as a comma-separated list of IETF (bcp47) language tags (e.g. de-DE, en-UK) or \"all\" for all possible languages used for translations (optional) (default to de-DE)

try:
    # Gets system protocol.
    api_response = api_instance.get_system_protocol(offset=offset, limit=limit, id=id, lock_id=lock_id, medium_id=medium_id, event=event, user_id=user_id, administrator=administrator, _from=_from, to=to, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemProtocolApi->get_system_protocol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset for paging | [optional] 
 **limit** | **int**| Limit of result size | [optional] 
 **id** | **int**| Filter events by unique protocol entry identifier | [optional] 
 **lock_id** | **int**| Filter events by unique lock id | [optional] 
 **medium_id** | **int**| Filter events by unique medium id | [optional] 
 **event** | **str**| Filter events by event type | [optional] 
 **user_id** | **int**| Filter events by unique administrator user identifier | [optional] 
 **administrator** | **str**| Filter events by name of administrator | [optional] 
 **_from** | **str**| Timestamp from when the protocols need to be considered (ISO 8601-format compliant date with time in UTC, milliseconds precision: yyyy-mm-ddThh:mm:ss.SSSZ) | [optional] 
 **to** | **str**| Timestamp until when the protocol need to be considered (ISO 8601-format compliant date with time in UTC, milliseconds precision: yyyy-mm-ddThh:mm:ss.SSSZ) | [optional] 
 **language** | **str**| Language codes as a comma-separated list of IETF (bcp47) language tags (e.g. de-DE, en-UK) or \&quot;all\&quot; for all possible languages used for translations | [optional] [default to de-DE]

### Return type

[**SystemProtocolPagingList**](SystemProtocolPagingList.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

