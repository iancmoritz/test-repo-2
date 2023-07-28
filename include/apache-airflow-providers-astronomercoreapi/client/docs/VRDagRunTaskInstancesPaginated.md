# VRDagRunTaskInstancesPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**task_instances** | [**List[DagRunTaskInstance]**](DagRunTaskInstance.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from astronomercoreapi.models.vr_dag_run_task_instances_paginated import VRDagRunTaskInstancesPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of VRDagRunTaskInstancesPaginated from a JSON string
vr_dag_run_task_instances_paginated_instance = VRDagRunTaskInstancesPaginated.from_json(json)
# print the JSON string representation of the object
print VRDagRunTaskInstancesPaginated.to_json()

# convert the object into a dict
vr_dag_run_task_instances_paginated_dict = vr_dag_run_task_instances_paginated_instance.to_dict()
# create an instance of VRDagRunTaskInstancesPaginated from a dict
vr_dag_run_task_instances_paginated_form_dict = vr_dag_run_task_instances_paginated.from_dict(vr_dag_run_task_instances_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


