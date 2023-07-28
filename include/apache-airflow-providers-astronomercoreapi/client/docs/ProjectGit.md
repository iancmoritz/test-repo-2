# ProjectGit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** |  | [optional] 
**dags_path** | **str** |  | [optional] 
**git_vendor_attributes** | [**ProjectGitVendorAttributes**](ProjectGitVendorAttributes.md) |  | [optional] 
**repo** | **str** |  | [optional] 
**token_set** | **bool** |  | [optional] 
**vendor** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.project_git import ProjectGit

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectGit from a JSON string
project_git_instance = ProjectGit.from_json(json)
# print the JSON string representation of the object
print ProjectGit.to_json()

# convert the object into a dict
project_git_dict = project_git_instance.to_dict()
# create an instance of ProjectGit from a dict
project_git_form_dict = project_git.from_dict(project_git_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


