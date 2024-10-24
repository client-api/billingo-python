# DocumentProductData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**unit_price** | **float** |  | 
**unit_price_type** | [**UnitPriceType**](UnitPriceType.md) |  | 
**quantity** | **float** |  | 
**unit** | **str** |  | 
**vat** | [**Vat**](Vat.md) |  | 
**comment** | **str** |  | [optional] 
**entitlement** | [**Entitlement**](Entitlement.md) |  | [optional] 

## Example

```python
from clientapi_billingo.models.document_product_data import DocumentProductData

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentProductData from a JSON string
document_product_data_instance = DocumentProductData.from_json(json)
# print the JSON string representation of the object
print(DocumentProductData.to_json())

# convert the object into a dict
document_product_data_dict = document_product_data_instance.to_dict()
# create an instance of DocumentProductData from a dict
document_product_data_from_dict = DocumentProductData.from_dict(document_product_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


