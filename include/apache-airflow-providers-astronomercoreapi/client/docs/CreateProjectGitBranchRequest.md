# CreateProjectGitBranchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from astronomercoreapi.models.create_project_git_branch_request import CreateProjectGitBranchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectGitBranchRequest from a JSON string
create_project_git_branch_request_instance = CreateProjectGitBranchRequest.from_json(json)
# print the JSON string representation of the object
print CreateProjectGitBranchRequest.to_json()

# convert the object into a dict
create_project_git_branch_request_dict = create_project_git_branch_request_instance.to_dict()
# create an instance of CreateProjectGitBranchRequest from a dict
create_project_git_branch_request_form_dict = create_project_git_branch_request.from_dict(create_project_git_branch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


