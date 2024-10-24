# SpendingList

An object with a data property that contains an array of up to limit spending. Each entry in the array is a separate spending object. If no more spending are available, the resulting array will be empty.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SpendingListItem]**](SpendingListItem.md) |  | [optional] 
**total** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**current_page** | **int** |  | [optional] 
**last_page** | **int** |  | [optional] 
**prev_page_url** | **str** |  | [optional] 
**next_page_url** | **str** |  | [optional] 

## Example

```python
from clientapi_billingo.models.spending_list import SpendingList

# TODO update the JSON string below
json = "{}"
# create an instance of SpendingList from a JSON string
spending_list_instance = SpendingList.from_json(json)
# print the JSON string representation of the object
print(SpendingList.to_json())

# convert the object into a dict
spending_list_dict = spending_list_instance.to_dict()
# create an instance of SpendingList from a dict
spending_list_from_dict = SpendingList.from_dict(spending_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


