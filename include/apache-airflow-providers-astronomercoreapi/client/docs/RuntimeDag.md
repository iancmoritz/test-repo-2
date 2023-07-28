# RuntimeDag


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** |  | 
**default_view** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**file_token** | **str** |  | 
**fileloc** | **str** |  | 
**has_import_errors** | **bool** |  | [optional] 
**has_task_concurrency_limits** | **bool** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_paused** | **bool** |  | [optional] 
**is_subdag** | **bool** |  | [optional] 
**last_expired** | **str** |  | [optional] 
**last_parsed_time** | **str** |  | [optional] 
**last_pickled** | **str** |  | [optional] 
**max_active_runs** | **int** |  | [optional] 
**max_active_tasks** | **int** |  | [optional] 
**next_dagrun** | **str** |  | [optional] 
**next_dagrun_create_after** | **str** |  | [optional] 
**next_dagrun_data_interval_end** | **str** |  | [optional] 
**next_dagrun_data_interval_start** | **str** |  | [optional] 
**owners** | **List[str]** |  | 
**pickle_id** | **str** |  | [optional] 
**root_dag_id** | **str** |  | [optional] 
**schedule_interval** | **object** |  | [optional] 
**scheduler_lock** | **bool** |  | [optional] 
**tags** | [**List[DagTag]**](DagTag.md) |  | [optional] 
**timetable_description** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.runtime_dag import RuntimeDag

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeDag from a JSON string
runtime_dag_instance = RuntimeDag.from_json(json)
# print the JSON string representation of the object
print RuntimeDag.to_json()

# convert the object into a dict
runtime_dag_dict = runtime_dag_instance.to_dict()
# create an instance of RuntimeDag from a dict
runtime_dag_form_dict = runtime_dag.from_dict(runtime_dag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


