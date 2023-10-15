# DocumentBlock


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**custom_field1** | **str** |  | [optional] 
**custom_field2** | **str** |  | [optional] 
**type** | [**DocumentBlockType**](DocumentBlockType.md) |  | [optional] 

## Example

```python
from clientapi_billingo.models.document_block import DocumentBlock

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentBlock from a JSON string
document_block_instance = DocumentBlock.from_json(json)
# print the JSON string representation of the object
print DocumentBlock.to_json()

# convert the object into a dict
document_block_dict = document_block_instance.to_dict()
# create an instance of DocumentBlock from a dict
document_block_form_dict = document_block.from_dict(document_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


