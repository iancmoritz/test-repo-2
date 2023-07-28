# Invite


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **str** |  | 
**invite_id** | **str** |  | 
**invitee** | [**BasicSubjectProfile**](BasicSubjectProfile.md) |  | 
**inviter** | [**BasicSubjectProfile**](BasicSubjectProfile.md) |  | 
**o_auth_invite_id** | **str** |  | [optional] 
**org_name** | **str** | Deprecated: orgName has been replaced with organizationName | [optional] 
**org_short_name** | **str** | Deprecated: orgShortName has been replaced with organizationShortName | [optional] 
**organization_id** | **str** |  | 
**organization_name** | **str** |  | [optional] 
**organization_short_name** | **str** |  | [optional] 
**ticket_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.invite import Invite

# TODO update the JSON string below
json = "{}"
# create an instance of Invite from a JSON string
invite_instance = Invite.from_json(json)
# print the JSON string representation of the object
print Invite.to_json()

# convert the object into a dict
invite_dict = invite_instance.to_dict()
# create an instance of Invite from a dict
invite_form_dict = invite.from_dict(invite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


