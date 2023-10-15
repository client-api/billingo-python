# clientapi_billingo.DocumentExportApi

All URIs are relative to *https://api.billingo.hu/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](DocumentExportApi.md#create) | **POST** /document-export | Create document export.
[**download**](DocumentExportApi.md#download) | **GET** /document-export/{id}/download | Return exported binary file.
[**poll**](DocumentExportApi.md#poll) | **GET** /document-export/{id}/poll | Retrieve export state.

# **create**
> DocumentExportId create(body)

Create document export.

Return with the id of the export.

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
api_instance = clientapi_billingo.DocumentExportApi(clientapi_billingo.ApiClient(configuration))
body = clientapi_billingo.CreateDocumentExport() # CreateDocumentExport | Create document export body.

try:
    # Create document export.
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentExportApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDocumentExport**](CreateDocumentExport.md)| Create document export body. | 

### Return type

[**DocumentExportId**](DocumentExportId.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download**
> str download(id)

Return exported binary file.

Return the exported file.

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
api_instance = clientapi_billingo.DocumentExportApi(clientapi_billingo.ApiClient(configuration))
id = 'id_example' # str | The ID from create document export endpoint.

try:
    # Return exported binary file.
    api_response = api_instance.download(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentExportApi->download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID from create document export endpoint. | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/*, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poll**
> DocumentExportStatus poll(id)

Retrieve export state.

Return state of the given export.

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
api_instance = clientapi_billingo.DocumentExportApi(clientapi_billingo.ApiClient(configuration))
id = 'id_example' # str | The ID from create document export endpoint.

try:
    # Retrieve export state.
    api_response = api_instance.poll(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentExportApi->poll: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID from create document export endpoint. | 

### Return type

[**DocumentExportStatus**](DocumentExportStatus.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

