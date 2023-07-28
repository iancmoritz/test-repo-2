# MutateWorkspaceUserRoleRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 

## Example

```python
from astronomercoreapi.models.mutate_workspace_user_role_request import MutateWorkspaceUserRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MutateWorkspaceUserRoleRequest from a JSON string
mutate_workspace_user_role_request_instance = MutateWorkspaceUserRoleRequest.from_json(json)
# print the JSON string representation of the object
print MutateWorkspaceUserRoleRequest.to_json()

# convert the object into a dict
mutate_workspace_user_role_request_dict = mutate_workspace_user_role_request_instance.to_dict()
# create an instance of MutateWorkspaceUserRoleRequest from a dict
mutate_workspace_user_role_request_form_dict = mutate_workspace_user_role_request.from_dict(mutate_workspace_user_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


