# ProjectGitCommitsPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commits** | [**List[ProjectGitCommit]**](ProjectGitCommit.md) |  | 
**has_next_page** | **bool** |  | 
**page** | **int** |  | 
**per_page** | **int** |  | 

## Example

```python
from astronomercoreapi.models.project_git_commits_paginated import ProjectGitCommitsPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectGitCommitsPaginated from a JSON string
project_git_commits_paginated_instance = ProjectGitCommitsPaginated.from_json(json)
# print the JSON string representation of the object
print ProjectGitCommitsPaginated.to_json()

# convert the object into a dict
project_git_commits_paginated_dict = project_git_commits_paginated_instance.to_dict()
# create an instance of ProjectGitCommitsPaginated from a dict
project_git_commits_paginated_form_dict = project_git_commits_paginated.from_dict(project_git_commits_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


