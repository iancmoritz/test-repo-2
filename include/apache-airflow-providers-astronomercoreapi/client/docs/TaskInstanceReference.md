# TaskInstanceReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** |  | [optional] 
**dag_run_id** | **str** |  | [optional] 
**execution_date** | **str** |  | [optional] 
**task_id** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.task_instance_reference import TaskInstanceReference

# TODO update the JSON string below
json = "{}"
# create an instance of TaskInstanceReference from a JSON string
task_instance_reference_instance = TaskInstanceReference.from_json(json)
# print the JSON string representation of the object
print TaskInstanceReference.to_json()

# convert the object into a dict
task_instance_reference_dict = task_instance_reference_instance.to_dict()
# create an instance of TaskInstanceReference from a dict
task_instance_reference_form_dict = task_instance_reference.from_dict(task_instance_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


