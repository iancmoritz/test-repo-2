# InternalPaginationResultDagRunWithTaskInstances


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[InternalDagRunWithTaskInstances]**](InternalDagRunWithTaskInstances.md) |  | [optional] 
**next_cursor** | **str** |  | [optional] 
**prev_cursor** | **str** |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from astronomercoreapi.models.internal_pagination_result_dag_run_with_task_instances import InternalPaginationResultDagRunWithTaskInstances

# TODO update the JSON string below
json = "{}"
# create an instance of InternalPaginationResultDagRunWithTaskInstances from a JSON string
internal_pagination_result_dag_run_with_task_instances_instance = InternalPaginationResultDagRunWithTaskInstances.from_json(json)
# print the JSON string representation of the object
print InternalPaginationResultDagRunWithTaskInstances.to_json()

# convert the object into a dict
internal_pagination_result_dag_run_with_task_instances_dict = internal_pagination_result_dag_run_with_task_instances_instance.to_dict()
# create an instance of InternalPaginationResultDagRunWithTaskInstances from a dict
internal_pagination_result_dag_run_with_task_instances_form_dict = internal_pagination_result_dag_run_with_task_instances.from_dict(internal_pagination_result_dag_run_with_task_instances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


