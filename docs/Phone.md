# Phone

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**medium_type** | **str** | Phone type of the medium | [optional] 
**app_type** | **str** | Type of the used app | [optional] 
**platform_version** | **str** | Current version of the platform | [optional] 
**phone_settings** | [**PhoneSettings**](PhoneSettings.md) |  | 
**pairing_code** | **str** | Generated pairing code | [optional] 
**pairing_code_valid_until** | **str** | Timestamp until when the pairing code is valid (ISO 8601-format compliant date with time in UTC, milliseconds precision: yyyy-mm-ddThh:mm:ss.SSSZ) | [optional] 
**phone_number** | **str** | Phone number of the phone starting with &#x27;+&#x27; followed by 1-49 digits (incl. possible spaces), e.g. +436641234567 | 
**sent_key_on** | **str** | Timestamp when the pairing code was sent to the phone (ISO 8601-format compliant date with time in UTC, milliseconds precision: yyyy-mm-ddThh:mm:ss.SSSZ) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

