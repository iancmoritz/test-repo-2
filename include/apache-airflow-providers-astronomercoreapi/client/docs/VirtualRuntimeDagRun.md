# VirtualRuntimeDagRun


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conf** | **Dict[str, object]** |  | [optional] 
**dag_id** | **str** |  | 
**dag_run_id** | **str** |  | 
**data_interval_end** | **str** |  | [optional] 
**data_interval_start** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**external_trigger** | **bool** |  | [optional] 
**last_pickled** | **str** |  | [optional] 
**logical_date** | **str** |  | [optional] 
**run_type** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.virtual_runtime_dag_run import VirtualRuntimeDagRun

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualRuntimeDagRun from a JSON string
virtual_runtime_dag_run_instance = VirtualRuntimeDagRun.from_json(json)
# print the JSON string representation of the object
print VirtualRuntimeDagRun.to_json()

# convert the object into a dict
virtual_runtime_dag_run_dict = virtual_runtime_dag_run_instance.to_dict()
# create an instance of VirtualRuntimeDagRun from a dict
virtual_runtime_dag_run_form_dict = virtual_runtime_dag_run.from_dict(virtual_runtime_dag_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


