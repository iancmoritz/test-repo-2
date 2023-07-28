# Organization


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_service_id** | **str** |  | 
**billing_email** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**created_by** | **str** |  | [optional] 
**created_by_subject** | [**BasicSubjectProfile**](BasicSubjectProfile.md) |  | [optional] 
**domains** | **List[str]** |  | [optional] 
**entitlements** | [**Dict[str, Entitlement]**](Entitlement.md) |  | [optional] 
**id** | **str** |  | 
**is_azure_managed** | **bool** |  | [optional] 
**is_scim_enabled** | **bool** |  | 
**managed_domains** | [**List[ManagedDomain]**](ManagedDomain.md) |  | [optional] 
**metronome_id** | **str** |  | [optional] 
**metronome_plan_id** | **str** |  | [optional] 
**name** | **str** |  | 
**payment_method** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**salesforce_id** | **str** |  | [optional] 
**short_name** | **str** |  | 
**status** | **str** |  | [optional] 
**stripe_id** | **str** |  | [optional] 
**stripe_payment_method_id** | **str** |  | [optional] 
**support_plan** | **str** |  | 
**trial_expires_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | 
**updated_by** | **str** |  | [optional] 
**updated_by_subject** | [**BasicSubjectProfile**](BasicSubjectProfile.md) |  | [optional] 
**uses_custom_metronome_plan** | **bool** |  | [optional] 

## Example

```python
from astronomercoreapi.models.organization import Organization

# TODO update the JSON string below
json = "{}"
# create an instance of Organization from a JSON string
organization_instance = Organization.from_json(json)
# print the JSON string representation of the object
print Organization.to_json()

# convert the object into a dict
organization_dict = organization_instance.to_dict()
# create an instance of Organization from a dict
organization_form_dict = organization.from_dict(organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


