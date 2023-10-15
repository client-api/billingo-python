# clientapi_billingo.BankAccountApi

All URIs are relative to *https://api.billingo.hu/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bank_account**](BankAccountApi.md#create_bank_account) | **POST** /bank-accounts | Create a bank account
[**delete_bank_account**](BankAccountApi.md#delete_bank_account) | **DELETE** /bank-accounts/{id} | Delete a bank account
[**get_bank_account**](BankAccountApi.md#get_bank_account) | **GET** /bank-accounts/{id} | Retrieve a bank account
[**list_bank_account**](BankAccountApi.md#list_bank_account) | **GET** /bank-accounts | List all bank account
[**update_bank_account**](BankAccountApi.md#update_bank_account) | **PUT** /bank-accounts/{id} | Update a bank account

# **create_bank_account**
> BankAccount create_bank_account(body)

Create a bank account

Create a new bank account. Returns a bank account object if the create is succeded.

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
api_instance = clientapi_billingo.BankAccountApi(clientapi_billingo.ApiClient(configuration))
body = clientapi_billingo.BankAccount() # BankAccount | BankAccount object that you would like to store.

try:
    # Create a bank account
    api_response = api_instance.create_bank_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountApi->create_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BankAccount**](BankAccount.md)| BankAccount object that you would like to store. | 

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bank_account**
> delete_bank_account(id)

Delete a bank account

Delete an existing bank account.

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
api_instance = clientapi_billingo.BankAccountApi(clientapi_billingo.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete a bank account
    api_instance.delete_bank_account(id)
except ApiException as e:
    print("Exception when calling BankAccountApi->delete_bank_account: %s\n" % e)
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

# **get_bank_account**
> BankAccount get_bank_account(id)

Retrieve a bank account

Retrieves the details of an existing bank account.

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
api_instance = clientapi_billingo.BankAccountApi(clientapi_billingo.ApiClient(configuration))
id = 56 # int | 

try:
    # Retrieve a bank account
    api_response = api_instance.get_bank_account(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountApi->get_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bank_account**
> BankAccountList list_bank_account(page=page, per_page=per_page)

List all bank account

Returns a list of your bank accounts. The bank accounts are returned sorted by creation date, with the most recent bank account appearing first.

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
api_instance = clientapi_billingo.BankAccountApi(clientapi_billingo.ApiClient(configuration))
page = 56 # int |  (optional)
per_page = 25 # int |  (optional) (default to 25)

try:
    # List all bank account
    api_response = api_instance.list_bank_account(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountApi->list_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] [default to 25]

### Return type

[**BankAccountList**](BankAccountList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bank_account**
> BankAccount update_bank_account(body, id)

Update a bank account

Update an existing bank accounts. Returns a bank account object if the update is succeded.

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
api_instance = clientapi_billingo.BankAccountApi(clientapi_billingo.ApiClient(configuration))
body = clientapi_billingo.BankAccount() # BankAccount | Bank account object that you would like to update.
id = 56 # int | 

try:
    # Update a bank account
    api_response = api_instance.update_bank_account(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountApi->update_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BankAccount**](BankAccount.md)| Bank account object that you would like to update. | 
 **id** | **int**|  | 

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

