# ReceiptInsert

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_id** | **str** |  | [optional] 
**partner_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**emails** | **list[str]** |  | [optional] 
**block_id** | **int** |  | 
**type** | [**DocumentType**](DocumentType.md) |  | 
**payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | 
**currency** | [**Currency**](Currency.md) |  | 
**conversion_rate** | **float** |  | [optional] 
**electronic** | **bool** |  | [optional] [default to False]
**items** | **list[OneOfReceiptInsertItemsItems]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

