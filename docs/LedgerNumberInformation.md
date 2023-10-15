# LedgerNumberInformation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bevetel** | **str** |  | [optional] 
**vevo** | **str** |  | [optional] 
**penztar** | **str** |  | [optional] 
**afa** | **str** |  | [optional] 

## Example

```python
from clientapi_billingo.models.ledger_number_information import LedgerNumberInformation

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerNumberInformation from a JSON string
ledger_number_information_instance = LedgerNumberInformation.from_json(json)
# print the JSON string representation of the object
print LedgerNumberInformation.to_json()

# convert the object into a dict
ledger_number_information_dict = ledger_number_information_instance.to_dict()
# create an instance of LedgerNumberInformation from a dict
ledger_number_information_form_dict = ledger_number_information.from_dict(ledger_number_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


