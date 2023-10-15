# ConversationRate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_currency** | [**Currency**](Currency.md) |  | [optional] 
**to_currency** | [**Currency**](Currency.md) |  | [optional] 
**conversation_rate** | **float** |  | [optional] 
**var_date** | **date** |  | [optional] 

## Example

```python
from clientapi_billingo.models.conversation_rate import ConversationRate

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationRate from a JSON string
conversation_rate_instance = ConversationRate.from_json(json)
# print the JSON string representation of the object
print ConversationRate.to_json()

# convert the object into a dict
conversation_rate_dict = conversation_rate_instance.to_dict()
# create an instance of ConversationRate from a dict
conversation_rate_form_dict = conversation_rate.from_dict(conversation_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


