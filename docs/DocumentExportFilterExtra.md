# DocumentExportFilterExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tensoft_vkod** | **str** |  | [optional] 
**ledger_number** | [**LedgerNumberInformation**](LedgerNumberInformation.md) |  | [optional] 
**forintsoft_konyvelesi_naplo_szam** | **str** |  | [optional] 
**positive_ledger_number** | **str** |  | [optional] 
**negative_ledger_number** | **str** |  | [optional] 
**rlb_kata** | **bool** |  | [optional] 
**rlb_note** | **str** |  | [optional] 
**novitax_naplokod** | **str** |  | [optional] 
**use_gross_values** | **bool** |  | [optional] 

## Example

```python
from clientapi_billingo.models.document_export_filter_extra import DocumentExportFilterExtra

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentExportFilterExtra from a JSON string
document_export_filter_extra_instance = DocumentExportFilterExtra.from_json(json)
# print the JSON string representation of the object
print(DocumentExportFilterExtra.to_json())

# convert the object into a dict
document_export_filter_extra_dict = document_export_filter_extra_instance.to_dict()
# create an instance of DocumentExportFilterExtra from a dict
document_export_filter_extra_from_dict = DocumentExportFilterExtra.from_dict(document_export_filter_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


