# Address


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | [**Country**](Country.md) |  | 
**post_code** | **str** |  | 
**city** | **str** |  | 
**address** | **str** |  | 

## Example

```python
from clientapi_billingo.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print(Address.to_json())

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_from_dict = Address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


