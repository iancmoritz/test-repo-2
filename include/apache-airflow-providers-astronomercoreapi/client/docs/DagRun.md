# DagRun


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conf** | **Dict[str, object]** |  | [optional] 
**dag_id** | **str** |  | 
**dag_run_id** | **str** | Deprecated: DagRunId has been replaced with Id | 
**data_interval_end** | **str** |  | [optional] 
**data_interval_start** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**execution_date** | **str** |  | [optional] 
**external_trigger** | **bool** |  | [optional] 
**id** | **str** |  | 
**last_pickled** | **str** |  | [optional] 
**logical_date** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**run_type** | **str** | Deprecated: RunType has been replaced with Type | [optional] 
**start_date** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.dag_run import DagRun

# TODO update the JSON string below
json = "{}"
# create an instance of DagRun from a JSON string
dag_run_instance = DagRun.from_json(json)
# print the JSON string representation of the object
print DagRun.to_json()

# convert the object into a dict
dag_run_dict = dag_run_instance.to_dict()
# create an instance of DagRun from a dict
dag_run_form_dict = dag_run.from_dict(dag_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


