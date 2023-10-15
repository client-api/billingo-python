# Document

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The document&#x27;s unique identifier. | [optional] 
**invoice_number** | **str** | The document&#x27;s invoice number. | [optional] 
**type** | [**DocumentType**](DocumentType.md) |  | [optional] 
**cancelled** | **bool** |  | [optional] 
**block_id** | **int** | DocumentBlock&#x27;s identifier. | [optional] 
**payment_status** | [**PaymentStatus**](PaymentStatus.md) |  | [optional] 
**payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 
**gross_total** | **float** | The document&#x27;s gross total price. | [optional] 
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
**tags** | **list[str]** |  | [optional] 
**notification_status** | [**DocumentNotificationStatus**](DocumentNotificationStatus.md) |  | [optional] 
**language** | [**DocumentLanguage**](DocumentLanguage.md) |  | [optional] 
**items** | [**list[DocumentItem]**](DocumentItem.md) |  | [optional] 
**summary** | [**DocumentSummary**](DocumentSummary.md) |  | [optional] 
**settings** | [**DocumentSettings**](DocumentSettings.md) |  | [optional] 
**online_szamla_status** | [**OnlineSzamlaStatusEnum**](OnlineSzamlaStatusEnum.md) |  | [optional] 
**related_documents** | [**list[DocumentAncestor]**](DocumentAncestor.md) |  | [optional] 
**discount** | [**Discount**](Discount.md) |  | [optional] 
**correction_type** | [**CorrectionType**](CorrectionType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

