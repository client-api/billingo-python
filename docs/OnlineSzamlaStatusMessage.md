# OnlineSzamlaStatusMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validation_result_code** | **str** |  | [optional] 
**validation_error_code** | **str** |  | [optional] 
**human_readable_message** | **str** |  | [optional] 

## Example

```python
from clientapi_billingo.models.online_szamla_status_message import OnlineSzamlaStatusMessage

# TODO update the JSON string below
json = "{}"
# create an instance of OnlineSzamlaStatusMessage from a JSON string
online_szamla_status_message_instance = OnlineSzamlaStatusMessage.from_json(json)
# print the JSON string representation of the object
print OnlineSzamlaStatusMessage.to_json()

# convert the object into a dict
online_szamla_status_message_dict = online_szamla_status_message_instance.to_dict()
# create an instance of OnlineSzamlaStatusMessage from a dict
online_szamla_status_message_form_dict = online_szamla_status_message.from_dict(online_szamla_status_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


