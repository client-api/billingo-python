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

* Api Key Authentication (api_key):

```python
import clientapi_billingo
from clientapi_billingo.models.tax_number import TaxNumber
from clientapi_billingo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.billingo.hu/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = clientapi_billingo.Configuration(
    host = "https://api.billingo.hu/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with clientapi_billingo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_billingo.UtilApi(api_client)
    tax_number = 'tax_number_example' # str | 

    try:
        # Check tax number.
        api_response = api_instance.check_tax_number(tax_number)
        print("The response of UtilApi->check_tax_number:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**400** | The request is malformed. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**401** | Authorization information is missing or invalid. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**402** | Authenticated user doesn&#39;t have subscription. |  -  |
**422** | Validation errors occured. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**429** | Too many requests |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**500** | Internal server error. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_id**
> Id get_id(id)

Convert legacy ID to v3 ID.

Retrieves the API v3 ID.

### Example

* Api Key Authentication (api_key):

```python
import clientapi_billingo
from clientapi_billingo.models.id import Id
from clientapi_billingo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.billingo.hu/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = clientapi_billingo.Configuration(
    host = "https://api.billingo.hu/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with clientapi_billingo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_billingo.UtilApi(api_client)
    id = 56 # int | 

    try:
        # Convert legacy ID to v3 ID.
        api_response = api_instance.get_id(id)
        print("The response of UtilApi->get_id:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**400** | The request is malformed. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**401** | Authorization information is missing or invalid. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**402** | Authenticated user doesn&#39;t have subscription. |  -  |
**422** | Validation errors occured. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**429** | Too many requests |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**500** | Internal server error. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**404** | Non-existent resource is requested. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_time**
> ServerTime get_server_time()

Get the server time

Return the server time.

### Example

* Api Key Authentication (api_key):

```python
import clientapi_billingo
from clientapi_billingo.models.server_time import ServerTime
from clientapi_billingo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.billingo.hu/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = clientapi_billingo.Configuration(
    host = "https://api.billingo.hu/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with clientapi_billingo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_billingo.UtilApi(api_client)

    try:
        # Get the server time
        api_response = api_instance.get_server_time()
        print("The response of UtilApi->get_server_time:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**400** | The request is malformed. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**401** | Authorization information is missing or invalid. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**402** | Authenticated user doesn&#39;t have subscription. |  -  |
**422** | Validation errors occured. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**429** | Too many requests |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**500** | Internal server error. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

