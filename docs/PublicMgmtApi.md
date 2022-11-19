# airkey.PublicMgmtApi

All URIs are relative to *https://integration.api.airkey.evva.com:443/cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reset_test_data**](PublicMgmtApi.md#reset_test_data) | **POST** /v1/public-mgmt/reset-test-data | Resets test data in the integration environment.

# **reset_test_data**
> reset_test_data()

Resets test data in the integration environment.

Resets the test data for the customer generated in the integration environment.

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
api_instance = airkey.PublicMgmtApi(airkey.ApiClient(configuration))

try:
    # Resets test data in the integration environment.
    api_instance.reset_test_data()
except ApiException as e:
    print("Exception when calling PublicMgmtApi->reset_test_data: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[X-API-Key](../README.md#X-API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

