# ProjectsPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | 
**offset** | **int** |  | 
**projects** | [**List[Project]**](Project.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from astronomercoreapi.models.projects_paginated import ProjectsPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsPaginated from a JSON string
projects_paginated_instance = ProjectsPaginated.from_json(json)
# print the JSON string representation of the object
print ProjectsPaginated.to_json()

# convert the object into a dict
projects_paginated_dict = projects_paginated_instance.to_dict()
# create an instance of ProjectsPaginated from a dict
projects_paginated_form_dict = projects_paginated.from_dict(projects_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


