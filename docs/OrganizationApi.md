# clientapi_billingo.OrganizationApi

All URIs are relative to *https://api.billingo.hu/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_organization_data**](OrganizationApi.md#get_organization_data) | **GET** /organization | Retrieve a organization data.

# **get_organization_data**
> OrganizationData get_organization_data()

Retrieve a organization data.

Retrieves the data of organization.

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
api_instance = clientapi_billingo.OrganizationApi(clientapi_billingo.ApiClient(configuration))

try:
    # Retrieve a organization data.
    api_response = api_instance.get_organization_data()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->get_organization_data: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrganizationData**](OrganizationData.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

