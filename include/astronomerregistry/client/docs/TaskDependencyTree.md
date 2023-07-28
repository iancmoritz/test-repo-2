# TaskDependencyTree


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[TaskDependencyTree]**](TaskDependencyTree.md) |  | 
**data** | [**TaskDependency**](TaskDependency.md) |  | 
**id** | **str** |  | 
**task_group** | **str** |  | [optional] 

## Example

```python
from astronomerregistry.models.task_dependency_tree import TaskDependencyTree

# TODO update the JSON string below
json = "{}"
# create an instance of TaskDependencyTree from a JSON string
task_dependency_tree_instance = TaskDependencyTree.from_json(json)
# print the JSON string representation of the object
print TaskDependencyTree.to_json()

# convert the object into a dict
task_dependency_tree_dict = task_dependency_tree_instance.to_dict()
# create an instance of TaskDependencyTree from a dict
task_dependency_tree_form_dict = task_dependency_tree.from_dict(task_dependency_tree_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


