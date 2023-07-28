# MutateOrgUserRoleRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 

## Example

```python
from astronomercoreapi.models.mutate_org_user_role_request import MutateOrgUserRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MutateOrgUserRoleRequest from a JSON string
mutate_org_user_role_request_instance = MutateOrgUserRoleRequest.from_json(json)
# print the JSON string representation of the object
print MutateOrgUserRoleRequest.to_json()

# convert the object into a dict
mutate_org_user_role_request_dict = mutate_org_user_role_request_instance.to_dict()
# create an instance of MutateOrgUserRoleRequest from a dict
mutate_org_user_role_request_form_dict = mutate_org_user_role_request.from_dict(mutate_org_user_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


