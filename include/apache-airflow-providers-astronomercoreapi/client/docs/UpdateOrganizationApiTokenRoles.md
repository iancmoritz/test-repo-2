# UpdateOrganizationApiTokenRoles


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization** | **str** |  | 
**workspace** | [**List[ApiTokenWorkspaceRole]**](ApiTokenWorkspaceRole.md) |  | [optional] 

## Example

```python
from astronomercoreapi.models.update_organization_api_token_roles import UpdateOrganizationApiTokenRoles

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrganizationApiTokenRoles from a JSON string
update_organization_api_token_roles_instance = UpdateOrganizationApiTokenRoles.from_json(json)
# print the JSON string representation of the object
print UpdateOrganizationApiTokenRoles.to_json()

# convert the object into a dict
update_organization_api_token_roles_dict = update_organization_api_token_roles_instance.to_dict()
# create an instance of UpdateOrganizationApiTokenRoles from a dict
update_organization_api_token_roles_form_dict = update_organization_api_token_roles.from_dict(update_organization_api_token_roles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


