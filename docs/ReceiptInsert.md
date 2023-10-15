# ReceiptInsert


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_id** | **str** |  | [optional] 
**partner_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**emails** | **List[str]** |  | [optional] 
**block_id** | **int** |  | 
**type** | [**DocumentType**](DocumentType.md) |  | 
**payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | 
**currency** | [**Currency**](Currency.md) |  | 
**conversion_rate** | **float** |  | [optional] 
**electronic** | **bool** |  | [optional] [default to False]
**items** | [**List[ReceiptInsertItemsInner]**](ReceiptInsertItemsInner.md) |  | [optional] 

## Example

```python
from clientapi_billingo.models.receipt_insert import ReceiptInsert

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptInsert from a JSON string
receipt_insert_instance = ReceiptInsert.from_json(json)
# print the JSON string representation of the object
print ReceiptInsert.to_json()

# convert the object into a dict
receipt_insert_dict = receipt_insert_instance.to_dict()
# create an instance of ReceiptInsert from a dict
receipt_insert_form_dict = receipt_insert.from_dict(receipt_insert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


