# LockProtocolEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_category** | **str** | Category of event | [optional] 
**event** | [**LockProtocolEvent**](LockProtocolEvent.md) |  | [optional] 
**details** | [**LockProtocolDetails**](LockProtocolDetails.md) |  | [optional] 
**lock_utc_delta** | **int** | Time difference of locking component regarding UTC | [optional] 
**medium** | [**SimpleMedium**](SimpleMedium.md) |  | [optional] 
**operator_name** | **str** | Name of person who was responsible for this event | [optional] 
**source_lock** | **bool** | Locking component has verified event or not | [optional] 
**source_medium** | **bool** | Medium has verified event or not | [optional] 
**timestamp** | **str** | Timestamp of the event (ISO 8601-format compliant date with time in UTC, milliseconds precision) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

