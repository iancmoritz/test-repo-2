# WorkspaceDagRun


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

## Example

```python
from astronomercoreapi.models.workspace_dag_run import WorkspaceDagRun

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceDagRun from a JSON string
workspace_dag_run_instance = WorkspaceDagRun.from_json(json)
# print the JSON string representation of the object
print WorkspaceDagRun.to_json()

# convert the object into a dict
workspace_dag_run_dict = workspace_dag_run_instance.to_dict()
# create an instance of WorkspaceDagRun from a dict
workspace_dag_run_form_dict = workspace_dag_run.from_dict(workspace_dag_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


