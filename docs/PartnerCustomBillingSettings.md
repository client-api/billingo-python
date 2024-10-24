# PartnerCustomBillingSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 
**document_form** | [**DocumentForm**](DocumentForm.md) |  | [optional] 
**due_days** | **int** |  | [optional] 
**document_currency** | [**Currency**](Currency.md) |  | [optional] 
**template_language_code** | [**DocumentLanguage**](DocumentLanguage.md) |  | [optional] 
**discount** | [**Discount**](Discount.md) |  | [optional] 

## Example

```python
from clientapi_billingo.models.partner_custom_billing_settings import PartnerCustomBillingSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerCustomBillingSettings from a JSON string
partner_custom_billing_settings_instance = PartnerCustomBillingSettings.from_json(json)
# print the JSON string representation of the object
print(PartnerCustomBillingSettings.to_json())

# convert the object into a dict
partner_custom_billing_settings_dict = partner_custom_billing_settings_instance.to_dict()
# create an instance of PartnerCustomBillingSettings from a dict
partner_custom_billing_settings_from_dict = PartnerCustomBillingSettings.from_dict(partner_custom_billing_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


