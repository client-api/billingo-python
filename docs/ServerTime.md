# ServerTime


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**epoch** | **int** |  | [optional] 
**formatted** | **str** |  | [optional] 
**w3c** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from clientapi_billingo.models.server_time import ServerTime

# TODO update the JSON string below
json = "{}"
# create an instance of ServerTime from a JSON string
server_time_instance = ServerTime.from_json(json)
# print the JSON string representation of the object
print ServerTime.to_json()

# convert the object into a dict
server_time_dict = server_time_instance.to_dict()
# create an instance of ServerTime from a dict
server_time_form_dict = server_time.from_dict(server_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


