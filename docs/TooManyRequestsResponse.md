# TooManyRequestsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ClientError**](ClientError.md) |  | [optional] 

## Example

```python
from clientapi_billingo.models.too_many_requests_response import TooManyRequestsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TooManyRequestsResponse from a JSON string
too_many_requests_response_instance = TooManyRequestsResponse.from_json(json)
# print the JSON string representation of the object
print(TooManyRequestsResponse.to_json())

# convert the object into a dict
too_many_requests_response_dict = too_many_requests_response_instance.to_dict()
# create an instance of TooManyRequestsResponse from a dict
too_many_requests_response_from_dict = TooManyRequestsResponse.from_dict(too_many_requests_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


