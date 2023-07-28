# Workspace


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_only_deployments_default** | **bool** |  | 
**created_at** | **datetime** |  | 
**created_by** | [**BasicSubjectProfile**](BasicSubjectProfile.md) |  | [optional] 
**deployment_count** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | 
**org_short_name** | **str** | Deprecated: orgShortName has been replaced with organizationShortName | [optional] 
**organization_id** | **str** |  | 
**organization_name** | **str** |  | [optional] 
**organization_short_name** | **str** |  | [optional] 
**serverless_runtime_count** | **int** |  | [optional] 
**updated_at** | **datetime** |  | 
**updated_by** | [**BasicSubjectProfile**](BasicSubjectProfile.md) |  | [optional] 
**user_count** | **int** |  | [optional] 

## Example

```python
from astronomercoreapi.models.workspace import Workspace

# TODO update the JSON string below
json = "{}"
# create an instance of Workspace from a JSON string
workspace_instance = Workspace.from_json(json)
# print the JSON string representation of the object
print Workspace.to_json()

# convert the object into a dict
workspace_dict = workspace_instance.to_dict()
# create an instance of Workspace from a dict
workspace_form_dict = workspace.from_dict(workspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


