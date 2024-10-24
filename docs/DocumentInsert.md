# DocumentInsert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_id** | **str** |  | [optional] 
**partner_id** | **int** |  | 
**block_id** | **int** |  | 
**bank_account_id** | **int** |  | [optional] 
**type** | [**DocumentInsertType**](DocumentInsertType.md) |  | 
**fulfillment_date** | **date** |  | 
**due_date** | **date** |  | 
**payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | 
**language** | [**DocumentLanguage**](DocumentLanguage.md) |  | 
**currency** | [**Currency**](Currency.md) |  | 
**conversion_rate** | **float** |  | [optional] 
**electronic** | **bool** |  | [optional] [default to False]
**paid** | **bool** |  | [optional] [default to False]
**items** | [**List[DocumentInsertItemsInner]**](DocumentInsertItemsInner.md) |  | [optional] 
**comment** | **str** |  | [optional] 
**settings** | [**DocumentSettings**](DocumentSettings.md) |  | [optional] 
**advance_invoice** | **List[int]** |  | [optional] 
**discount** | [**Discount**](Discount.md) |  | [optional] 
**instant_payment** | **bool** |  | [optional] 

## Example

```python
from clientapi_billingo.models.document_insert import DocumentInsert

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentInsert from a JSON string
document_insert_instance = DocumentInsert.from_json(json)
# print the JSON string representation of the object
print(DocumentInsert.to_json())

# convert the object into a dict
document_insert_dict = document_insert_instance.to_dict()
# create an instance of DocumentInsert from a dict
document_insert_from_dict = DocumentInsert.from_dict(document_insert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


