# CellRunTaskLogs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last** | **int** |  | 
**logs** | [**List[CellRunTaskLog]**](CellRunTaskLog.md) |  | 

## Example

```python
from astronomercoreapi.models.cell_run_task_logs import CellRunTaskLogs

# TODO update the JSON string below
json = "{}"
# create an instance of CellRunTaskLogs from a JSON string
cell_run_task_logs_instance = CellRunTaskLogs.from_json(json)
# print the JSON string representation of the object
print CellRunTaskLogs.to_json()

# convert the object into a dict
cell_run_task_logs_dict = cell_run_task_logs_instance.to_dict()
# create an instance of CellRunTaskLogs from a dict
cell_run_task_logs_form_dict = cell_run_task_logs.from_dict(cell_run_task_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


