# airkey.BlacklistsApi

All URIs are relative to *https://integration.api.airkey.evva.com:443/cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_blacklists**](BlacklistsApi.md#get_blacklists) | **GET** /v1/blacklists | Gets all available blacklist entries.

# **get_blacklists**
> list[BlacklistEntry] get_blacklists(lock_id=lock_id, medium_id=medium_id)

Gets all available blacklist entries.

Returns a list of all available blacklist entries defined in the access control system, sorted by lock id and medium id in ascending order.

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
api_instance = airkey.BlacklistsApi(airkey.ApiClient(configuration))
lock_id = 789 # int | Filter blacklist entries by lock id (optional)
medium_id = 789 # int | Filter blacklist entries by medium id (optional)

try:
    # Gets all available blacklist entries.
    api_response = api_instance.get_blacklists(lock_id=lock_id, medium_id=medium_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlacklistsApi->get_blacklists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lock_id** | **int**| Filter blacklist entries by lock id | [optional] 
 **medium_id** | **int**| Filter blacklist entries by medium id | [optional] 

### Return type

[**list[BlacklistEntry]**](BlacklistEntry.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

