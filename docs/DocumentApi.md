# clientapi_billingo.DocumentApi

All URIs are relative to *https://api.billingo.hu/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_document**](DocumentApi.md#archive_document) | **PUT** /documents/{id}/archive | Archive a proforma document.
[**cancel_document**](DocumentApi.md#cancel_document) | **POST** /documents/{id}/cancel | Cancel a document
[**create_document**](DocumentApi.md#create_document) | **POST** /documents | Create a document
[**create_document_from_draft**](DocumentApi.md#create_document_from_draft) | **PUT** /documents/{id} | Converts a draft to an invoice.
[**create_document_from_proforma**](DocumentApi.md#create_document_from_proforma) | **POST** /documents/{id}/create-from-proforma | Create a document from proforma.
[**create_modification_document**](DocumentApi.md#create_modification_document) | **POST** /documents/{id}/create-modification-document | Create a modification document.
[**create_receipt**](DocumentApi.md#create_receipt) | **POST** /documents/receipt | Create a receipt
[**create_receipt_from_draft**](DocumentApi.md#create_receipt_from_draft) | **PUT** /documents/receipt/{id} | Converts a draft to a receipt.
[**delete_document**](DocumentApi.md#delete_document) | **DELETE** /documents/{id} | Delete a draft.
[**delete_payment**](DocumentApi.md#delete_payment) | **DELETE** /documents/{id}/payments | Delete all payment history on document
[**document_copy**](DocumentApi.md#document_copy) | **POST** /documents/{id}/copy | Copy a document
[**download_document**](DocumentApi.md#download_document) | **GET** /documents/{id}/download | Download a document in PDF format.
[**get_document**](DocumentApi.md#get_document) | **GET** /documents/{id} | Retrieve a document
[**get_document_by_vendor_id**](DocumentApi.md#get_document_by_vendor_id) | **GET** /documents/vendor/{vendor_id} | Retrieve a document by vendor id
[**get_online_szamla_status**](DocumentApi.md#get_online_szamla_status) | **GET** /documents/{id}/online-szamla | Retrieve a document Online Számla status
[**get_payment**](DocumentApi.md#get_payment) | **GET** /documents/{id}/payments | Retrieve a payment histroy
[**get_public_url**](DocumentApi.md#get_public_url) | **GET** /documents/{id}/public-url | Retrieve a document download public url.
[**list_document**](DocumentApi.md#list_document) | **GET** /documents | List all documents
[**pos_print**](DocumentApi.md#pos_print) | **GET** /documents/{id}/print/pos | Returns a printable POS PDF
[**send_document**](DocumentApi.md#send_document) | **POST** /documents/{id}/send | Send invoice to given email adresses.
[**update_payment**](DocumentApi.md#update_payment) | **PUT** /documents/{id}/payments | Update payment history

# **archive_document**
> archive_document(id)

Archive a proforma document.

Archive an existing proforma document.

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
api_instance = clientapi_billingo.DocumentApi(clientapi_billingo.ApiClient(configuration))
id = 56 # int | 

try:
    # Archive a proforma document.
    api_instance.archive_document(id)
except ApiException as e:
    print("Exception when calling DocumentApi->archive_document: %s\n" % e)
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

# **cancel_document**
> Document cancel_document(id, body=body)

Cancel a document

Cancel a document. Returns a cancellation document object if the cancellation is succeded.

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
api_instance = clientapi_billingo.DocumentApi(clientapi_billingo.ApiClient(configuration))
id = 56 # int | 
body = clientapi_billingo.DocumentCancellation() # DocumentCancellation | Comment and notifiable email addresses - comma separated for multiple email addresses (optional)

try:
    # Cancel a document
    api_response = api_instance.cancel_document(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->cancel_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**DocumentCancellation**](DocumentCancellation.md)| Comment and notifiable email addresses - comma separated for multiple email addresses | [optional] 

### Return type

[**Document**](Document.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_document**
> Document create_document(body)

Create a document

Create a new document. Returns a document object if the create is succeded.

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
api_instance = clientapi_billingo.DocumentApi(clientapi_billingo.ApiClient(configuration))
body = clientapi_billingo.DocumentInsert() # DocumentInsert | DocumentInsert object that you would like to store.

try:
    # Create a document
    api_response = api_instance.create_document(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->create_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentInsert**](DocumentInsert.md)| DocumentInsert object that you would like to store. | 

### Return type

[**Document**](Document.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_document_from_draft**
> Document create_document_from_draft(body, id)

Converts a draft to an invoice.

Converts a draft to an invoice. Returns the invoice object if the convert is succeded.

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
api_instance = clientapi_billingo.DocumentApi(clientapi_billingo.ApiClient(configuration))
body = clientapi_billingo.DocumentInsert() # DocumentInsert | DocumentInsert object that you would like to store.
id = 56 # int | 

try:
    # Converts a draft to an invoice.
    api_response = api_instance.create_document_from_draft(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->create_document_from_draft: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentInsert**](DocumentInsert.md)| DocumentInsert object that you would like to store. | 
 **id** | **int**|  | 

### Return type

[**Document**](Document.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_document_from_proforma**
> Document create_document_from_proforma(id, body=body)

Create a document from proforma.

Create a new document from proforma. Returns a document object if the create is succeded.

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
api_instance = clientapi_billingo.DocumentApi(clientapi_billingo.ApiClient(configuration))
id = 56 # int | 
body = clientapi_billingo.InvoiceSettings() # InvoiceSettings | InvoiceSettings object. (optional)

try:
    # Create a document from proforma.
    api_response = api_instance.create_document_from_proforma(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->create_document_from_proforma: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**InvoiceSettings**](InvoiceSettings.md)| InvoiceSettings object. | [optional] 

### Return type

[**Document**](Document.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_modification_document**
> Document create_modification_document(body, id)

Create a modification document.

Create a modification document for the given document. Returns a new document object if the create is successful.

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
api_instance = clientapi_billingo.DocumentApi(clientapi_billingo.ApiClient(configuration))
body = clientapi_billingo.ModificationDocumentInsert() # ModificationDocumentInsert | ModificationDocumentInsert object that you would like to store.
id = 56 # int | 

try:
    # Create a modification document.
    api_response = api_instance.create_modification_document(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->create_modification_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModificationDocumentInsert**](ModificationDocumentInsert.md)| ModificationDocumentInsert object that you would like to store. | 
 **id** | **int**|  | 

### Return type

[**Document**](Document.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_receipt**
> Document create_receipt(body)

Create a receipt

Create a new receipt. Returns a document object if the create is succeded.

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
api_instance = clientapi_billingo.DocumentApi(clientapi_billingo.ApiClient(configuration))
body = clientapi_billingo.ReceiptInsert() # ReceiptInsert | ReceiptInsert object that you would like to store.

try:
    # Create a receipt
    api_response = api_instance.create_receipt(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->create_receipt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReceiptInsert**](ReceiptInsert.md)| ReceiptInsert object that you would like to store. | 

### Return type

[**Document**](Document.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_receipt_from_draft**
> Document create_receipt_from_draft(body, id)

Converts a draft to a receipt.

Converts a draft to a receipt. Returns the receipt object if the convert is succeded.

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
api_instance = clientapi_billingo.DocumentApi(clientapi_billingo.ApiClient(configuration))
body = clientapi_billingo.ReceiptInsert() # ReceiptInsert | ReceiptInsert object that you would like to store.
id = 56 # int | 

try:
    # Converts a draft to a receipt.
    api_response = api_instance.create_receipt_from_draft(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->create_receipt_from_draft: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReceiptInsert**](ReceiptInsert.md)| ReceiptInsert object that you would like to store. | 
 **id** | **int**|  | 

### Return type

[**Document**](Document.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document**
> delete_document(id)

Delete a draft.

Delete an existing draft.

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
api_instance = clientapi_billingo.DocumentApi(clientapi_billingo.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete a draft.
    api_instance.delete_document(id)
except ApiException as e:
    print("Exception when calling DocumentApi->delete_document: %s\n" % e)
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

# **delete_payment**
> list[PaymentHistory] delete_payment(id)

Delete all payment history on document

Delete all exist payment history on document.

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
api_instance = clientapi_billingo.DocumentApi(clientapi_billingo.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete all payment history on document
    api_response = api_instance.delete_payment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->delete_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**list[PaymentHistory]**](PaymentHistory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_copy**
> Document document_copy(id)

Copy a document

Copy a document. Returns the new document if the copy was succeded.

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
api_instance = clientapi_billingo.DocumentApi(clientapi_billingo.ApiClient(configuration))
id = 56 # int | 

try:
    # Copy a document
    api_response = api_instance.document_copy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->document_copy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Document**](Document.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_document**
> str download_document(id)

Download a document in PDF format.

Download a document. Returns a document in PDF format.

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
api_instance = clientapi_billingo.DocumentApi(clientapi_billingo.ApiClient(configuration))
id = 56 # int | 

try:
    # Download a document in PDF format.
    api_response = api_instance.download_document(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->download_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> Document get_document(id)

Retrieve a document

Retrieves the details of an existing document.

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
api_instance = clientapi_billingo.DocumentApi(clientapi_billingo.ApiClient(configuration))
id = 56 # int | 

try:
    # Retrieve a document
    api_response = api_instance.get_document(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->get_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Document**](Document.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_by_vendor_id**
> Document get_document_by_vendor_id(vendor_id)

Retrieve a document by vendor id

Retrieves the details of an existing document by vendor id.

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
api_instance = clientapi_billingo.DocumentApi(clientapi_billingo.ApiClient(configuration))
vendor_id = 'vendor_id_example' # str | 

try:
    # Retrieve a document by vendor id
    api_response = api_instance.get_document_by_vendor_id(vendor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->get_document_by_vendor_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **str**|  | 

### Return type

[**Document**](Document.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_online_szamla_status**
> OnlineSzamlaStatus get_online_szamla_status(id)

Retrieve a document Online Számla status

Retrieves the details of an existing document status.

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
api_instance = clientapi_billingo.DocumentApi(clientapi_billingo.ApiClient(configuration))
id = 56 # int | 

try:
    # Retrieve a document Online Számla status
    api_response = api_instance.get_online_szamla_status(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->get_online_szamla_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**OnlineSzamlaStatus**](OnlineSzamlaStatus.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment**
> list[PaymentHistory] get_payment(id)

Retrieve a payment histroy

Retrieves the details of payment history an existing document.

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
api_instance = clientapi_billingo.DocumentApi(clientapi_billingo.ApiClient(configuration))
id = 56 # int | 

try:
    # Retrieve a payment histroy
    api_response = api_instance.get_payment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->get_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**list[PaymentHistory]**](PaymentHistory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_url**
> DocumentPublicUrl get_public_url(id)

Retrieve a document download public url.

Retrieves public url to download an existing document.

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
api_instance = clientapi_billingo.DocumentApi(clientapi_billingo.ApiClient(configuration))
id = 56 # int | 

try:
    # Retrieve a document download public url.
    api_response = api_instance.get_public_url(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->get_public_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**DocumentPublicUrl**](DocumentPublicUrl.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_document**
> DocumentList list_document(page=page, per_page=per_page, block_id=block_id, partner_id=partner_id, payment_method=payment_method, payment_status=payment_status, start_date=start_date, end_date=end_date, start_number=start_number, end_number=end_number, start_year=start_year, end_year=end_year, type=type, query=query, paid_start_date=paid_start_date, paid_end_date=paid_end_date, fulfillment_start_date=fulfillment_start_date, fulfillment_end_date=fulfillment_end_date, last_modified_date=last_modified_date)

List all documents

Returns a list of your documents. The documents are returned sorted by creation date, with the most recent documents appearing first.

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
api_instance = clientapi_billingo.DocumentApi(clientapi_billingo.ApiClient(configuration))
page = 56 # int |  (optional)
per_page = 25 # int |  (optional) (default to 25)
block_id = 56 # int | Filter documents by the identifier of your DocumentBlock. (optional)
partner_id = 56 # int | Filter documents by the identifier of your Partner. (optional)
payment_method = clientapi_billingo.PaymentMethod() # PaymentMethod | Filter documents by PaymentMethod value. (optional)
payment_status = clientapi_billingo.PaymentStatus() # PaymentStatus | Filter documents by PaymentStatus value. (optional)
start_date = '2013-10-20' # date | Filter documents by their invoice date. (optional)
end_date = '2013-10-20' # date | Filter documents by their invoice date. (optional)
start_number = 56 # int | Starting number of the document, should not contain year or any other formatting. Required if `start_year` given (optional)
end_number = 56 # int | Ending number of the document, should not contain year or any other formatting. Required if `end_year` given (optional)
start_year = 56 # int | Year for `start_number` parameter. Required if `start_number` given. (optional)
end_year = 56 # int | Year for `end_number` parameter. Required if `end_number` given. (optional)
type = clientapi_billingo.DocumentType() # DocumentType | Filter documents by type (optional)
query = 'query_example' # str | Filter documents by the given text (optional)
paid_start_date = '2013-10-20' # date | Filter documents by their payment date. (optional)
paid_end_date = '2013-10-20' # date | Filter documents by their payment date. (optional)
fulfillment_start_date = '2013-10-20' # date | Filter documents by their fulfillment date. (optional)
fulfillment_end_date = '2013-10-20' # date | Filter documents by their fulfillment date. (optional)
last_modified_date = 'last_modified_date_example' # str | Filter documents by their last modified date. (optional)

try:
    # List all documents
    api_response = api_instance.list_document(page=page, per_page=per_page, block_id=block_id, partner_id=partner_id, payment_method=payment_method, payment_status=payment_status, start_date=start_date, end_date=end_date, start_number=start_number, end_number=end_number, start_year=start_year, end_year=end_year, type=type, query=query, paid_start_date=paid_start_date, paid_end_date=paid_end_date, fulfillment_start_date=fulfillment_start_date, fulfillment_end_date=fulfillment_end_date, last_modified_date=last_modified_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->list_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] [default to 25]
 **block_id** | **int**| Filter documents by the identifier of your DocumentBlock. | [optional] 
 **partner_id** | **int**| Filter documents by the identifier of your Partner. | [optional] 
 **payment_method** | [**PaymentMethod**](.md)| Filter documents by PaymentMethod value. | [optional] 
 **payment_status** | [**PaymentStatus**](.md)| Filter documents by PaymentStatus value. | [optional] 
 **start_date** | **date**| Filter documents by their invoice date. | [optional] 
 **end_date** | **date**| Filter documents by their invoice date. | [optional] 
 **start_number** | **int**| Starting number of the document, should not contain year or any other formatting. Required if &#x60;start_year&#x60; given | [optional] 
 **end_number** | **int**| Ending number of the document, should not contain year or any other formatting. Required if &#x60;end_year&#x60; given | [optional] 
 **start_year** | **int**| Year for &#x60;start_number&#x60; parameter. Required if &#x60;start_number&#x60; given. | [optional] 
 **end_year** | **int**| Year for &#x60;end_number&#x60; parameter. Required if &#x60;end_number&#x60; given. | [optional] 
 **type** | [**DocumentType**](.md)| Filter documents by type | [optional] 
 **query** | **str**| Filter documents by the given text | [optional] 
 **paid_start_date** | **date**| Filter documents by their payment date. | [optional] 
 **paid_end_date** | **date**| Filter documents by their payment date. | [optional] 
 **fulfillment_start_date** | **date**| Filter documents by their fulfillment date. | [optional] 
 **fulfillment_end_date** | **date**| Filter documents by their fulfillment date. | [optional] 
 **last_modified_date** | **str**| Filter documents by their last modified date. | [optional] 

### Return type

[**DocumentList**](DocumentList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pos_print**
> str pos_print(id, size)

Returns a printable POS PDF

Returns a printable POS PDF file of a particular document.

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
api_instance = clientapi_billingo.DocumentApi(clientapi_billingo.ApiClient(configuration))
id = 56 # int | 
size = 1.2 # float | In which size the POS PDF should be rendered.

try:
    # Returns a printable POS PDF
    api_response = api_instance.pos_print(id, size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->pos_print: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **size** | **float**| In which size the POS PDF should be rendered. | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_document**
> SendDocument send_document(id, body=body)

Send invoice to given email adresses.

Returns a list of emails, where the invoice is sent.

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
api_instance = clientapi_billingo.DocumentApi(clientapi_billingo.ApiClient(configuration))
id = 56 # int | 
body = clientapi_billingo.SendDocument() # SendDocument | List of email-s where you want to send the invoice. (optional)

try:
    # Send invoice to given email adresses.
    api_response = api_instance.send_document(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->send_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**SendDocument**](SendDocument.md)| List of email-s where you want to send the invoice. | [optional] 

### Return type

[**SendDocument**](SendDocument.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment**
> list[PaymentHistory] update_payment(body, id)

Update payment history

Update payment history an existing document. Returns a payment history object if the update is succeded.

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
api_instance = clientapi_billingo.DocumentApi(clientapi_billingo.ApiClient(configuration))
body = [clientapi_billingo.PaymentHistory()] # list[PaymentHistory] | Payment history object that you would like to update.
id = 56 # int | 

try:
    # Update payment history
    api_response = api_instance.update_payment(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->update_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[PaymentHistory]**](PaymentHistory.md)| Payment history object that you would like to update. | 
 **id** | **int**|  | 

### Return type

[**list[PaymentHistory]**](PaymentHistory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

