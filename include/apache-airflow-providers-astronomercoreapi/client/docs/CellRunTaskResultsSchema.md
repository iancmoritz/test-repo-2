# CellRunTaskResultsSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**List[CellRunTaskResultsSchemaColumn]**](CellRunTaskResultsSchemaColumn.md) |  | 

## Example

```python
from astronomercoreapi.models.cell_run_task_results_schema import CellRunTaskResultsSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CellRunTaskResultsSchema from a JSON string
cell_run_task_results_schema_instance = CellRunTaskResultsSchema.from_json(json)
# print the JSON string representation of the object
print CellRunTaskResultsSchema.to_json()

# convert the object into a dict
cell_run_task_results_schema_dict = cell_run_task_results_schema_instance.to_dict()
# create an instance of CellRunTaskResultsSchema from a dict
cell_run_task_results_schema_form_dict = cell_run_task_results_schema.from_dict(cell_run_task_results_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


