# airkey.LocksApi

All URIs are relative to *https://integration.api.airkey.evva.com:443/cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_lock**](LocksApi.md#get_lock) | **GET** /v1/locks/{lockId} | Gets information of a specific lock.
[**get_locks**](LocksApi.md#get_locks) | **GET** /v1/locks | Gets information of all locks.
[**update_lock**](LocksApi.md#update_lock) | **PUT** /v1/locks/{lockId} | Updates the provided lock.

# **get_lock**
> Lock get_lock(lock_id)

Gets information of a specific lock.

Returns a specific lock with its information.

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
api_instance = airkey.LocksApi(airkey.ApiClient(configuration))
lock_id = 789 # int | Unique identifier of the lock

try:
    # Gets information of a specific lock.
    api_response = api_instance.get_lock(lock_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocksApi->get_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lock_id** | **int**| Unique identifier of the lock | 

### Return type

[**Lock**](Lock.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_locks**
> LockPagingList get_locks(offset=offset, limit=limit, calendar_id=calendar_id, locking_system_id=locking_system_id)

Gets information of all locks.

Returns a list of all locks with their information, sorted by lock id in ascending order. Maintenance tasks of a lock can be determined by using the maintenance-tasks resource (with lockId as query parameter for a single lock).

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
api_instance = airkey.LocksApi(airkey.ApiClient(configuration))
offset = 56 # int | Offset for paging (optional)
limit = 56 # int | Limit of result size (optional)
calendar_id = 789 # int | Filter locks by holiday calendar id (optional)
locking_system_id = 789 # int | Filter locks by technical identifier lockingSystemId (optional)

try:
    # Gets information of all locks.
    api_response = api_instance.get_locks(offset=offset, limit=limit, calendar_id=calendar_id, locking_system_id=locking_system_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocksApi->get_locks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset for paging | [optional] 
 **limit** | **int**| Limit of result size | [optional] 
 **calendar_id** | **int**| Filter locks by holiday calendar id | [optional] 
 **locking_system_id** | **int**| Filter locks by technical identifier lockingSystemId | [optional] 

### Return type

[**LockPagingList**](LockPagingList.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lock**
> Lock update_lock(body, lock_id)

Updates the provided lock.

Updates the provided lock and returns the new version of the lock object.

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
api_instance = airkey.LocksApi(airkey.ApiClient(configuration))
body = airkey.Lock() # Lock | Lock to be updated
lock_id = 789 # int | Unique identifier of the lock

try:
    # Updates the provided lock.
    api_response = api_instance.update_lock(body, lock_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocksApi->update_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Lock**](Lock.md)| Lock to be updated | 
 **lock_id** | **int**| Unique identifier of the lock | 

### Return type

[**Lock**](Lock.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

