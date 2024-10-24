# DocumentOrganization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**tax_number** | **str** |  | [optional] 
**bank_account** | [**DocumentBankAccount**](DocumentBankAccount.md) |  | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**small_taxpayer** | **bool** |  | [optional] 
**ev_number** | **str** |  | [optional] 
**eu_tax_number** | **str** |  | [optional] 
**cash_settled** | **bool** |  | [optional] 

## Example

```python
from clientapi_billingo.models.document_organization import DocumentOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentOrganization from a JSON string
document_organization_instance = DocumentOrganization.from_json(json)
# print the JSON string representation of the object
print(DocumentOrganization.to_json())

# convert the object into a dict
document_organization_dict = document_organization_instance.to_dict()
# create an instance of DocumentOrganization from a dict
document_organization_from_dict = DocumentOrganization.from_dict(document_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


