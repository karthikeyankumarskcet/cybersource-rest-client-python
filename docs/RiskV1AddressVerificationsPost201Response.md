# RiskV1AddressVerificationsPost201Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PtsV2IncrementalAuthorizationPatch201ResponseLinks**](PtsV2IncrementalAuthorizationPatch201ResponseLinks.md) |  | [optional] 
**id** | **str** | An unique identification number to identify the submitted request. It is also appended to the endpoint of the resource.  On incremental authorizations, this value with be the same as the identification number returned in the original authorization response.  #### PIN debit Returned for all PIN debit services.  | [optional] 
**submit_time_utc** | **str** | Time of request in UTC. Format: &#x60;YYYY-MM-DDThh:mm:ssZ&#x60; **Example** &#x60;2016-08-11T22:47:57Z&#x60; equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The &#x60;T&#x60; separates the date and the time. The &#x60;Z&#x60; indicates UTC.  Returned by authorization service.  #### PIN debit Time when the PIN debit credit, PIN debit purchase or PIN debit reversal was requested.  Returned by PIN debit credit, PIN debit purchase or PIN debit reversal.  | [optional] 
**submit_time_local** | **str** | Time that the transaction was submitted in local time. | [optional] 
**status** | **str** | The status for the call can be: - COMPLETED - INVALID_REQUEST - DECLINED  | [optional] 
**message** | **str** | The message describing the reason of the status. Value can be   - Apartment number missing or not found.   - Insufficient address information.   - House/Box number not found on street.   - Multiple address matches were found.   - P.O. Box identifier not found or out of range.   - Route service identifier not found or out of range.   - Street name not found in Postal code.   - Postal code not found in database.   - Unable to verify or correct address.   - Multiple addres matches were found (international)   - Address match not found (no reason given)   - Unsupported character set  | [optional] 
**client_reference_information** | [**RiskV1DecisionsPost201ResponseClientReferenceInformation**](RiskV1DecisionsPost201ResponseClientReferenceInformation.md) |  | [optional] 
**address_verification_information** | [**RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation**](RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.md) |  | [optional] 
**error_information** | [**RiskV1AddressVerificationsPost201ResponseErrorInformation**](RiskV1AddressVerificationsPost201ResponseErrorInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


