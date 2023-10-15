# ReceiptProductData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**unit_price** | **float** |  | 
**vat** | [**Vat**](Vat.md) |  | 

## Example

```python
from clientapi_billingo.models.receipt_product_data import ReceiptProductData

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptProductData from a JSON string
receipt_product_data_instance = ReceiptProductData.from_json(json)
# print the JSON string representation of the object
print ReceiptProductData.to_json()

# convert the object into a dict
receipt_product_data_dict = receipt_product_data_instance.to_dict()
# create an instance of ReceiptProductData from a dict
receipt_product_data_form_dict = receipt_product_data.from_dict(receipt_product_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


