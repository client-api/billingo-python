# SpendingPartner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**tax_code** | **str** |  | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**iban** | **str** |  | [optional] 
**swift** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**internal_comment** | **str** |  | [optional] 
**group_member_tax_number** | **str** |  | [optional] 

## Example

```python
from clientapi_billingo.models.spending_partner import SpendingPartner

# TODO update the JSON string below
json = "{}"
# create an instance of SpendingPartner from a JSON string
spending_partner_instance = SpendingPartner.from_json(json)
# print the JSON string representation of the object
print SpendingPartner.to_json()

# convert the object into a dict
spending_partner_dict = spending_partner_instance.to_dict()
# create an instance of SpendingPartner from a dict
spending_partner_form_dict = spending_partner.from_dict(spending_partner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


