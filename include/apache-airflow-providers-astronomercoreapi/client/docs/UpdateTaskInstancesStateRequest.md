# UpdateTaskInstancesStateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_run_id** | **str** |  | [optional] 
**execution_date** | **str** |  | [optional] 
**include_downstream** | **bool** |  | [optional] 
**include_future** | **bool** |  | [optional] 
**include_past** | **bool** |  | [optional] 
**include_upstream** | **bool** |  | [optional] 
**is_dry_run** | **bool** |  | [optional] 
**state** | **str** |  | [optional] 
**task_id** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.update_task_instances_state_request import UpdateTaskInstancesStateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTaskInstancesStateRequest from a JSON string
update_task_instances_state_request_instance = UpdateTaskInstancesStateRequest.from_json(json)
# print the JSON string representation of the object
print UpdateTaskInstancesStateRequest.to_json()

# convert the object into a dict
update_task_instances_state_request_dict = update_task_instances_state_request_instance.to_dict()
# create an instance of UpdateTaskInstancesStateRequest from a dict
update_task_instances_state_request_form_dict = update_task_instances_state_request.from_dict(update_task_instances_state_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


