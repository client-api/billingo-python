# SpendingSave


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | [**Currency**](Currency.md) |  | 
**conversion_rate** | **float** |  | [optional] 
**total_gross** | **float** |  | 
**total_gross_huf** | **float** |  | 
**total_vat_amount** | **float** |  | 
**total_vat_amount_huf** | **float** |  | 
**fulfillment_date** | **date** |  | 
**paid_at** | **date** |  | [optional] 
**category** | [**Category**](Category.md) |  | 
**comment** | **str** |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**invoice_date** | **date** |  | [optional] 
**due_date** | **date** |  | [optional] 
**payment_method** | [**SpendingPaymentMethod**](SpendingPaymentMethod.md) |  | 
**partner_id** | **int** |  | [optional] 

## Example

```python
from clientapi_billingo.models.spending_save import SpendingSave

# TODO update the JSON string below
json = "{}"
# create an instance of SpendingSave from a JSON string
spending_save_instance = SpendingSave.from_json(json)
# print the JSON string representation of the object
print SpendingSave.to_json()

# convert the object into a dict
spending_save_dict = spending_save_instance.to_dict()
# create an instance of SpendingSave from a dict
spending_save_form_dict = spending_save.from_dict(spending_save_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


