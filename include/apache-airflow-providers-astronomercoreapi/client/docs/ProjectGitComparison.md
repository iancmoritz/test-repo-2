# ProjectGitComparison


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_comparisons** | [**List[ProjectGitFileComparison]**](ProjectGitFileComparison.md) |  | 

## Example

```python
from astronomercoreapi.models.project_git_comparison import ProjectGitComparison

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectGitComparison from a JSON string
project_git_comparison_instance = ProjectGitComparison.from_json(json)
# print the JSON string representation of the object
print ProjectGitComparison.to_json()

# convert the object into a dict
project_git_comparison_dict = project_git_comparison_instance.to_dict()
# create an instance of ProjectGitComparison from a dict
project_git_comparison_form_dict = project_git_comparison.from_dict(project_git_comparison_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


