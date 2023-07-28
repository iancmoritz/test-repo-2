# TaskInstance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** |  | 
**dag_run_id** | **str** |  | 
**duration** | **float** |  | [optional] 
**end_date** | **str** |  | [optional] 
**execution_date** | **str** |  | [optional] 
**executor_config** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**map_index** | **int** |  | [optional] 
**max_tries** | **int** |  | [optional] 
**note** | **str** |  | [optional] 
**operator** | **str** |  | [optional] 
**pid** | **int** |  | [optional] 
**pool** | **str** |  | [optional] 
**pool_slots** | **int** |  | [optional] 
**priority_weight** | **int** |  | [optional] 
**queue** | **str** |  | [optional] 
**queued_when** | **str** |  | [optional] 
**rendered_fields** | **Dict[str, object]** |  | [optional] 
**start_date** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**task_id** | **str** |  | 
**try_number** | **int** |  | [optional] 
**unixname** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.task_instance import TaskInstance

# TODO update the JSON string below
json = "{}"
# create an instance of TaskInstance from a JSON string
task_instance_instance = TaskInstance.from_json(json)
# print the JSON string representation of the object
print TaskInstance.to_json()

# convert the object into a dict
task_instance_dict = task_instance_instance.to_dict()
# create an instance of TaskInstance from a dict
task_instance_form_dict = task_instance.from_dict(task_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


