# InternalTaskInstancesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mapped_task_instance_summary** | [**InternalMappedTaskInstanceSummary**](InternalMappedTaskInstanceSummary.md) |  | [optional] 
**unmapped_task_instance** | [**InternalUnmappedTaskInstance**](InternalUnmappedTaskInstance.md) |  | [optional] 

## Example

```python
from astronomercoreapi.models.internal_task_instances_inner import InternalTaskInstancesInner

# TODO update the JSON string below
json = "{}"
# create an instance of InternalTaskInstancesInner from a JSON string
internal_task_instances_inner_instance = InternalTaskInstancesInner.from_json(json)
# print the JSON string representation of the object
print InternalTaskInstancesInner.to_json()

# convert the object into a dict
internal_task_instances_inner_dict = internal_task_instances_inner_instance.to_dict()
# create an instance of InternalTaskInstancesInner from a dict
internal_task_instances_inner_form_dict = internal_task_instances_inner.from_dict(internal_task_instances_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


