# SpendingListItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**category** | [**Category**](Category.md) |  | [optional] 
**paid_at** | **date** |  | [optional] 
**fulfillment_date** | **date** |  | [optional] 
**partner** | [**SpendingPartner**](SpendingPartner.md) |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**conversion_rate** | **float** |  | [optional] 
**total_gross** | **float** |  | [optional] 
**total_gross_local** | **float** |  | [optional] 
**total_vat_amount** | **float** |  | [optional] 
**total_vat_amount_local** | **float** |  | [optional] 
**invoice_date** | **date** |  | [optional] 
**due_date** | **date** |  | [optional] 
**payment_method** | [**SpendingPaymentMethod**](SpendingPaymentMethod.md) |  | [optional] 
**comment** | **str** |  | [optional] 
**is_created_by_nav** | **bool** |  | [optional] 

## Example

```python
from clientapi_billingo.models.spending_list_item import SpendingListItem

# TODO update the JSON string below
json = "{}"
# create an instance of SpendingListItem from a JSON string
spending_list_item_instance = SpendingListItem.from_json(json)
# print the JSON string representation of the object
print SpendingListItem.to_json()

# convert the object into a dict
spending_list_item_dict = spending_list_item_instance.to_dict()
# create an instance of SpendingListItem from a dict
spending_list_item_form_dict = spending_list_item.from_dict(spending_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


