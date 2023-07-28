# CreateProjectGitCommitRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** |  | [optional] 
**message** | **str** |  | 
**paths** | **List[str]** | if not provided, all project paths are committed | [optional] 

## Example

```python
from astronomercoreapi.models.create_project_git_commit_request import CreateProjectGitCommitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectGitCommitRequest from a JSON string
create_project_git_commit_request_instance = CreateProjectGitCommitRequest.from_json(json)
# print the JSON string representation of the object
print CreateProjectGitCommitRequest.to_json()

# convert the object into a dict
create_project_git_commit_request_dict = create_project_git_commit_request_instance.to_dict()
# create an instance of CreateProjectGitCommitRequest from a dict
create_project_git_commit_request_form_dict = create_project_git_commit_request.from_dict(create_project_git_commit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


