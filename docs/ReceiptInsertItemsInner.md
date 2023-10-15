# ReceiptInsertItemsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **int** |  | 
**name** | **str** |  | [optional] 
**unit_price** | **float** |  | 
**vat** | [**Vat**](Vat.md) |  | 

## Example

```python
from clientapi_billingo.models.receipt_insert_items_inner import ReceiptInsertItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptInsertItemsInner from a JSON string
receipt_insert_items_inner_instance = ReceiptInsertItemsInner.from_json(json)
# print the JSON string representation of the object
print ReceiptInsertItemsInner.to_json()

# convert the object into a dict
receipt_insert_items_inner_dict = receipt_insert_items_inner_instance.to_dict()
# create an instance of ReceiptInsertItemsInner from a dict
receipt_insert_items_inner_form_dict = receipt_insert_items_inner.from_dict(receipt_insert_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


