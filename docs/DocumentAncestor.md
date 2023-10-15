# DocumentAncestor

An object representing related documents to another document.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the related document. | [optional] 
**invoice_number** | **str** | Invoice number of the related document. | [optional] 

## Example

```python
from clientapi_billingo.models.document_ancestor import DocumentAncestor

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAncestor from a JSON string
document_ancestor_instance = DocumentAncestor.from_json(json)
# print the JSON string representation of the object
print DocumentAncestor.to_json()

# convert the object into a dict
document_ancestor_dict = document_ancestor_instance.to_dict()
# create an instance of DocumentAncestor from a dict
document_ancestor_form_dict = document_ancestor.from_dict(document_ancestor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


