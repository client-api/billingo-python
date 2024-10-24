# DocumentPartner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**emails** | **List[str]** |  | [optional] 
**taxcode** | **str** |  | [optional] 
**iban** | **str** |  | [optional] 
**swift** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**tax_type** | [**PartnerTaxType**](PartnerTaxType.md) |  | [optional] 

## Example

```python
from clientapi_billingo.models.document_partner import DocumentPartner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentPartner from a JSON string
document_partner_instance = DocumentPartner.from_json(json)
# print the JSON string representation of the object
print(DocumentPartner.to_json())

# convert the object into a dict
document_partner_dict = document_partner_instance.to_dict()
# create an instance of DocumentPartner from a dict
document_partner_from_dict = DocumentPartner.from_dict(document_partner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


