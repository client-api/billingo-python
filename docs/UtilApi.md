# clientapi_billingo.UtilApi

All URIs are relative to *https://api.billingo.hu/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_tax_number**](UtilApi.md#check_tax_number) | **GET** /utils/check-tax-number/{tax_number} | Check tax number.
[**get_id**](UtilApi.md#get_id) | **GET** /utils/convert-legacy-id/{id} | Convert legacy ID to v3 ID.
[**get_server_time**](UtilApi.md#get_server_time) | **GET** /utils/time | Get the server time

# **check_tax_number**
> TaxNumber check_tax_number(tax_number)

Check tax number.

Check the given tax number format, and NAV validate.

### Example
```python
from __future__ import print_function
import time
import clientapi_billingo
from clientapi_billingo.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = clientapi_billingo.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = clientapi_billingo.UtilApi(clientapi_billingo.ApiClient(configuration))
tax_number = 'tax_number_example' # str | 

try:
    # Check tax number.
    api_response = api_instance.check_tax_number(tax_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilApi->check_tax_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_number** | **str**|  | 

### Return type

[**TaxNumber**](TaxNumber.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_id**
> Id get_id(id)

Convert legacy ID to v3 ID.

Retrieves the API v3 ID.

### Example
```python
from __future__ import print_function
import time
import clientapi_billingo
from clientapi_billingo.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = clientapi_billingo.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = clientapi_billingo.UtilApi(clientapi_billingo.ApiClient(configuration))
id = 56 # int | 

try:
    # Convert legacy ID to v3 ID.
    api_response = api_instance.get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilApi->get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Id**](Id.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_time**
> ServerTime get_server_time()

Get the server time

Return the server time.

### Example
```python
from __future__ import print_function
import time
import clientapi_billingo
from clientapi_billingo.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = clientapi_billingo.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = clientapi_billingo.UtilApi(clientapi_billingo.ApiClient(configuration))

try:
    # Get the server time
    api_response = api_instance.get_server_time()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilApi->get_server_time: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServerTime**](ServerTime.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

