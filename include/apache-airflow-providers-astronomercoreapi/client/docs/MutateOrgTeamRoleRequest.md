# MutateOrgTeamRoleRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 

## Example

```python
from astronomercoreapi.models.mutate_org_team_role_request import MutateOrgTeamRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MutateOrgTeamRoleRequest from a JSON string
mutate_org_team_role_request_instance = MutateOrgTeamRoleRequest.from_json(json)
# print the JSON string representation of the object
print MutateOrgTeamRoleRequest.to_json()

# convert the object into a dict
mutate_org_team_role_request_dict = mutate_org_team_role_request_instance.to_dict()
# create an instance of MutateOrgTeamRoleRequest from a dict
mutate_org_team_role_request_form_dict = mutate_org_team_role_request.from_dict(mutate_org_team_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


