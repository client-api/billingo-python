# DocumentExportStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**state** | [**DocumentExportStatusState**](DocumentExportStatusState.md) |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from clientapi_billingo.models.document_export_status import DocumentExportStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentExportStatus from a JSON string
document_export_status_instance = DocumentExportStatus.from_json(json)
# print the JSON string representation of the object
print DocumentExportStatus.to_json()

# convert the object into a dict
document_export_status_dict = document_export_status_instance.to_dict()
# create an instance of DocumentExportStatus from a dict
document_export_status_form_dict = document_export_status.from_dict(document_export_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


