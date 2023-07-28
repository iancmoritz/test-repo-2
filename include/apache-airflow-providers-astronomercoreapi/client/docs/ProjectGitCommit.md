# ProjectGitCommit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_name** | **str** |  | 
**var_date** | **str** |  | 
**message** | **str** |  | 
**sha** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from astronomercoreapi.models.project_git_commit import ProjectGitCommit

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectGitCommit from a JSON string
project_git_commit_instance = ProjectGitCommit.from_json(json)
# print the JSON string representation of the object
print ProjectGitCommit.to_json()

# convert the object into a dict
project_git_commit_dict = project_git_commit_instance.to_dict()
# create an instance of ProjectGitCommit from a dict
project_git_commit_form_dict = project_git_commit.from_dict(project_git_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


