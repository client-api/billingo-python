# DocumentSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mediated_service** | **bool** |  | [optional] [default to False]
**without_financial_fulfillment** | **bool** |  | [optional] [default to False]
**online_payment** | [**OnlinePayment**](OnlinePayment.md) |  | [optional] 
**round** | [**Round**](Round.md) |  | [optional] 
**no_send_onlineszamla_by_user** | **bool** |  | [optional] 
**order_number** | **str** |  | [optional] 
**place_id** | **int** |  | [optional] 
**instant_payment** | **bool** |  | [optional] 
**selected_type** | [**DocumentType**](DocumentType.md) |  | [optional] 

## Example

```python
from clientapi_billingo.models.document_settings import DocumentSettings

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSettings from a JSON string
document_settings_instance = DocumentSettings.from_json(json)
# print the JSON string representation of the object
print(DocumentSettings.to_json())

# convert the object into a dict
document_settings_dict = document_settings_instance.to_dict()
# create an instance of DocumentSettings from a dict
document_settings_from_dict = DocumentSettings.from_dict(document_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


