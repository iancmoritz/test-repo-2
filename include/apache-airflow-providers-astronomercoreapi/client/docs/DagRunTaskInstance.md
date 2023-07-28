# DagRunTaskInstance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** |  | [optional] 
**dag_run_id** | **str** |  | [optional] 
**duration** | **float** |  | [optional] 
**end_date** | **str** |  | [optional] 
**execution_date** | **str** |  | [optional] 
**executor_config** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**max_tries** | **int** |  | [optional] 
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
**task_id** | **str** |  | [optional] 
**try_number** | **int** |  | [optional] 
**unixname** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.dag_run_task_instance import DagRunTaskInstance

# TODO update the JSON string below
json = "{}"
# create an instance of DagRunTaskInstance from a JSON string
dag_run_task_instance_instance = DagRunTaskInstance.from_json(json)
# print the JSON string representation of the object
print DagRunTaskInstance.to_json()

# convert the object into a dict
dag_run_task_instance_dict = dag_run_task_instance_instance.to_dict()
# create an instance of DagRunTaskInstance from a dict
dag_run_task_instance_form_dict = dag_run_task_instance.from_dict(dag_run_task_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


