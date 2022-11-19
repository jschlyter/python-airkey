# airkey.AuthorizationsApi

All URIs are relative to *https://integration.api.airkey.evva.com:443/cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_fetch_simple_authorization**](AuthorizationsApi.md#create_or_fetch_simple_authorization) | **POST** /v1/authorizations/simple | Creates simple authorizations
[**create_or_update_authorizations_with_advanced_options**](AuthorizationsApi.md#create_or_update_authorizations_with_advanced_options) | **POST** /v1/authorizations/advanced | Creates new and updates existing authorizations (advanced version - can be used to create/update all types of authorizations).
[**delete_authorization**](AuthorizationsApi.md#delete_authorization) | **PUT** /v1/authorizations | Requests deletion of provided authorizations.
[**get_authorization**](AuthorizationsApi.md#get_authorization) | **GET** /v1/authorizations/{authorizationId} | Gets a specific authorization.
[**get_authorizations**](AuthorizationsApi.md#get_authorizations) | **GET** /v1/authorizations | Gets all authorizations for locks and areas.

# **create_or_fetch_simple_authorization**
> Authorization create_or_fetch_simple_authorization(body)

Creates simple authorizations

Creates an authorization of type 'SIMPLE' (same as using SimpleAuthorizationInfo in POST /authorizations/advanced). If an authorization can’t be created (e.g. already has 8 authorizations), an error will be returned. Be advised that this is only a simplified interface for fulfilling basic authorization needs, a 'SIMPLE' authorization will actually consist of up to 3 AuthorizationInfo elements combined (of type one-day and permanent) within an authorization -> authorization of type 'SIMPLE' will never be part of a response. <br/>The dates and timestamps for the authorizations should always be provided regardless of the time zone. <br/>Either lockId or areaId needs to be set for an authorization. It's not possible to set both IDs at the same time.

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
api_instance = airkey.AuthorizationsApi(airkey.ApiClient(configuration))
body = airkey.SimpleAuthorizationCreate() # SimpleAuthorizationCreate | Authorization to be created

try:
    # Creates simple authorizations
    api_response = api_instance.create_or_fetch_simple_authorization(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationsApi->create_or_fetch_simple_authorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SimpleAuthorizationCreate**](SimpleAuthorizationCreate.md)| Authorization to be created | 

### Return type

[**Authorization**](Authorization.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_authorizations_with_advanced_options**
> list[Authorization] create_or_update_authorizations_with_advanced_options(body)

Creates new and updates existing authorizations (advanced version - can be used to create/update all types of authorizations).

Creates the provided authorizations to be added in the access control system, updates the provided existing authorizations and returns a list of the new authorization object versions. <br/> The dates and timestamps for the authorizations should always be provided regardless of the time zone. <br/>Create authorization: Either lockId or areaId needs to be set for an authorization. It's not possible to set both IDs at the same time. <br/>Update authorization: It's not possible to change a lockId/areaId

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
api_instance = airkey.AuthorizationsApi(airkey.ApiClient(configuration))
body = airkey.AuthorizationChange() # AuthorizationChange | Authorizations to be created or updated

try:
    # Creates new and updates existing authorizations (advanced version - can be used to create/update all types of authorizations).
    api_response = api_instance.create_or_update_authorizations_with_advanced_options(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationsApi->create_or_update_authorizations_with_advanced_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthorizationChange**](AuthorizationChange.md)| Authorizations to be created or updated | 

### Return type

[**list[Authorization]**](Authorization.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_authorization**
> list[Authorization] delete_authorization(body)

Requests deletion of provided authorizations.

Requests and marks provided authorizations for deletion and returns a list of the new authorization object versions.

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
api_instance = airkey.AuthorizationsApi(airkey.ApiClient(configuration))
body = [airkey.AuthorizationDelete()] # list[AuthorizationDelete] | Authorizations to be deleted

try:
    # Requests deletion of provided authorizations.
    api_response = api_instance.delete_authorization(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationsApi->delete_authorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AuthorizationDelete]**](AuthorizationDelete.md)| Authorizations to be deleted | 

### Return type

[**list[Authorization]**](Authorization.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorization**
> Authorization get_authorization(authorization_id)

Gets a specific authorization.

Returns a specific authorization for locks and areas defined in the access control system.

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
api_instance = airkey.AuthorizationsApi(airkey.ApiClient(configuration))
authorization_id = 789 # int | Unique identifier of the authorization

try:
    # Gets a specific authorization.
    api_response = api_instance.get_authorization(authorization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationsApi->get_authorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_id** | **int**| Unique identifier of the authorization | 

### Return type

[**Authorization**](Authorization.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorizations**
> AuthorizationPagingList get_authorizations(offset=offset, limit=limit, lock_id=lock_id, area_id=area_id, medium_id=medium_id, person_id=person_id)

Gets all authorizations for locks and areas.

Returns a list of all authorizations for locks and areas defined in the access control system, sorted by 'created on' timestamp in descending order.

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
api_instance = airkey.AuthorizationsApi(airkey.ApiClient(configuration))
offset = 56 # int | Offset for paging (optional)
limit = 56 # int | Limit of result size (optional)
lock_id = 789 # int | Filter authorizations by lock id (optional)
area_id = 789 # int | Filter authorizations by area id (optional)
medium_id = 789 # int | Filter authorizations by medium id (optional)
person_id = 789 # int | Filter authorizations by person id (optional)

try:
    # Gets all authorizations for locks and areas.
    api_response = api_instance.get_authorizations(offset=offset, limit=limit, lock_id=lock_id, area_id=area_id, medium_id=medium_id, person_id=person_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationsApi->get_authorizations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset for paging | [optional] 
 **limit** | **int**| Limit of result size | [optional] 
 **lock_id** | **int**| Filter authorizations by lock id | [optional] 
 **area_id** | **int**| Filter authorizations by area id | [optional] 
 **medium_id** | **int**| Filter authorizations by medium id | [optional] 
 **person_id** | **int**| Filter authorizations by person id | [optional] 

### Return type

[**AuthorizationPagingList**](AuthorizationPagingList.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

