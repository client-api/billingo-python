# clientapi_billingo.CurrencyApi

All URIs are relative to *https://api.billingo.hu/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_conversion_rate**](CurrencyApi.md#get_conversion_rate) | **GET** /currencies | Get currencies exchange rate.

# **get_conversion_rate**
> ConversationRate get_conversion_rate(_from, to, _date=_date)

Get currencies exchange rate.

Return with the exchange value of given currencies.

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
api_instance = clientapi_billingo.CurrencyApi(clientapi_billingo.ApiClient(configuration))
_from = clientapi_billingo.Currency() # Currency | 
to = clientapi_billingo.Currency() # Currency | 
_date = '2013-10-20' # date |  (optional)

try:
    # Get currencies exchange rate.
    api_response = api_instance.get_conversion_rate(_from, to, _date=_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrencyApi->get_conversion_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | [**Currency**](.md)|  | 
 **to** | [**Currency**](.md)|  | 
 **_date** | **date**|  | [optional] 

### Return type

[**ConversationRate**](ConversationRate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

