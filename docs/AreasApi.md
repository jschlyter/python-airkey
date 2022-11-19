# airkey.AreasApi

All URIs are relative to *https://integration.api.airkey.evva.com:443/cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_area**](AreasApi.md#get_area) | **GET** /v1/areas/{areaId} | Gets a specific area.
[**get_areas**](AreasApi.md#get_areas) | **GET** /v1/areas | Gets all available areas.

# **get_area**
> Area get_area(area_id)

Gets a specific area.

Returns a specific area defined in the access control system.

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
api_instance = airkey.AreasApi(airkey.ApiClient(configuration))
area_id = 789 # int | Unique identifier of the area

try:
    # Gets a specific area.
    api_response = api_instance.get_area(area_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AreasApi->get_area: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area_id** | **int**| Unique identifier of the area | 

### Return type

[**Area**](Area.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_areas**
> AreaPagingList get_areas(lock_id=lock_id, offset=offset, limit=limit)

Gets all available areas.

Returns a list of all available areas defined in the access control system, sorted by area id in ascending order.

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
api_instance = airkey.AreasApi(airkey.ApiClient(configuration))
lock_id = 789 # int | Filter areas by lock id (optional)
offset = 56 # int | Offset for paging (optional)
limit = 56 # int | Limit of result size (optional)

try:
    # Gets all available areas.
    api_response = api_instance.get_areas(lock_id=lock_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AreasApi->get_areas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lock_id** | **int**| Filter areas by lock id | [optional] 
 **offset** | **int**| Offset for paging | [optional] 
 **limit** | **int**| Limit of result size | [optional] 

### Return type

[**AreaPagingList**](AreaPagingList.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

