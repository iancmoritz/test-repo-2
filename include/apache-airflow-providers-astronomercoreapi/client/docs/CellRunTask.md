# CellRunTask


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_figures** | **bool** |  | [optional] 
**has_results** | **bool** |  | [optional] 
**state** | **str** |  | 
**task_id** | **str** |  | 

## Example

```python
from astronomercoreapi.models.cell_run_task import CellRunTask

# TODO update the JSON string below
json = "{}"
# create an instance of CellRunTask from a JSON string
cell_run_task_instance = CellRunTask.from_json(json)
# print the JSON string representation of the object
print CellRunTask.to_json()

# convert the object into a dict
cell_run_task_dict = cell_run_task_instance.to_dict()
# create an instance of CellRunTask from a dict
cell_run_task_form_dict = cell_run_task.from_dict(cell_run_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


