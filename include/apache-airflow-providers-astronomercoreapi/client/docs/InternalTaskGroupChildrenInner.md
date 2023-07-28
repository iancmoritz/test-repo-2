# InternalTaskGroupChildrenInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task** | [**InternalTask**](InternalTask.md) |  | [optional] 
**task_group** | [**InternalTaskGroup**](InternalTaskGroup.md) |  | [optional] 

## Example

```python
from astronomercoreapi.models.internal_task_group_children_inner import InternalTaskGroupChildrenInner

# TODO update the JSON string below
json = "{}"
# create an instance of InternalTaskGroupChildrenInner from a JSON string
internal_task_group_children_inner_instance = InternalTaskGroupChildrenInner.from_json(json)
# print the JSON string representation of the object
print InternalTaskGroupChildrenInner.to_json()

# convert the object into a dict
internal_task_group_children_inner_dict = internal_task_group_children_inner_instance.to_dict()
# create an instance of InternalTaskGroupChildrenInner from a dict
internal_task_group_children_inner_form_dict = internal_task_group_children_inner.from_dict(internal_task_group_children_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


