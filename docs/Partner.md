# Partner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**emails** | **List[str]** |  | [optional] 
**taxcode** | **str** |  | [optional] 
**iban** | **str** |  | [optional] 
**swift** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**general_ledger_number** | **str** |  | [optional] 
**tax_type** | [**PartnerTaxType**](PartnerTaxType.md) |  | [optional] 
**custom_billing_settings** | [**PartnerCustomBillingSettings**](PartnerCustomBillingSettings.md) |  | [optional] 
**group_member_tax_number** | **str** | The tax number of group member. Send tax number for update. Send empty string for delete. Ignored if omitted. | [optional] 

## Example

```python
from clientapi_billingo.models.partner import Partner

# TODO update the JSON string below
json = "{}"
# create an instance of Partner from a JSON string
partner_instance = Partner.from_json(json)
# print the JSON string representation of the object
print(Partner.to_json())

# convert the object into a dict
partner_dict = partner_instance.to_dict()
# create an instance of Partner from a dict
partner_from_dict = Partner.from_dict(partner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


