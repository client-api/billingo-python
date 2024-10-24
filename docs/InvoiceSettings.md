# InvoiceSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_type** | [**DocumentType**](DocumentType.md) |  | [optional] 
**fulfillment_date** | **date** |  | [optional] 
**due_date** | **date** |  | [optional] 
**document_format** | [**DocumentFormat**](DocumentFormat.md) |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from clientapi_billingo.models.invoice_settings import InvoiceSettings

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceSettings from a JSON string
invoice_settings_instance = InvoiceSettings.from_json(json)
# print the JSON string representation of the object
print(InvoiceSettings.to_json())

# convert the object into a dict
invoice_settings_dict = invoice_settings_instance.to_dict()
# create an instance of InvoiceSettings from a dict
invoice_settings_from_dict = InvoiceSettings.from_dict(invoice_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


