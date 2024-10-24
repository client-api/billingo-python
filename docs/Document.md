# Document

Document object representing your invoice. NOTE: partner property is deprecated. Please use document_partner instead.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The document&#39;s unique identifier. | [optional] 
**invoice_number** | **str** | The document&#39;s invoice number. | [optional] 
**type** | [**DocumentType**](DocumentType.md) |  | [optional] 
**cancelled** | **bool** |  | [optional] 
**block_id** | **int** | DocumentBlock&#39;s identifier. | [optional] 
**payment_status** | [**PaymentStatus**](PaymentStatus.md) |  | [optional] 
**payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 
**gross_total** | **float** | The document&#39;s gross total price. | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**conversion_rate** | **float** |  | [optional] 
**invoice_date** | **date** |  | [optional] 
**fulfillment_date** | **date** |  | [optional] 
**due_date** | **date** |  | [optional] 
**paid_date** | **date** |  | [optional] 
**organization** | [**DocumentOrganization**](DocumentOrganization.md) |  | [optional] 
**partner** | [**Partner**](Partner.md) |  | [optional] 
**document_partner** | [**DocumentPartner**](DocumentPartner.md) |  | [optional] 
**electronic** | **bool** |  | [optional] 
**comment** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**notification_status** | [**DocumentNotificationStatus**](DocumentNotificationStatus.md) |  | [optional] 
**language** | [**DocumentLanguage**](DocumentLanguage.md) |  | [optional] 
**items** | [**List[DocumentItem]**](DocumentItem.md) |  | [optional] 
**summary** | [**DocumentSummary**](DocumentSummary.md) |  | [optional] 
**settings** | [**DocumentSettings**](DocumentSettings.md) |  | [optional] 
**online_szamla_status** | [**OnlineSzamlaStatusEnum**](OnlineSzamlaStatusEnum.md) |  | [optional] 
**related_documents** | [**List[DocumentAncestor]**](DocumentAncestor.md) |  | [optional] 
**discount** | [**Discount**](Discount.md) |  | [optional] 
**correction_type** | [**CorrectionType**](CorrectionType.md) |  | [optional] 

## Example

```python
from clientapi_billingo.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print(Document.to_json())

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_from_dict = Document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


