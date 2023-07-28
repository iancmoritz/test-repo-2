# ClearTaskInstancesRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_run_id** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**include_downstream** | **bool** |  | [optional] 
**include_future** | **bool** |  | [optional] 
**include_parent_dags** | **bool** |  | [optional] 
**include_past** | **bool** |  | [optional] 
**include_sub_dags** | **bool** |  | [optional] 
**include_upstream** | **bool** |  | [optional] 
**is_dry_run** | **bool** |  | [optional] 
**only_failed** | **bool** |  | [optional] 
**only_running** | **bool** |  | [optional] 
**reset_dag_runs** | **bool** |  | [optional] 
**start_date** | **str** |  | [optional] 
**task_ids** | **List[str]** |  | [optional] 

## Example

```python
from astronomercoreapi.models.clear_task_instances_request import ClearTaskInstancesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClearTaskInstancesRequest from a JSON string
clear_task_instances_request_instance = ClearTaskInstancesRequest.from_json(json)
# print the JSON string representation of the object
print ClearTaskInstancesRequest.to_json()

# convert the object into a dict
clear_task_instances_request_dict = clear_task_instances_request_instance.to_dict()
# create an instance of ClearTaskInstancesRequest from a dict
clear_task_instances_request_form_dict = clear_task_instances_request.from_dict(clear_task_instances_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


