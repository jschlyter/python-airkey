# airkey.SendAKeyApi

All URIs are relative to *https://integration.api.airkey.evva.com:443/cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_a_key**](SendAKeyApi.md#send_a_key) | **POST** /v1/send-a-key | Sends a registration code to the phone and creates all necessary prerequisites if needed.

# **send_a_key**
> SendAKeyResponse send_a_key(body)

Sends a registration code to the phone and creates all necessary prerequisites if needed.

Based on the given phone number this request sends a registration link via SMS for easy installation of the AirKey app. It simplifies the task of creating new mobile app users by implicitly creating new persons, phones and authorizations of type 'SIMPLE' if needed, i.e. it reuses an existing person if found. Please check before if a phone already exists with the given phone number to prevent duplicates (GET /media/phones using the filter phoneNumber). The reason why duplicates are allowed is to be able to create a new phone with an already existing phone number so it is not mandatory to delete an old phone before creating the new phone with the same phone number. <br/>Authorization creation mirrors the behaviour of POST /authorizations/simple. If you need more control consider creating a phone and person with this call and using the advanced authorization interface for creating authorizations. <br/>Either lockId or areaId needs to be set for an authorization. It's not possible to set both IDs at the same time.

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
api_instance = airkey.SendAKeyApi(airkey.ApiClient(configuration))
body = airkey.SendAKeyRequest() # SendAKeyRequest | Send-A-Key request wrapper

try:
    # Sends a registration code to the phone and creates all necessary prerequisites if needed.
    api_response = api_instance.send_a_key(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SendAKeyApi->send_a_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SendAKeyRequest**](SendAKeyRequest.md)| Send-A-Key request wrapper | 

### Return type

[**SendAKeyResponse**](SendAKeyResponse.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

