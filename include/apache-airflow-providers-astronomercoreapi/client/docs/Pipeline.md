# Pipeline


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catchup** | **bool** |  | [optional] 
**cell_positions** | **List[str]** |  | [optional] 
**concurrency** | **int** |  | [optional] 
**created_at** | **str** |  | 
**created_by** | **str** |  | 
**dag_file** | **str** |  | [optional] 
**dag_run_timeout_seconds** | **int** |  | [optional] 
**default_args** | [**DefaultArgs**](DefaultArgs.md) |  | [optional] 
**dependencies** | **Dict[str, List[str]]** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | 
**imports** | **List[str]** |  | [optional] 
**is_paused_upon_creation** | **bool** |  | [optional] 
**max_active_runs** | **int** |  | [optional] 
**max_active_tasks** | **int** |  | [optional] 
**name** | **str** |  | 
**organization_id** | **str** |  | 
**params** | **Dict[str, str]** |  | [optional] 
**project_id** | **str** |  | 
**schedule_interval** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**timezone** | **str** |  | [optional] 
**updated_at** | **str** |  | 
**updated_by** | **str** |  | 
**workspace_id** | **str** |  | 

## Example

```python
from astronomercoreapi.models.pipeline import Pipeline

# TODO update the JSON string below
json = "{}"
# create an instance of Pipeline from a JSON string
pipeline_instance = Pipeline.from_json(json)
# print the JSON string representation of the object
print Pipeline.to_json()

# convert the object into a dict
pipeline_dict = pipeline_instance.to_dict()
# create an instance of Pipeline from a dict
pipeline_form_dict = pipeline.from_dict(pipeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


