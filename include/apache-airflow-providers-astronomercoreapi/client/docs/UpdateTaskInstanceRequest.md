# UpdateTaskInstanceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_dry_run** | **bool** |  | [optional] 
**state** | **str** |  | 

## Example

```python
from astronomercoreapi.models.update_task_instance_request import UpdateTaskInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTaskInstanceRequest from a JSON string
update_task_instance_request_instance = UpdateTaskInstanceRequest.from_json(json)
# print the JSON string representation of the object
print UpdateTaskInstanceRequest.to_json()

# convert the object into a dict
update_task_instance_request_dict = update_task_instance_request_instance.to_dict()
# create an instance of UpdateTaskInstanceRequest from a dict
update_task_instance_request_form_dict = update_task_instance_request.from_dict(update_task_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


