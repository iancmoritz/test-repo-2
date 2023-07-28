# DefaultArgsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**depends_on_past** | **bool** |  | [optional] 
**email** | **List[str]** |  | [optional] 
**email_on_failure** | **bool** |  | [optional] 
**email_on_retry** | **bool** |  | [optional] 
**execution_timeout_seconds** | **int** |  | [optional] 
**max_retry_delay_seconds** | **int** |  | [optional] 
**queue** | **str** |  | [optional] 
**retries** | **int** |  | [optional] 
**retry_delay_seconds** | **int** |  | [optional] 
**retry_exponential_backoff** | **bool** |  | [optional] 
**sla_seconds** | **int** |  | [optional] 
**task_concurrency** | **int** |  | [optional] 
**trigger_rule** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.default_args_request import DefaultArgsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultArgsRequest from a JSON string
default_args_request_instance = DefaultArgsRequest.from_json(json)
# print the JSON string representation of the object
print DefaultArgsRequest.to_json()

# convert the object into a dict
default_args_request_dict = default_args_request_instance.to_dict()
# create an instance of DefaultArgsRequest from a dict
default_args_request_form_dict = default_args_request.from_dict(default_args_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


