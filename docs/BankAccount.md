# BankAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | 
**account_number** | **str** |  | 
**account_number_iban** | **str** |  | [optional] 
**swift** | **str** |  | [optional] 
**currency** | [**Currency**](Currency.md) |  | 
**need_qr** | **bool** |  | [optional] [default to False]

## Example

```python
from clientapi_billingo.models.bank_account import BankAccount

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccount from a JSON string
bank_account_instance = BankAccount.from_json(json)
# print the JSON string representation of the object
print BankAccount.to_json()

# convert the object into a dict
bank_account_dict = bank_account_instance.to_dict()
# create an instance of BankAccount from a dict
bank_account_form_dict = bank_account.from_dict(bank_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


