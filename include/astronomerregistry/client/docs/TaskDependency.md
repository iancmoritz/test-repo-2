# TaskDependency


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** |  | 
**provider** | **str** | May not exist in DB | [optional] 
**version** | **str** | May not exist in DB | [optional] 

## Example

```python
from astronomerregistry.models.task_dependency import TaskDependency

# TODO update the JSON string below
json = "{}"
# create an instance of TaskDependency from a JSON string
task_dependency_instance = TaskDependency.from_json(json)
# print the JSON string representation of the object
print TaskDependency.to_json()

# convert the object into a dict
task_dependency_dict = task_dependency_instance.to_dict()
# create an instance of TaskDependency from a dict
task_dependency_form_dict = task_dependency.from_dict(task_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


