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
> Partner create_partner(partner)

Create a partner

Create a new partner. Returns a partner object if the create is succeded.

### Example

* Api Key Authentication (api_key):

```python
import clientapi_billingo
from clientapi_billingo.models.partner import Partner
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
    api_instance = clientapi_billingo.PartnerApi(api_client)
    partner = clientapi_billingo.Partner() # Partner | Partner object that you would like to store.

    try:
        # Create a partner
        api_response = api_instance.create_partner(partner)
        print("The response of PartnerApi->create_partner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerApi->create_partner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner** | [**Partner**](Partner.md)| Partner object that you would like to store. | 

### Return type

[**Partner**](Partner.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Partner created successfully. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**400** | The request is malformed. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**401** | Authorization information is missing or invalid. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**402** | Authenticated user doesn&#39;t have subscription. |  -  |
**403** | Authenticated user doesn&#39;t have access to the resource. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**422** | Validation errors occured. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**429** | Too many requests |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**500** | Internal server error. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_partner**
> delete_partner(id)

Delete a partner

Delete an existing partner.

### Example

* Api Key Authentication (api_key):

```python
import clientapi_billingo
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
    api_instance = clientapi_billingo.PartnerApi(api_client)
    id = 56 # int | 

    try:
        # Delete a partner
        api_instance.delete_partner(id)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Partner deleted successfully. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**400** | The request is malformed. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**401** | Authorization information is missing or invalid. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**402** | Authenticated user doesn&#39;t have subscription. |  -  |
**403** | Authenticated user doesn&#39;t have access to the resource. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**429** | Too many requests |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**500** | Internal server error. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**404** | Non-existent resource is requested. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_partner**
> Partner get_partner(id)

Retrieve a partner

Retrieves the details of an existing partner.

### Example

* Api Key Authentication (api_key):

```python
import clientapi_billingo
from clientapi_billingo.models.partner import Partner
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
    api_instance = clientapi_billingo.PartnerApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve a partner
        api_response = api_instance.get_partner(id)
        print("The response of PartnerApi->get_partner:\n")
        pprint(api_response)
    except Exception as e:
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

# **list_partner**
> PartnerList list_partner(page=page, per_page=per_page, query=query)

List all partners

Returns a list of your partners. The partners are returned sorted by creation date, with the most recent partners appearing first.

### Example

* Api Key Authentication (api_key):

```python
import clientapi_billingo
from clientapi_billingo.models.partner_list import PartnerList
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
    api_instance = clientapi_billingo.PartnerApi(api_client)
    page = 56 # int |  (optional)
    per_page = 25 # int |  (optional) (default to 25)
    query = 'query_example' # str |  (optional)

    try:
        # List all partners
        api_response = api_instance.list_partner(page=page, per_page=per_page, query=query)
        print("The response of PartnerApi->list_partner:\n")
        pprint(api_response)
    except Exception as e:
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

# **update_partner**
> Partner update_partner(id, partner)

Update a partner

Update an existing partner. Returns a partner object if the update is succeded.

### Example

* Api Key Authentication (api_key):

```python
import clientapi_billingo
from clientapi_billingo.models.partner import Partner
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
    api_instance = clientapi_billingo.PartnerApi(api_client)
    id = 56 # int | 
    partner = clientapi_billingo.Partner() # Partner | Partner object that you would like to update.

    try:
        # Update a partner
        api_response = api_instance.update_partner(id, partner)
        print("The response of PartnerApi->update_partner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartnerApi->update_partner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **partner** | [**Partner**](Partner.md)| Partner object that you would like to update. | 

### Return type

[**Partner**](Partner.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Partner updated successfully. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**400** | The request is malformed. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**401** | Authorization information is missing or invalid. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**402** | Authenticated user doesn&#39;t have subscription. |  -  |
**403** | Authenticated user doesn&#39;t have access to the resource. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**422** | Validation errors occured. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**429** | Too many requests |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**500** | Internal server error. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |
**404** | Non-existent resource is requested. |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  * Retry-After - How many seconds you have to wait before making new request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

