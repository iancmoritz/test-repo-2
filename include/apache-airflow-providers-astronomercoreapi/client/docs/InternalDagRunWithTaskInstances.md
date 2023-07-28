# InternalDagRunWithTaskInstances


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_interval_end** | **str** |  | [optional] 
**data_interval_start** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**logical_date** | **str** |  | [optional] 
**run_id** | **str** |  | [optional] 
**run_type** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**task_instances** | [**List[InternalTaskInstancesInner]**](InternalTaskInstancesInner.md) |  | [optional] 

## Example

```python
from astronomercoreapi.models.internal_dag_run_with_task_instances import InternalDagRunWithTaskInstances

# TODO update the JSON string below
json = "{}"
# create an instance of InternalDagRunWithTaskInstances from a JSON string
internal_dag_run_with_task_instances_instance = InternalDagRunWithTaskInstances.from_json(json)
# print the JSON string representation of the object
print InternalDagRunWithTaskInstances.to_json()

# convert the object into a dict
internal_dag_run_with_task_instances_dict = internal_dag_run_with_task_instances_instance.to_dict()
# create an instance of InternalDagRunWithTaskInstances from a dict
internal_dag_run_with_task_instances_form_dict = internal_dag_run_with_task_instances.from_dict(internal_dag_run_with_task_instances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


