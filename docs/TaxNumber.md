# TaxNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_number** | **str** |  | [optional] 
**result** | [**CheckTaxNumberMessage**](CheckTaxNumberMessage.md) |  | [optional] 

## Example

```python
from clientapi_billingo.models.tax_number import TaxNumber

# TODO update the JSON string below
json = "{}"
# create an instance of TaxNumber from a JSON string
tax_number_instance = TaxNumber.from_json(json)
# print the JSON string representation of the object
print(TaxNumber.to_json())

# convert the object into a dict
tax_number_dict = tax_number_instance.to_dict()
# create an instance of TaxNumber from a dict
tax_number_from_dict = TaxNumber.from_dict(tax_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


