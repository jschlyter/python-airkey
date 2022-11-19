# airkey.MediaApi

All URIs are relative to *https://integration.api.airkey.evva.com:443/cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_owner_to_medium**](MediaApi.md#assign_owner_to_medium) | **POST** /v1/media/assign | Assigns a person to a medium for each provided assignment.
[**cancel_medium_assignments**](MediaApi.md#cancel_medium_assignments) | **POST** /v1/media/cancel-assignment | Cancels assignments of media.
[**create_phones**](MediaApi.md#create_phones) | **POST** /v1/media/phones | Adds list of new phones.
[**deactivate_medium**](MediaApi.md#deactivate_medium) | **POST** /v1/media/{mediumId}/deactivate | Deactivates provided medium.
[**delete_phones**](MediaApi.md#delete_phones) | **DELETE** /v1/media/phones | Deletes provided phones.
[**empty_medium**](MediaApi.md#empty_medium) | **POST** /v1/media/{mediumId}/empty | Empties provided medium.
[**generate_pairing_code_for_phone**](MediaApi.md#generate_pairing_code_for_phone) | **POST** /v1/media/phones/{phoneId}/pairing | Generates a new pairing code for a phone.
[**get_card**](MediaApi.md#get_card) | **GET** /v1/media/cards/{cardId} | Gets information of specific card.
[**get_cards**](MediaApi.md#get_cards) | **GET** /v1/media/cards | Gets information of all cards.
[**get_media**](MediaApi.md#get_media) | **GET** /v1/media | Gets information of all media.
[**get_medium**](MediaApi.md#get_medium) | **GET** /v1/media/{mediumId} | Gets information of a specific medium.
[**get_phone**](MediaApi.md#get_phone) | **GET** /v1/media/phones/{phoneId} | Gets information of specific phone.
[**get_phones**](MediaApi.md#get_phones) | **GET** /v1/media/phones | Gets information of all phones.
[**reactivate_medium**](MediaApi.md#reactivate_medium) | **POST** /v1/media/{mediumId}/reactivate | Reactivates provided medium.
[**reset_pin_of_phone**](MediaApi.md#reset_pin_of_phone) | **POST** /v1/media/phones/{phoneId}/pin-reset | Resets PIN of the phone.
[**send_registration_code_to_phone**](MediaApi.md#send_registration_code_to_phone) | **POST** /v1/media/phones/{phoneId}/send-registration-code-with-parameters | Sends pairing code to phone while the SMS text to be sent can be configured.
[**send_registration_code_to_phone1**](MediaApi.md#send_registration_code_to_phone1) | **POST** /v1/media/phones/{phoneId}/send-registration-code | Sends pairing code to phone.
[**update_cards**](MediaApi.md#update_cards) | **PUT** /v1/media/cards | Updates list of cards.
[**update_phones**](MediaApi.md#update_phones) | **PUT** /v1/media/phones | Updates list of phones.

# **assign_owner_to_medium**
> list[MediumAssignment] assign_owner_to_medium(body)

Assigns a person to a medium for each provided assignment.

Creates a person assignment for a medium according to the provided list of assignments and returns the resulting assignment list.

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
api_instance = airkey.MediaApi(airkey.ApiClient(configuration))
body = [airkey.MediumAssignment()] # list[MediumAssignment] | List of medium assignments

try:
    # Assigns a person to a medium for each provided assignment.
    api_response = api_instance.assign_owner_to_medium(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->assign_owner_to_medium: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MediumAssignment]**](MediumAssignment.md)| List of medium assignments | 

### Return type

[**list[MediumAssignment]**](MediumAssignment.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_medium_assignments**
> list[int] cancel_medium_assignments(body)

Cancels assignments of media.

Cancels the person assignments of the provided list of media and returns a list of identifiers of the updated medium objects.

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
api_instance = airkey.MediaApi(airkey.ApiClient(configuration))
body = [56] # list[int] | List of unique medium identifiers

try:
    # Cancels assignments of media.
    api_response = api_instance.cancel_medium_assignments(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->cancel_medium_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[int]**](int.md)| List of unique medium identifiers | 

### Return type

**list[int]**

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_phones**
> list[Phone] create_phones(body)

Adds list of new phones.

Creates and adds the provided phones to the access control system and returns a list of the new phone objects. Please check before if a phone already exists with the given phone number to prevent duplicates.

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
api_instance = airkey.MediaApi(airkey.ApiClient(configuration))
body = [airkey.PhoneCreate()] # list[PhoneCreate] | List of phones to be added

try:
    # Adds list of new phones.
    api_response = api_instance.create_phones(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->create_phones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[PhoneCreate]**](PhoneCreate.md)| List of phones to be added | 

### Return type

[**list[Phone]**](Phone.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_medium**
> Medium deactivate_medium(medium_id, reason, comment=comment)

Deactivates provided medium.

Deactivates the provided medium and returns a new version of the medium object. The fields \"reason\" and \"comment\" are saved in the system protocol and are not part of the response.

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
api_instance = airkey.MediaApi(airkey.ApiClient(configuration))
medium_id = 789 # int | Unique identifier of the medium to be deactivated
reason = 'reason_example' # str | Reason of deactivation (user defined input that can be used to describe the reasons for deactivating a medium, e.g. has been lost / was stolen / is broken)
comment = 'comment_example' # str | Additional comment of deactivation (user defined input that can be used to add further details regarding the reason for deactivating a medium, e.g. when all details won't fit within the reason field) (optional)

try:
    # Deactivates provided medium.
    api_response = api_instance.deactivate_medium(medium_id, reason, comment=comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->deactivate_medium: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **medium_id** | **int**| Unique identifier of the medium to be deactivated | 
 **reason** | **str**| Reason of deactivation (user defined input that can be used to describe the reasons for deactivating a medium, e.g. has been lost / was stolen / is broken) | 
 **comment** | **str**| Additional comment of deactivation (user defined input that can be used to add further details regarding the reason for deactivating a medium, e.g. when all details won&#x27;t fit within the reason field) | [optional] 

### Return type

[**Medium**](Medium.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_phones**
> list[int] delete_phones(body)

Deletes provided phones.

Deletes the provided phones and returns a list of identifiers of all deleted objects.

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
api_instance = airkey.MediaApi(airkey.ApiClient(configuration))
body = [56] # list[int] | List of unique identifiers of all phones to be deleted

try:
    # Deletes provided phones.
    api_response = api_instance.delete_phones(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->delete_phones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[int]**](int.md)| List of unique identifiers of all phones to be deleted | 

### Return type

**list[int]**

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **empty_medium**
> Medium empty_medium(medium_id)

Empties provided medium.

Empties the provided medium and returns a new version of the medium object. All authorizations will be deleted from the medium. The person assignment of the medium does not get cancelled.

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
api_instance = airkey.MediaApi(airkey.ApiClient(configuration))
medium_id = 789 # int | Unique identifier of the medium

try:
    # Empties provided medium.
    api_response = api_instance.empty_medium(medium_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->empty_medium: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **medium_id** | **int**| Unique identifier of the medium | 

### Return type

[**Medium**](Medium.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_pairing_code_for_phone**
> Phone generate_pairing_code_for_phone(phone_id)

Generates a new pairing code for a phone.

Generates a new pairing code for the provided phone and returns a new version of the phone object.

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
api_instance = airkey.MediaApi(airkey.ApiClient(configuration))
phone_id = 789 # int | Unique identifier of the phone

try:
    # Generates a new pairing code for a phone.
    api_response = api_instance.generate_pairing_code_for_phone(phone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->generate_pairing_code_for_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_id** | **int**| Unique identifier of the phone | 

### Return type

[**Phone**](Phone.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_card**
> Card get_card(card_id)

Gets information of specific card.

Returns all information of provided medium of type 'card'.

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
api_instance = airkey.MediaApi(airkey.ApiClient(configuration))
card_id = 789 # int | Unique identifier of the card

try:
    # Gets information of specific card.
    api_response = api_instance.get_card(card_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->get_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_id** | **int**| Unique identifier of the card | 

### Return type

[**Card**](Card.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cards**
> CardPagingList get_cards(person_id=person_id, locking_system_id=locking_system_id, assignment_status=assignment_status, offset=offset, limit=limit)

Gets information of all cards.

Returns a list of all media of type 'card' defined in the access control system.

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
api_instance = airkey.MediaApi(airkey.ApiClient(configuration))
person_id = 789 # int | Filter cards by person id (optional)
locking_system_id = 789 # int | Filter cards by technical identifier lockingSystemId (optional)
assignment_status = 'assignment_status_example' # str | Filter cards by assignment status (optional)
offset = 56 # int | Offset for paging (optional)
limit = 56 # int | Limit of result size (optional)

try:
    # Gets information of all cards.
    api_response = api_instance.get_cards(person_id=person_id, locking_system_id=locking_system_id, assignment_status=assignment_status, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->get_cards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **int**| Filter cards by person id | [optional] 
 **locking_system_id** | **int**| Filter cards by technical identifier lockingSystemId | [optional] 
 **assignment_status** | **str**| Filter cards by assignment status | [optional] 
 **offset** | **int**| Offset for paging | [optional] 
 **limit** | **int**| Limit of result size | [optional] 

### Return type

[**CardPagingList**](CardPagingList.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media**
> MediumPagingList get_media(person_id=person_id, locking_system_id=locking_system_id, assignment_status=assignment_status, offset=offset, limit=limit)

Gets information of all media.

Returns a list of all media defined in the access control system, sorted by medium id in ascending order.

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
api_instance = airkey.MediaApi(airkey.ApiClient(configuration))
person_id = 789 # int | Filter media by person id (optional)
locking_system_id = 789 # int | Filter media by technical identifier lockingSystemId (optional)
assignment_status = 'assignment_status_example' # str | Filter media by assignment status (optional)
offset = 56 # int | Offset for paging (optional)
limit = 56 # int | Limit of result size (optional)

try:
    # Gets information of all media.
    api_response = api_instance.get_media(person_id=person_id, locking_system_id=locking_system_id, assignment_status=assignment_status, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->get_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **int**| Filter media by person id | [optional] 
 **locking_system_id** | **int**| Filter media by technical identifier lockingSystemId | [optional] 
 **assignment_status** | **str**| Filter media by assignment status | [optional] 
 **offset** | **int**| Offset for paging | [optional] 
 **limit** | **int**| Limit of result size | [optional] 

### Return type

[**MediumPagingList**](MediumPagingList.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_medium**
> Medium get_medium(medium_id)

Gets information of a specific medium.

Returns all information of a specific medium defined in the access control system.

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
api_instance = airkey.MediaApi(airkey.ApiClient(configuration))
medium_id = 789 # int | Unique identifier of the medium

try:
    # Gets information of a specific medium.
    api_response = api_instance.get_medium(medium_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->get_medium: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **medium_id** | **int**| Unique identifier of the medium | 

### Return type

[**Medium**](Medium.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phone**
> Phone get_phone(phone_id)

Gets information of specific phone.

Returns all information of provided medium of type 'phone'.

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
api_instance = airkey.MediaApi(airkey.ApiClient(configuration))
phone_id = 789 # int | Unique identifier of the phone

try:
    # Gets information of specific phone.
    api_response = api_instance.get_phone(phone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->get_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_id** | **int**| Unique identifier of the phone | 

### Return type

[**Phone**](Phone.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phones**
> PhonePagingList get_phones(person_id=person_id, locking_system_id=locking_system_id, assignment_status=assignment_status, phone_number=phone_number, offset=offset, limit=limit)

Gets information of all phones.

Returns a list of all media of type 'phone' defined in the access control system.

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
api_instance = airkey.MediaApi(airkey.ApiClient(configuration))
person_id = 789 # int | Filter phones by person id (optional)
locking_system_id = 789 # int | Filter phones by technical identifier lockingSystemId (optional)
assignment_status = 'assignment_status_example' # str | Filter phones by assignment status (optional)
phone_number = 'phone_number_example' # str | Filter phones by phone number (optional)
offset = 56 # int | Offset for paging (optional)
limit = 56 # int | Limit of result size (optional)

try:
    # Gets information of all phones.
    api_response = api_instance.get_phones(person_id=person_id, locking_system_id=locking_system_id, assignment_status=assignment_status, phone_number=phone_number, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->get_phones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **int**| Filter phones by person id | [optional] 
 **locking_system_id** | **int**| Filter phones by technical identifier lockingSystemId | [optional] 
 **assignment_status** | **str**| Filter phones by assignment status | [optional] 
 **phone_number** | **str**| Filter phones by phone number | [optional] 
 **offset** | **int**| Offset for paging | [optional] 
 **limit** | **int**| Limit of result size | [optional] 

### Return type

[**PhonePagingList**](PhonePagingList.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reactivate_medium**
> Medium reactivate_medium(medium_id, reason, recover_authorizations, comment=comment)

Reactivates provided medium.

Reactivates the provided medium and returns a new version of the medium object. The fields \"reason\" and \"comment\" are saved in the system protocol and are not part of the response.

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
api_instance = airkey.MediaApi(airkey.ApiClient(configuration))
medium_id = 789 # int | Unique identifier of the medium to be reactivated
reason = 'reason_example' # str | Reason of reactivation (user defined input that can be used to describe the reasons for reactivating a medium, e.g. a medium has been found again)
recover_authorizations = true # bool | Recover authorizations available prior to deactivation
comment = 'comment_example' # str | Additional comment of reactivation (user defined input that can be used to add further details regarding the reason for reactivating a medium, e.g. when all details won't fit within the reason field) (optional)

try:
    # Reactivates provided medium.
    api_response = api_instance.reactivate_medium(medium_id, reason, recover_authorizations, comment=comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->reactivate_medium: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **medium_id** | **int**| Unique identifier of the medium to be reactivated | 
 **reason** | **str**| Reason of reactivation (user defined input that can be used to describe the reasons for reactivating a medium, e.g. a medium has been found again) | 
 **recover_authorizations** | **bool**| Recover authorizations available prior to deactivation | 
 **comment** | **str**| Additional comment of reactivation (user defined input that can be used to add further details regarding the reason for reactivating a medium, e.g. when all details won&#x27;t fit within the reason field) | [optional] 

### Return type

[**Medium**](Medium.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_pin_of_phone**
> Phone reset_pin_of_phone(phone_id)

Resets PIN of the phone.

Resets the PIN of the provided phone and returns new version of the phone object with set PIN reset time. After the phone was synchronized the PIN flag is reset.

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
api_instance = airkey.MediaApi(airkey.ApiClient(configuration))
phone_id = 789 # int | Unique identifier of the phone to reset the PIN

try:
    # Resets PIN of the phone.
    api_response = api_instance.reset_pin_of_phone(phone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->reset_pin_of_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_id** | **int**| Unique identifier of the phone to reset the PIN | 

### Return type

[**Phone**](Phone.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_registration_code_to_phone**
> Phone send_registration_code_to_phone(phone_id, body=body)

Sends pairing code to phone while the SMS text to be sent can be configured.

Sends a generated pairing code per SMS to the phone and returns a new version of the phone object.

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
api_instance = airkey.MediaApi(airkey.ApiClient(configuration))
phone_id = 789 # int | Unique identifier of the phone
body = airkey.SendRegistrationCodeRequest() # SendRegistrationCodeRequest | Send registration code request wrapper (optional)

try:
    # Sends pairing code to phone while the SMS text to be sent can be configured.
    api_response = api_instance.send_registration_code_to_phone(phone_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->send_registration_code_to_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_id** | **int**| Unique identifier of the phone | 
 **body** | [**SendRegistrationCodeRequest**](SendRegistrationCodeRequest.md)| Send registration code request wrapper | [optional] 

### Return type

[**Phone**](Phone.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_registration_code_to_phone1**
> Phone send_registration_code_to_phone1(phone_id)

Sends pairing code to phone.

Sends a generated pairing code per SMS to the phone and returns a new version of the phone object.

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
api_instance = airkey.MediaApi(airkey.ApiClient(configuration))
phone_id = 789 # int | Unique identifier of the phone

try:
    # Sends pairing code to phone.
    api_response = api_instance.send_registration_code_to_phone1(phone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->send_registration_code_to_phone1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_id** | **int**| Unique identifier of the phone | 

### Return type

[**Phone**](Phone.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cards**
> list[Card] update_cards(body)

Updates list of cards.

Updates the provided list of cards and returns a list of new object versions.

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
api_instance = airkey.MediaApi(airkey.ApiClient(configuration))
body = [airkey.Card()] # list[Card] | List of cards to be updated

try:
    # Updates list of cards.
    api_response = api_instance.update_cards(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->update_cards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Card]**](Card.md)| List of cards to be updated | 

### Return type

[**list[Card]**](Card.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_phones**
> list[Phone] update_phones(body)

Updates list of phones.

Updates the provided list of phones and returns a list of new object versions. Please check before if a phone already exists with the given phone number to prevent duplicates.

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
api_instance = airkey.MediaApi(airkey.ApiClient(configuration))
body = [airkey.Phone()] # list[Phone] | List of phones to be updated

try:
    # Updates list of phones.
    api_response = api_instance.update_phones(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->update_phones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Phone]**](Phone.md)| List of phones to be updated | 

### Return type

[**list[Phone]**](Phone.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

