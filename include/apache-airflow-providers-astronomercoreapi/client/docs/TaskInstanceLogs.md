# TaskInstanceLogs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**continuation_token** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.task_instance_logs import TaskInstanceLogs

# TODO update the JSON string below
json = "{}"
# create an instance of TaskInstanceLogs from a JSON string
task_instance_logs_instance = TaskInstanceLogs.from_json(json)
# print the JSON string representation of the object
print TaskInstanceLogs.to_json()

# convert the object into a dict
task_instance_logs_dict = task_instance_logs_instance.to_dict()
# create an instance of TaskInstanceLogs from a dict
task_instance_logs_form_dict = task_instance_logs.from_dict(task_instance_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


