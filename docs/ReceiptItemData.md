# ReceiptItemData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **int** |  | 

## Example

```python
from clientapi_billingo.models.receipt_item_data import ReceiptItemData

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptItemData from a JSON string
receipt_item_data_instance = ReceiptItemData.from_json(json)
# print the JSON string representation of the object
print ReceiptItemData.to_json()

# convert the object into a dict
receipt_item_data_dict = receipt_item_data_instance.to_dict()
# create an instance of ReceiptItemData from a dict
receipt_item_data_form_dict = receipt_item_data.from_dict(receipt_item_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


