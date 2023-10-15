# clientapi_billingo.PartnerApi

All URIs are relative to *https://api.billingo.hu/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_partner**](PartnerApi.md#create_partner) | **POST** /partners | Create a partner
[**delete_partner**](PartnerApi.md#delete_partner) | **DELETE** /partners/{id} | Delete a partner
[**get_partner**](PartnerApi.md#get_partner) | **GET** /partners/{id} | Retrieve a partner
[**list_partner**](PartnerApi.md#list_partner) | **GET** /partners | List all partners
[**update_partner**](PartnerApi.md#update_partner) | **PUT** /partners/{id} | Update a partner

# **create_partner**
> Partner create_partner(body)

Create a partner

Create a new partner. Returns a partner object if the create is succeded.

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
api_instance = clientapi_billingo.PartnerApi(clientapi_billingo.ApiClient(configuration))
body = clientapi_billingo.Partner() # Partner | Partner object that you would like to store.

try:
    # Create a partner
    api_response = api_instance.create_partner(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerApi->create_partner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Partner**](Partner.md)| Partner object that you would like to store. | 

### Return type

[**Partner**](Partner.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_partner**
> delete_partner(id)

Delete a partner

Delete an existing partner.

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
api_instance = clientapi_billingo.PartnerApi(clientapi_billingo.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete a partner
    api_instance.delete_partner(id)
except ApiException as e:
    print("Exception when calling PartnerApi->delete_partner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_partner**
> Partner get_partner(id)

Retrieve a partner

Retrieves the details of an existing partner.

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
api_instance = clientapi_billingo.PartnerApi(clientapi_billingo.ApiClient(configuration))
id = 56 # int | 

try:
    # Retrieve a partner
    api_response = api_instance.get_partner(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerApi->get_partner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Partner**](Partner.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_partner**
> PartnerList list_partner(page=page, per_page=per_page, query=query)

List all partners

Returns a list of your partners. The partners are returned sorted by creation date, with the most recent partners appearing first.

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
api_instance = clientapi_billingo.PartnerApi(clientapi_billingo.ApiClient(configuration))
page = 56 # int |  (optional)
per_page = 25 # int |  (optional) (default to 25)
query = 'query_example' # str |  (optional)

try:
    # List all partners
    api_response = api_instance.list_partner(page=page, per_page=per_page, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerApi->list_partner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] [default to 25]
 **query** | **str**|  | [optional] 

### Return type

[**PartnerList**](PartnerList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_partner**
> Partner update_partner(body, id)

Update a partner

Update an existing partner. Returns a partner object if the update is succeded.

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
api_instance = clientapi_billingo.PartnerApi(clientapi_billingo.ApiClient(configuration))
body = clientapi_billingo.Partner() # Partner | Partner object that you would like to update.
id = 56 # int | 

try:
    # Update a partner
    api_response = api_instance.update_partner(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnerApi->update_partner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Partner**](Partner.md)| Partner object that you would like to update. | 
 **id** | **int**|  | 

### Return type

[**Partner**](Partner.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

