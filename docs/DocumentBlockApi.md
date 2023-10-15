# clientapi_billingo.DocumentBlockApi

All URIs are relative to *https://api.billingo.hu/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_document_block**](DocumentBlockApi.md#list_document_block) | **GET** /document-blocks | List all document blocks

# **list_document_block**
> DocumentBlockList list_document_block(page=page, per_page=per_page, type=type)

List all document blocks

Returns a list of your document blocks. The document blocks are returned sorted by creation date, with the most recent document blocks appearing first.

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
api_instance = clientapi_billingo.DocumentBlockApi(clientapi_billingo.ApiClient(configuration))
page = 56 # int |  (optional)
per_page = 25 # int |  (optional) (default to 25)
type = clientapi_billingo.DocumentBlockType() # DocumentBlockType | Filter document blocks by type (optional)

try:
    # List all document blocks
    api_response = api_instance.list_document_block(page=page, per_page=per_page, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentBlockApi->list_document_block: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] [default to 25]
 **type** | [**DocumentBlockType**](.md)| Filter document blocks by type | [optional] 

### Return type

[**DocumentBlockList**](DocumentBlockList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

