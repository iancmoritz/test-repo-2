# ProjectGitBranchesPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branches** | [**List[ProjectGitBranch]**](ProjectGitBranch.md) |  | 
**has_next_page** | **bool** |  | 
**page** | **int** |  | 
**per_page** | **int** |  | 

## Example

```python
from astronomercoreapi.models.project_git_branches_paginated import ProjectGitBranchesPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectGitBranchesPaginated from a JSON string
project_git_branches_paginated_instance = ProjectGitBranchesPaginated.from_json(json)
# print the JSON string representation of the object
print ProjectGitBranchesPaginated.to_json()

# convert the object into a dict
project_git_branches_paginated_dict = project_git_branches_paginated_instance.to_dict()
# create an instance of ProjectGitBranchesPaginated from a dict
project_git_branches_paginated_form_dict = project_git_branches_paginated.from_dict(project_git_branches_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


