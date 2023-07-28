# TaskInstanceReferences


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_instances** | [**List[TaskInstanceReference]**](TaskInstanceReference.md) |  | [optional] 

## Example

```python
from astronomercoreapi.models.task_instance_references import TaskInstanceReferences

# TODO update the JSON string below
json = "{}"
# create an instance of TaskInstanceReferences from a JSON string
task_instance_references_instance = TaskInstanceReferences.from_json(json)
# print the JSON string representation of the object
print TaskInstanceReferences.to_json()

# convert the object into a dict
task_instance_references_dict = task_instance_references_instance.to_dict()
# create an instance of TaskInstanceReferences from a dict
task_instance_references_form_dict = task_instance_references.from_dict(task_instance_references_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


