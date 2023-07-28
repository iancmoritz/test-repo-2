# WorkspacesPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | 
**offset** | **int** |  | 
**total_count** | **int** |  | 
**workspaces** | [**List[Workspace]**](Workspace.md) |  | 

## Example

```python
from astronomercoreapi.models.workspaces_paginated import WorkspacesPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspacesPaginated from a JSON string
workspaces_paginated_instance = WorkspacesPaginated.from_json(json)
# print the JSON string representation of the object
print WorkspacesPaginated.to_json()

# convert the object into a dict
workspaces_paginated_dict = workspaces_paginated_instance.to_dict()
# create an instance of WorkspacesPaginated from a dict
workspaces_paginated_form_dict = workspaces_paginated.from_dict(workspaces_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


