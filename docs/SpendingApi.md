# clientapi_billingo.SpendingApi

All URIs are relative to *https://api.billingo.hu/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spending_delete**](SpendingApi.md#spending_delete) | **DELETE** /spendings/{id} | Deletes a spending.
[**spending_list**](SpendingApi.md#spending_list) | **GET** /spendings | Lists all spending
[**spending_save**](SpendingApi.md#spending_save) | **POST** /spendings | Creates a new spending.
[**spending_show**](SpendingApi.md#spending_show) | **GET** /spendings/{id} | Retrieves one specific spending.
[**spending_update**](SpendingApi.md#spending_update) | **PUT** /spendings/{id} | Updates a spending item.

# **spending_delete**
> spending_delete(id)

Deletes a spending.

Deletes the spending identified by the ID given in path.

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
api_instance = clientapi_billingo.SpendingApi(clientapi_billingo.ApiClient(configuration))
id = 56 # int | 

try:
    # Deletes a spending.
    api_instance.spending_delete(id)
except ApiException as e:
    print("Exception when calling SpendingApi->spending_delete: %s\n" % e)
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

# **spending_list**
> SpendingList spending_list(q=q, page=page, per_page=per_page, spending_date=spending_date, start_date=start_date, end_date=end_date, payment_status=payment_status, spending_type=spending_type, categories=categories, currencies=currencies, payment_methods=payment_methods)

Lists all spending

Returns a list of your spending items, ordered by the due date.

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
api_instance = clientapi_billingo.SpendingApi(clientapi_billingo.ApiClient(configuration))
q = '' # str |  (optional)
page = 1 # int |  (optional) (default to 1)
per_page = 25 # int |  (optional) (default to 25)
spending_date = clientapi_billingo.DateType() # DateType |  (optional)
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
payment_status = clientapi_billingo.PaymentStatusSpending() # PaymentStatusSpending |  (optional)
spending_type = clientapi_billingo.Source() # Source |  (optional)
categories = clientapi_billingo.Category() # Category |  (optional)
currencies = clientapi_billingo.Currency() # Currency |  (optional)
payment_methods = clientapi_billingo.PaymentMethod() # PaymentMethod |  (optional)

try:
    # Lists all spending
    api_response = api_instance.spending_list(q=q, page=page, per_page=per_page, spending_date=spending_date, start_date=start_date, end_date=end_date, payment_status=payment_status, spending_type=spending_type, categories=categories, currencies=currencies, payment_methods=payment_methods)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpendingApi->spending_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 25]
 **spending_date** | [**DateType**](.md)|  | [optional] 
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **payment_status** | [**PaymentStatusSpending**](.md)|  | [optional] 
 **spending_type** | [**Source**](.md)|  | [optional] 
 **categories** | [**Category**](.md)|  | [optional] 
 **currencies** | [**Currency**](.md)|  | [optional] 
 **payment_methods** | [**PaymentMethod**](.md)|  | [optional] 

### Return type

[**SpendingList**](SpendingList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spending_save**
> Spending spending_save(body=body)

Creates a new spending.

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
api_instance = clientapi_billingo.SpendingApi(clientapi_billingo.ApiClient(configuration))
body = clientapi_billingo.SpendingSave() # SpendingSave |  (optional)

try:
    # Creates a new spending.
    api_response = api_instance.spending_save(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpendingApi->spending_save: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpendingSave**](SpendingSave.md)|  | [optional] 

### Return type

[**Spending**](Spending.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spending_show**
> Spending spending_show(id)

Retrieves one specific spending.

Retrives the spending identified by the given ID in path.

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
api_instance = clientapi_billingo.SpendingApi(clientapi_billingo.ApiClient(configuration))
id = 56 # int | 

try:
    # Retrieves one specific spending.
    api_response = api_instance.spending_show(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpendingApi->spending_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Spending**](Spending.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spending_update**
> Spending spending_update(id, body=body)

Updates a spending item.

Updates the spending item identified by the ID given in path.

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
api_instance = clientapi_billingo.SpendingApi(clientapi_billingo.ApiClient(configuration))
id = 56 # int | 
body = clientapi_billingo.SpendingSave() # SpendingSave |  (optional)

try:
    # Updates a spending item.
    api_response = api_instance.spending_update(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpendingApi->spending_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**SpendingSave**](SpendingSave.md)|  | [optional] 

### Return type

[**Spending**](Spending.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

