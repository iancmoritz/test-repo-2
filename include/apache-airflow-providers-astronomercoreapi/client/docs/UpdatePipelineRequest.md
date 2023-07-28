# UpdatePipelineRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catchup** | **bool** |  | [optional] 
**cell_positions** | **List[str]** |  | [optional] 
**concurrency** | **int** |  | [optional] 
**dag_run_timeout_seconds** | **int** |  | [optional] 
**default_args** | [**DefaultArgsRequest**](DefaultArgsRequest.md) |  | [optional] 
**description** | **str** |  | [optional] 
**imports** | **List[str]** |  | [optional] 
**is_paused_upon_creation** | **bool** |  | [optional] 
**max_active_runs** | **int** |  | [optional] 
**max_active_tasks** | **int** |  | [optional] 
**name** | **str** |  | 
**params** | **Dict[str, str]** |  | [optional] 
**schedule_interval** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.update_pipeline_request import UpdatePipelineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePipelineRequest from a JSON string
update_pipeline_request_instance = UpdatePipelineRequest.from_json(json)
# print the JSON string representation of the object
print UpdatePipelineRequest.to_json()

# convert the object into a dict
update_pipeline_request_dict = update_pipeline_request_instance.to_dict()
# create an instance of UpdatePipelineRequest from a dict
update_pipeline_request_form_dict = update_pipeline_request.from_dict(update_pipeline_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


