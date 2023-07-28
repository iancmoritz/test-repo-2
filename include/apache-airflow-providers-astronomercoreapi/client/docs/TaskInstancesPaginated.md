# TaskInstancesPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | 
**offset** | **int** |  | 
**task_instances** | [**List[TaskInstance]**](TaskInstance.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from astronomercoreapi.models.task_instances_paginated import TaskInstancesPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of TaskInstancesPaginated from a JSON string
task_instances_paginated_instance = TaskInstancesPaginated.from_json(json)
# print the JSON string representation of the object
print TaskInstancesPaginated.to_json()

# convert the object into a dict
task_instances_paginated_dict = task_instances_paginated_instance.to_dict()
# create an instance of TaskInstancesPaginated from a dict
task_instances_paginated_form_dict = task_instances_paginated.from_dict(task_instances_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


