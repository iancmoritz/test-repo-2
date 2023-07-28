# CellRunTaskLog


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**log** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from astronomercoreapi.models.cell_run_task_log import CellRunTaskLog

# TODO update the JSON string below
json = "{}"
# create an instance of CellRunTaskLog from a JSON string
cell_run_task_log_instance = CellRunTaskLog.from_json(json)
# print the JSON string representation of the object
print CellRunTaskLog.to_json()

# convert the object into a dict
cell_run_task_log_dict = cell_run_task_log_instance.to_dict()
# create an instance of CellRunTaskLog from a dict
cell_run_task_log_form_dict = cell_run_task_log.from_dict(cell_run_task_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


