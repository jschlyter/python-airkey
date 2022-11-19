# HolidayCalendarSlotUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier | 
**version** | **int** | Current version number of the holiday calendar slot | 
**slot_name** | **str** | Name of the holiday calendar slot (max. 50 characters) | 
**valid_from** | **str** | Holiday calendar slot start time regardless of the time zone (ISO 8601-format compliant date with time, without time zone: yyyy-mm-ddThh:mm) | 
**valid_to** | **str** | Holiday calendar slot end time regardless of the time zone (ISO 8601-format compliant date with time, without time zone: yyyy-mm-ddThh:mm) | 
**series** | [**HolidayCalendarSeries**](HolidayCalendarSeries.md) |  | [optional] 
**series_sequence_number** | **int** | Sequence number of this holiday calendar slot in the time series | [optional] 
**modify_future_slots** | **bool** | Updating this holiday calendar slot only or also all future slots in the series | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

