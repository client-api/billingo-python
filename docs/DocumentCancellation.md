# DocumentCancellation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellation_reason** | **str** |  | [optional] 
**cancellation_recipients** | **str** |  | [optional] 

## Example

```python
from clientapi_billingo.models.document_cancellation import DocumentCancellation

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCancellation from a JSON string
document_cancellation_instance = DocumentCancellation.from_json(json)
# print the JSON string representation of the object
print DocumentCancellation.to_json()

# convert the object into a dict
document_cancellation_dict = document_cancellation_instance.to_dict()
# create an instance of DocumentCancellation from a dict
document_cancellation_form_dict = document_cancellation.from_dict(document_cancellation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


