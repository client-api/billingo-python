# ModificationDocumentInsert


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**due_date** | **date** |  | [optional] 
**comment** | **str** |  | [optional] 
**payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 
**without_financial_fulfillment** | **bool** |  | [optional] [default to False]
**items** | [**List[DocumentInsertItemsInner]**](DocumentInsertItemsInner.md) |  | [optional] 

## Example

```python
from clientapi_billingo.models.modification_document_insert import ModificationDocumentInsert

# TODO update the JSON string below
json = "{}"
# create an instance of ModificationDocumentInsert from a JSON string
modification_document_insert_instance = ModificationDocumentInsert.from_json(json)
# print the JSON string representation of the object
print ModificationDocumentInsert.to_json()

# convert the object into a dict
modification_document_insert_dict = modification_document_insert_instance.to_dict()
# create an instance of ModificationDocumentInsert from a dict
modification_document_insert_form_dict = modification_document_insert.from_dict(modification_document_insert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


