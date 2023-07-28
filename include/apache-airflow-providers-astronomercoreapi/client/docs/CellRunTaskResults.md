# CellRunTaskResults


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | 
**row_count** | **int** |  | [optional] 
**var_schema** | [**CellRunTaskResultsSchema**](CellRunTaskResultsSchema.md) |  | 

## Example

```python
from astronomercoreapi.models.cell_run_task_results import CellRunTaskResults

# TODO update the JSON string below
json = "{}"
# create an instance of CellRunTaskResults from a JSON string
cell_run_task_results_instance = CellRunTaskResults.from_json(json)
# print the JSON string representation of the object
print CellRunTaskResults.to_json()

# convert the object into a dict
cell_run_task_results_dict = cell_run_task_results_instance.to_dict()
# create an instance of CellRunTaskResults from a dict
cell_run_task_results_form_dict = cell_run_task_results.from_dict(cell_run_task_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


