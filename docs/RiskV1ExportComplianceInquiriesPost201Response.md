# RiskV1ExportComplianceInquiriesPost201Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PtsV2IncrementalAuthorizationPatch201ResponseLinks**](PtsV2IncrementalAuthorizationPatch201ResponseLinks.md) |  | [optional] 
**id** | **str** | An unique identification number to identify the submitted request. It is also appended to the endpoint of the resource.  On incremental authorizations, this value with be the same as the identification number returned in the original authorization response.  #### PIN debit Returned for all PIN debit services.  | [optional] 
**submit_time_utc** | **str** | Time of request in UTC. Format: &#x60;YYYY-MM-DDThh:mm:ssZ&#x60; **Example** &#x60;2016-08-11T22:47:57Z&#x60; equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The &#x60;T&#x60; separates the date and the time. The &#x60;Z&#x60; indicates UTC.  Returned by authorization service.  #### PIN debit Time when the PIN debit credit, PIN debit purchase or PIN debit reversal was requested.  Returned by PIN debit credit, PIN debit purchase or PIN debit reversal.  | [optional] 
**submit_time_local** | **str** | Time that the transaction was submitted in local time. | [optional] 
**status** | **str** | The status for the call can be: - COMPLETED - INVALID_REQUEST - DECLINED  | [optional] 
**message** | **str** | The message describing the reason of the status. Value can be   - The customer matched the Denied Parties List   - The Export bill_country/ship_country  match   - Export email_country match   - Export hostname_country/ip_country match  | [optional] 
**client_reference_information** | [**RiskV1DecisionsPost201ResponseClientReferenceInformation**](RiskV1DecisionsPost201ResponseClientReferenceInformation.md) |  | [optional] 
**export_compliance_information** | [**RiskV1ExportComplianceInquiriesPost201ResponseExportComplianceInformation**](RiskV1ExportComplianceInquiriesPost201ResponseExportComplianceInformation.md) |  | [optional] 
**error_information** | [**RiskV1ExportComplianceInquiriesPost201ResponseErrorInformation**](RiskV1ExportComplianceInquiriesPost201ResponseErrorInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


