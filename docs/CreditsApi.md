# airkey.CreditsApi

All URIs are relative to *https://integration.api.airkey.evva.com:443/cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_credits**](CreditsApi.md#get_credits) | **GET** /v1/credits | Gets available credit information.

# **get_credits**
> CreditInfo get_credits()

Gets available credit information.

Returns information about available credits of customer.

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
api_instance = airkey.CreditsApi(airkey.ApiClient(configuration))

try:
    # Gets available credit information.
    api_response = api_instance.get_credits()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditsApi->get_credits: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CreditInfo**](CreditInfo.md)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

