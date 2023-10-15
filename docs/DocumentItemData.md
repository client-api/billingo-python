# DocumentItemData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **int** |  | 
**quantity** | **float** |  | 
**comment** | **str** |  | [optional] 

## Example

```python
from clientapi_billingo.models.document_item_data import DocumentItemData

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentItemData from a JSON string
document_item_data_instance = DocumentItemData.from_json(json)
# print the JSON string representation of the object
print DocumentItemData.to_json()

# convert the object into a dict
document_item_data_dict = document_item_data_instance.to_dict()
# create an instance of DocumentItemData from a dict
document_item_data_form_dict = document_item_data.from_dict(document_item_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


