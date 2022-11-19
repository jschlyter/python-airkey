# airkey.HolidayCalendarsApi

All URIs are relative to *https://integration.api.airkey.evva.com:443/cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_holiday_calendar_slot**](HolidayCalendarsApi.md#create_holiday_calendar_slot) | **POST** /v1/holiday-calendars/{holidayCalendarId}/slots | Adds a new holiday calendar slot to the holiday calendar.
[**delete_holiday_calendar_slot**](HolidayCalendarsApi.md#delete_holiday_calendar_slot) | **DELETE** /v1/holiday-calendars/{holidayCalendarId}/slots/{holidayCalendarSlotId} | Deletes provided holiday calendar slot.
[**get_holiday_calendar**](HolidayCalendarsApi.md#get_holiday_calendar) | **GET** /v1/holiday-calendars/{holidayCalendarId} | Gets a specific holiday calendar.
[**get_holiday_calendar_slot**](HolidayCalendarsApi.md#get_holiday_calendar_slot) | **GET** /v1/holiday-calendars/{holidayCalendarId}/slots/{holidayCalendarSlotId} | Gets a specific holiday calendar slot.
[**get_holiday_calendars**](HolidayCalendarsApi.md#get_holiday_calendars) | **GET** /v1/holiday-calendars | Gets all holiday calendars.
[**get_locks_by_calendar_id**](HolidayCalendarsApi.md#get_locks_by_calendar_id) | **GET** /v1/holiday-calendars/{holidayCalendarId}/locks | Gets all locks using the holiday calendar.
[**update_holiday_calendar**](HolidayCalendarsApi.md#update_holiday_calendar) | **PUT** /v1/holiday-calendars/{holidayCalendarId} | Updates the holiday calendar.
[**update_holiday_calendar_slot**](HolidayCalendarsApi.md#update_holiday_calendar_slot) | **PUT** /v1/holiday-calendars/{holidayCalendarId}/slots/{holidayCalendarSlotId} | Updates a holiday calendar slot of the holiday calendar.

# **create_holiday_calendar_slot**
> HolidayCalendar create_holiday_calendar_slot(body, holiday_calendar_id)

Adds a new holiday calendar slot to the holiday calendar.

Creates and adds the holiday calendar slot to the provided holiday calendar and returns the updated holiday calendar object version. In case of a series definition in the given holiday calendar slot, more than one holiday calendar slots could be created. To retrieve the newly created slots from the returned calendar, they can be filtered based on given slot name.

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
api_instance = airkey.HolidayCalendarsApi(airkey.ApiClient(configuration))
body = airkey.HolidayCalendarSlotCreate() # HolidayCalendarSlotCreate | Holiday calendar slot to be added
holiday_calendar_id = 789 # int | Unique identifier of the holiday calendar with which the holiday calendar slot should be associated

try:
    # Adds a new holiday calendar slot to the holiday calendar.
    api_response = api_instance.create_holiday_calendar_slot(body, holiday_calendar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HolidayCalendarsApi->create_holiday_calendar_slot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HolidayCalendarSlotCreate**](HolidayCalendarSlotCreate.md)| Holiday calendar slot to be added | 
 **holiday_calendar_id** | **int**| Unique identifier of the holiday calendar with which the holiday calendar slot should be associated | 

### Return type

[**HolidayCalendar**](HolidayCalendar.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_holiday_calendar_slot**
> HolidayCalendar delete_holiday_calendar_slot(body, holiday_calendar_id, holiday_calendar_slot_id)

Deletes provided holiday calendar slot.

Deletes the provided holiday calendar slot and returns the new holiday calendar object version.

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
api_instance = airkey.HolidayCalendarsApi(airkey.ApiClient(configuration))
body = airkey.HolidayCalendarSlotDelete() # HolidayCalendarSlotDelete | Holiday calendar slot to be deleted
holiday_calendar_id = 789 # int | Unique identifier of the holiday calendar with which the holiday calendar slot is associated
holiday_calendar_slot_id = 789 # int | Unique identifier of the holiday calendar slot to be deleted

try:
    # Deletes provided holiday calendar slot.
    api_response = api_instance.delete_holiday_calendar_slot(body, holiday_calendar_id, holiday_calendar_slot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HolidayCalendarsApi->delete_holiday_calendar_slot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HolidayCalendarSlotDelete**](HolidayCalendarSlotDelete.md)| Holiday calendar slot to be deleted | 
 **holiday_calendar_id** | **int**| Unique identifier of the holiday calendar with which the holiday calendar slot is associated | 
 **holiday_calendar_slot_id** | **int**| Unique identifier of the holiday calendar slot to be deleted | 

### Return type

[**HolidayCalendar**](HolidayCalendar.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_holiday_calendar**
> HolidayCalendar get_holiday_calendar(holiday_calendar_id)

Gets a specific holiday calendar.

Returns information about a specific holiday calendar defined in the access control system.

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
api_instance = airkey.HolidayCalendarsApi(airkey.ApiClient(configuration))
holiday_calendar_id = 789 # int | Unique identifier of the holiday calendar

try:
    # Gets a specific holiday calendar.
    api_response = api_instance.get_holiday_calendar(holiday_calendar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HolidayCalendarsApi->get_holiday_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **holiday_calendar_id** | **int**| Unique identifier of the holiday calendar | 

### Return type

[**HolidayCalendar**](HolidayCalendar.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_holiday_calendar_slot**
> HolidayCalendarSlot get_holiday_calendar_slot(holiday_calendar_id, holiday_calendar_slot_id)

Gets a specific holiday calendar slot.

Returns information about a specific holiday calendar slot of the holiday calendar.

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
api_instance = airkey.HolidayCalendarsApi(airkey.ApiClient(configuration))
holiday_calendar_id = 789 # int | Unique identifier of the holiday calendar with which the holiday calendar slot is associated
holiday_calendar_slot_id = 789 # int | Unique identifier of the holiday calendar slot

try:
    # Gets a specific holiday calendar slot.
    api_response = api_instance.get_holiday_calendar_slot(holiday_calendar_id, holiday_calendar_slot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HolidayCalendarsApi->get_holiday_calendar_slot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **holiday_calendar_id** | **int**| Unique identifier of the holiday calendar with which the holiday calendar slot is associated | 
 **holiday_calendar_slot_id** | **int**| Unique identifier of the holiday calendar slot | 

### Return type

[**HolidayCalendarSlot**](HolidayCalendarSlot.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_holiday_calendars**
> HolidayCalendarList get_holiday_calendars()

Gets all holiday calendars.

Returns all available holiday calendars defined in the access control system, sorted by holiday calendar id in ascending order.

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
api_instance = airkey.HolidayCalendarsApi(airkey.ApiClient(configuration))

try:
    # Gets all holiday calendars.
    api_response = api_instance.get_holiday_calendars()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HolidayCalendarsApi->get_holiday_calendars: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HolidayCalendarList**](HolidayCalendarList.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_locks_by_calendar_id**
> LockPagingList get_locks_by_calendar_id(holiday_calendar_id, offset=offset, limit=limit)

Gets all locks using the holiday calendar.

Returns a list of all locks that are currently using the provided holiday calendar.

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
api_instance = airkey.HolidayCalendarsApi(airkey.ApiClient(configuration))
holiday_calendar_id = 789 # int | Unique identifier of the holiday calendar
offset = 56 # int | Offset for paging (optional)
limit = 56 # int | Limit of result size (optional)

try:
    # Gets all locks using the holiday calendar.
    api_response = api_instance.get_locks_by_calendar_id(holiday_calendar_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HolidayCalendarsApi->get_locks_by_calendar_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **holiday_calendar_id** | **int**| Unique identifier of the holiday calendar | 
 **offset** | **int**| Offset for paging | [optional] 
 **limit** | **int**| Limit of result size | [optional] 

### Return type

[**LockPagingList**](LockPagingList.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_holiday_calendar**
> HolidayCalendar update_holiday_calendar(body, holiday_calendar_id)

Updates the holiday calendar.

Updates the provided holiday calendar and returns the new holiday calendar object version.

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
api_instance = airkey.HolidayCalendarsApi(airkey.ApiClient(configuration))
body = airkey.HolidayCalendar() # HolidayCalendar | Holiday calendar to be updated
holiday_calendar_id = 789 # int | Unique identifier of the holiday calendar to be updated

try:
    # Updates the holiday calendar.
    api_response = api_instance.update_holiday_calendar(body, holiday_calendar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HolidayCalendarsApi->update_holiday_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HolidayCalendar**](HolidayCalendar.md)| Holiday calendar to be updated | 
 **holiday_calendar_id** | **int**| Unique identifier of the holiday calendar to be updated | 

### Return type

[**HolidayCalendar**](HolidayCalendar.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_holiday_calendar_slot**
> HolidayCalendar update_holiday_calendar_slot(body, holiday_calendar_id, holiday_calendar_slot_id)

Updates a holiday calendar slot of the holiday calendar.

Updates the provided holiday calendar slot and returns the new holiday calendar object version.

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
api_instance = airkey.HolidayCalendarsApi(airkey.ApiClient(configuration))
body = airkey.HolidayCalendarSlotUpdate() # HolidayCalendarSlotUpdate | Holiday calendar slot to be updated
holiday_calendar_id = 789 # int | Unique identifier of the holiday calendar with which the holiday calendar slot is associated
holiday_calendar_slot_id = 789 # int | Unique identifier of the holiday calendar slot to be updated

try:
    # Updates a holiday calendar slot of the holiday calendar.
    api_response = api_instance.update_holiday_calendar_slot(body, holiday_calendar_id, holiday_calendar_slot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HolidayCalendarsApi->update_holiday_calendar_slot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HolidayCalendarSlotUpdate**](HolidayCalendarSlotUpdate.md)| Holiday calendar slot to be updated | 
 **holiday_calendar_id** | **int**| Unique identifier of the holiday calendar with which the holiday calendar slot is associated | 
 **holiday_calendar_slot_id** | **int**| Unique identifier of the holiday calendar slot to be updated | 

### Return type

[**HolidayCalendar**](HolidayCalendar.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

