# airkey.LockProtocolApi

All URIs are relative to *https://integration.api.airkey.evva.com:443/cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_lock_protocol**](LockProtocolApi.md#get_lock_protocol) | **GET** /v1/lock-protocol | Gets protocol of locks.

# **get_lock_protocol**
> LockProtocolPagingList get_lock_protocol(offset=offset, limit=limit, area_id=area_id, lock_id=lock_id, _from=_from, to=to, language=language)

Gets protocol of locks.

Returns a list of protocols of all locks in the access control system.

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
api_instance = airkey.LockProtocolApi(airkey.ApiClient(configuration))
offset = 56 # int | Offset for paging (optional)
limit = 56 # int | Limit of result size (optional)
area_id = 789 # int | Filter protocols by area id (optional)
lock_id = 789 # int | Filter protocols by lock id (optional)
_from = '_from_example' # str | Timestamp from when the protocols need to be considered (ISO 8601-format compliant date with time in UTC, milliseconds precision) (optional)
to = 'to_example' # str | Timestamp until when the protocols need to be considered (ISO 8601-format compliant date with time in UTC, milliseconds precision) (optional)
language = 'de-DE' # str | Language codes as a comma-separated list of IETF (bcp47) language tags (e.g. de-DE, en-UK) or \"all\" for all possible languages used for translations (optional) (default to de-DE)

try:
    # Gets protocol of locks.
    api_response = api_instance.get_lock_protocol(offset=offset, limit=limit, area_id=area_id, lock_id=lock_id, _from=_from, to=to, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LockProtocolApi->get_lock_protocol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset for paging | [optional] 
 **limit** | **int**| Limit of result size | [optional] 
 **area_id** | **int**| Filter protocols by area id | [optional] 
 **lock_id** | **int**| Filter protocols by lock id | [optional] 
 **_from** | **str**| Timestamp from when the protocols need to be considered (ISO 8601-format compliant date with time in UTC, milliseconds precision) | [optional] 
 **to** | **str**| Timestamp until when the protocols need to be considered (ISO 8601-format compliant date with time in UTC, milliseconds precision) | [optional] 
 **language** | **str**| Language codes as a comma-separated list of IETF (bcp47) language tags (e.g. de-DE, en-UK) or \&quot;all\&quot; for all possible languages used for translations | [optional] [default to de-DE]

### Return type

[**LockProtocolPagingList**](LockProtocolPagingList.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

