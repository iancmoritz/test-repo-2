# WorkspaceDag


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** |  | 
**deployment_id** | **str** |  | 
**is_active** | **bool** |  | [optional] 
**is_paused** | **bool** |  | 
**next_run_at** | **str** |  | [optional] 
**owners** | **List[str]** |  | [optional] 
**runs** | [**List[WorkspaceDagRun]**](WorkspaceDagRun.md) |  | [optional] 
**schedule** | [**DagSchedule**](DagSchedule.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**timetable_description** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.workspace_dag import WorkspaceDag

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceDag from a JSON string
workspace_dag_instance = WorkspaceDag.from_json(json)
# print the JSON string representation of the object
print WorkspaceDag.to_json()

# convert the object into a dict
workspace_dag_dict = workspace_dag_instance.to_dict()
# create an instance of WorkspaceDag from a dict
workspace_dag_form_dict = workspace_dag.from_dict(workspace_dag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


