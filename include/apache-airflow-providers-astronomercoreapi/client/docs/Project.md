# Project


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connections** | [**List[ProjectConnection]**](ProjectConnection.md) |  | [optional] 
**created_at** | **datetime** |  | 
**created_by** | **str** |  | 
**description** | **str** |  | [optional] 
**git** | [**ProjectGit**](ProjectGit.md) |  | [optional] 
**id** | **str** |  | 
**includes** | [**List[ProjectInclude]**](ProjectInclude.md) |  | [optional] 
**name** | **str** |  | 
**organization_id** | **str** |  | 
**pipeline_count** | **int** |  | [optional] 
**requirement_dependencies** | **Dict[str, List[str]]** |  | [optional] 
**requirements** | **List[str]** |  | [optional] 
**updated_at** | **datetime** |  | 
**updated_by** | **str** |  | 
**variables** | [**List[ProjectVariable]**](ProjectVariable.md) |  | [optional] 
**workspace_id** | **str** |  | 

## Example

```python
from astronomercoreapi.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print Project.to_json()

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_form_dict = project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


