# JitPolicy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_org_role** | **str** |  | 
**default_workspace_roles** | [**List[WorkspaceRole]**](WorkspaceRole.md) |  | [optional] 

## Example

```python
from astronomercoreapi.models.jit_policy import JitPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of JitPolicy from a JSON string
jit_policy_instance = JitPolicy.from_json(json)
# print the JSON string representation of the object
print JitPolicy.to_json()

# convert the object into a dict
jit_policy_dict = jit_policy_instance.to_dict()
# create an instance of JitPolicy from a dict
jit_policy_form_dict = jit_policy.from_dict(jit_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


