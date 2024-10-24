# CreateDocumentExport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_type** | [**DocumentExportQueryType**](DocumentExportQueryType.md) |  | 
**start_date** | **date** |  | 
**end_date** | **date** |  | 
**document_block_id** | **int** |  | [optional] 
**export_type** | [**DocumentExportType**](DocumentExportType.md) |  | 
**number_start_year** | **int** |  | [optional] 
**number_start_sequence** | **int** |  | [optional] 
**number_end_year** | **int** |  | [optional] 
**number_end_sequence** | **int** |  | [optional] 
**payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 
**sort_by** | [**DocumentExportSortBy**](DocumentExportSortBy.md) |  | [optional] 
**other_options** | [**DocumentExportOtherOptions**](DocumentExportOtherOptions.md) |  | [optional] 
**filter_extra** | [**DocumentExportFilterExtra**](DocumentExportFilterExtra.md) |  | [optional] 

## Example

```python
from clientapi_billingo.models.create_document_export import CreateDocumentExport

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDocumentExport from a JSON string
create_document_export_instance = CreateDocumentExport.from_json(json)
# print the JSON string representation of the object
print(CreateDocumentExport.to_json())

# convert the object into a dict
create_document_export_dict = create_document_export_instance.to_dict()
# create an instance of CreateDocumentExport from a dict
create_document_export_from_dict = CreateDocumentExport.from_dict(create_document_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


