# CellRun


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_task_id** | **str** |  | 
**state** | **str** |  | 
**tasks** | [**List[CellRunTask]**](CellRunTask.md) |  | 

## Example

```python
from astronomercoreapi.models.cell_run import CellRun

# TODO update the JSON string below
json = "{}"
# create an instance of CellRun from a JSON string
cell_run_instance = CellRun.from_json(json)
# print the JSON string representation of the object
print CellRun.to_json()

# convert the object into a dict
cell_run_dict = cell_run_instance.to_dict()
# create an instance of CellRun from a dict
cell_run_form_dict = cell_run.from_dict(cell_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


