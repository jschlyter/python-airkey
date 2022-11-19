# SystemProtocolEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier | 
**event** | [**SystemProtocolEvent**](SystemProtocolEvent.md) |  | [optional] 
**details** | [**SystemProtocolDetails**](SystemProtocolDetails.md) |  | [optional] 
**timestamp** | **str** | Timestamp of the event (ISO 8601-format compliant date with time in UTC, milliseconds precision) | [optional] 
**lock_identifier** | **str** | Identifier of the locking component which was involved in the event, otherwise empty if no locking component was involved | [optional] 
**lock_id** | **int** | Unique id of the locking component which was involved in the event if it still exists in the access control system, otherwise empty | [optional] 
**medium_identifier** | **str** | Identifier of the medium which was involved in the event, otherwise empty if no medium was involved,  | [optional] 
**medium_id** | **int** | Unique id of the medium which was involved in the event if it still exists in the access control system, otherwise empty | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

