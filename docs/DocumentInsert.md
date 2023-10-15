# DocumentInsert

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_id** | **str** |  | [optional] 
**partner_id** | **int** |  | 
**block_id** | **int** |  | 
**bank_account_id** | **int** |  | [optional] 
**type** | [**DocumentInsertType**](DocumentInsertType.md) |  | 
**fulfillment_date** | **date** |  | 
**due_date** | **date** |  | 
**payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | 
**language** | [**DocumentLanguage**](DocumentLanguage.md) |  | 
**currency** | [**Currency**](Currency.md) |  | 
**conversion_rate** | **float** |  | [optional] 
**electronic** | **bool** |  | [optional] [default to False]
**paid** | **bool** |  | [optional] [default to False]
**items** | **list[OneOfDocumentInsertItemsItems]** |  | [optional] 
**comment** | **str** |  | [optional] 
**settings** | [**DocumentSettings**](DocumentSettings.md) |  | [optional] 
**advance_invoice** | **list[int]** |  | [optional] 
**discount** | [**Discount**](Discount.md) |  | [optional] 
**instant_payment** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

