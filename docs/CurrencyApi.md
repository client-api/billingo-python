# clientapi_billingo.CurrencyApi

All URIs are relative to *https://api.billingo.hu/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_conversion_rate**](CurrencyApi.md#get_conversion_rate) | **GET** /currencies | Get currencies exchange rate.


# **get_conversion_rate**
> ConversationRate get_conversion_rate(var_from, to, var_date=var_date)

Get currencies exchange rate.

Return with the exchange value of given currencies.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import clientapi_billingo
from clientapi_billingo.models.conversation_rate import ConversationRate
from clientapi_billingo.models.currency import Currency
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
    api_instance = clientapi_billingo.CurrencyApi(api_client)
    var_from = clientapi_billingo.Currency() # Currency | 
    to = clientapi_billingo.Currency() # Currency | 
    var_date = '2013-10-20' # date |  (optional)

    try:
        # Get currencies exchange rate.
        api_response = api_instance.get_conversion_rate(var_from, to, var_date=var_date)
        print("The response of CurrencyApi->get_conversion_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyApi->get_conversion_rate: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | [**Currency**](.md)|  | 
 **to** | [**Currency**](.md)|  | 
 **var_date** | **date**|  | [optional] 

### Return type

[**ConversationRate**](ConversationRate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Currencies exchange rate returned. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**400** | The request is malformed. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**401** | Authorization information is missing or invalid. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**402** | Authenticated user doesn&#39;t have subscription. |  -  |
**422** | Validation errors occured. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**429** | Too many requests |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**500** | Internal server error. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

