# PaymentHistory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | 
**price** | **float** |  | 
**payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | 
**voucher_number** | **str** |  | [optional] 
**conversion_rate** | **float** |  | [optional] 

## Example

```python
from clientapi_billingo.models.payment_history import PaymentHistory

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentHistory from a JSON string
payment_history_instance = PaymentHistory.from_json(json)
# print the JSON string representation of the object
print PaymentHistory.to_json()

# convert the object into a dict
payment_history_dict = payment_history_instance.to_dict()
# create an instance of PaymentHistory from a dict
payment_history_form_dict = payment_history.from_dict(payment_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


