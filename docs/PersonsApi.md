# airkey.PersonsApi

All URIs are relative to *https://integration.api.airkey.evva.com:443/cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_persons**](PersonsApi.md#create_persons) | **POST** /v1/persons | Adds list of new persons.
[**delete_persons**](PersonsApi.md#delete_persons) | **DELETE** /v1/persons | Deletes provided persons.
[**get_person**](PersonsApi.md#get_person) | **GET** /v1/persons/{personId} | Gets a specific person.
[**get_persons**](PersonsApi.md#get_persons) | **GET** /v1/persons | Gets all persons.
[**update_persons**](PersonsApi.md#update_persons) | **PUT** /v1/persons | Updates list of persons.

# **create_persons**
> list[Person] create_persons(body)

Adds list of new persons.

Creates and adds the provided persons to the access control system and returns a list of the new person objects.

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
api_instance = airkey.PersonsApi(airkey.ApiClient(configuration))
body = [airkey.PersonCreate()] # list[PersonCreate] | List of persons to be added

try:
    # Adds list of new persons.
    api_response = api_instance.create_persons(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonsApi->create_persons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[PersonCreate]**](PersonCreate.md)| List of persons to be added | 

### Return type

[**list[Person]**](Person.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_persons**
> list[int] delete_persons(body)

Deletes provided persons.

Deletes the provided persons and returns a list of identifiers of all deleted objects.

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
api_instance = airkey.PersonsApi(airkey.ApiClient(configuration))
body = [56] # list[int] | List of unique identifiers of all persons to be deleted

try:
    # Deletes provided persons.
    api_response = api_instance.delete_persons(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonsApi->delete_persons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[int]**](int.md)| List of unique identifiers of all persons to be deleted | 

### Return type

**list[int]**

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person**
> Person get_person(person_id)

Gets a specific person.

Returns a specific person defined in the access control system.

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
api_instance = airkey.PersonsApi(airkey.ApiClient(configuration))
person_id = 789 # int | Unique identifier of the person

try:
    # Gets a specific person.
    api_response = api_instance.get_person(person_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonsApi->get_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **int**| Unique identifier of the person | 

### Return type

[**Person**](Person.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_persons**
> PersonPagingList get_persons(offset=offset, limit=limit, first_name=first_name, last_name=last_name, secondary_identification=secondary_identification, search=search)

Gets all persons.

Returns a list of all persons defined in the access control system, sorted by person id in ascending order.

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
api_instance = airkey.PersonsApi(airkey.ApiClient(configuration))
offset = 56 # int | Offset for paging (optional)
limit = 56 # int | Limit of result size (optional)
first_name = 'first_name_example' # str | Filter persons by first name (optional)
last_name = 'last_name_example' # str | Filter persons by last name (optional)
secondary_identification = 'secondary_identification_example' # str | Filter persons by secondary identification (optional)
search = 'search_example' # str | Filter persons by matches in: first name, last name, secondary identification, email address, comment, street, city, country (optional)

try:
    # Gets all persons.
    api_response = api_instance.get_persons(offset=offset, limit=limit, first_name=first_name, last_name=last_name, secondary_identification=secondary_identification, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonsApi->get_persons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset for paging | [optional] 
 **limit** | **int**| Limit of result size | [optional] 
 **first_name** | **str**| Filter persons by first name | [optional] 
 **last_name** | **str**| Filter persons by last name | [optional] 
 **secondary_identification** | **str**| Filter persons by secondary identification | [optional] 
 **search** | **str**| Filter persons by matches in: first name, last name, secondary identification, email address, comment, street, city, country | [optional] 

### Return type

[**PersonPagingList**](PersonPagingList.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_persons**
> list[Person] update_persons(body)

Updates list of persons.

Updates the provided list of persons and returns a list of new object versions.

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
api_instance = airkey.PersonsApi(airkey.ApiClient(configuration))
body = [airkey.Person()] # list[Person] | List of persons to be updated

try:
    # Updates list of persons.
    api_response = api_instance.update_persons(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonsApi->update_persons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Person]**](Person.md)| List of persons to be updated | 

### Return type

[**list[Person]**](Person.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

