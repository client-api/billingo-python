# OrganizationData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_code** | **str** |  | [optional] 
**subscription** | [**Subscription**](Subscription.md) |  | [optional] 

## Example

```python
from clientapi_billingo.models.organization_data import OrganizationData

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationData from a JSON string
organization_data_instance = OrganizationData.from_json(json)
# print the JSON string representation of the object
print OrganizationData.to_json()

# convert the object into a dict
organization_data_dict = organization_data_instance.to_dict()
# create an instance of OrganizationData from a dict
organization_data_form_dict = organization_data.from_dict(organization_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


