# airkey.MaintenanceTasksApi

All URIs are relative to *https://integration.api.airkey.evva.com:443/cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_maintenance_tasks**](MaintenanceTasksApi.md#get_maintenance_tasks) | **GET** /v1/maintenance-tasks | Gets all maintenance tasks.

# **get_maintenance_tasks**
> MaintenanceTaskPagingList get_maintenance_tasks(lock_id=lock_id, lock_identifier=lock_identifier, door_name=door_name, offset=offset, limit=limit)

Gets all maintenance tasks.

Returns a list of all available maintenance tasks of the access control system, sorted by lockId in ascending order.

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
api_instance = airkey.MaintenanceTasksApi(airkey.ApiClient(configuration))
lock_id = 789 # int | Filter maintenance tasks by lock id (optional)
lock_identifier = 'lock_identifier_example' # str | Filter maintenance tasks by lock identifier (optional)
door_name = 'door_name_example' # str | Filter maintenance tasks by door name (optional)
offset = 56 # int | Offset for paging (optional)
limit = 56 # int | Limit of result size (optional)

try:
    # Gets all maintenance tasks.
    api_response = api_instance.get_maintenance_tasks(lock_id=lock_id, lock_identifier=lock_identifier, door_name=door_name, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceTasksApi->get_maintenance_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lock_id** | **int**| Filter maintenance tasks by lock id | [optional] 
 **lock_identifier** | **str**| Filter maintenance tasks by lock identifier | [optional] 
 **door_name** | **str**| Filter maintenance tasks by door name | [optional] 
 **offset** | **int**| Offset for paging | [optional] 
 **limit** | **int**| Limit of result size | [optional] 

### Return type

[**MaintenanceTaskPagingList**](MaintenanceTaskPagingList.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

