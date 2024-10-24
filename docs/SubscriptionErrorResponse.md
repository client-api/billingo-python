# SubscriptionErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ClientError**](ClientError.md) |  | [optional] 

## Example

```python
from clientapi_billingo.models.subscription_error_response import SubscriptionErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionErrorResponse from a JSON string
subscription_error_response_instance = SubscriptionErrorResponse.from_json(json)
# print the JSON string representation of the object
print(SubscriptionErrorResponse.to_json())

# convert the object into a dict
subscription_error_response_dict = subscription_error_response_instance.to_dict()
# create an instance of SubscriptionErrorResponse from a dict
subscription_error_response_from_dict = SubscriptionErrorResponse.from_dict(subscription_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


