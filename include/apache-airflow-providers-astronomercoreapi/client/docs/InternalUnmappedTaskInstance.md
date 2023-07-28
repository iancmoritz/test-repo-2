# InternalUnmappedTaskInstance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**task_id** | **str** |  | [optional] 
**try_number** | **int** |  | [optional] 

## Example

```python
from astronomercoreapi.models.internal_unmapped_task_instance import InternalUnmappedTaskInstance

# TODO update the JSON string below
json = "{}"
# create an instance of InternalUnmappedTaskInstance from a JSON string
internal_unmapped_task_instance_instance = InternalUnmappedTaskInstance.from_json(json)
# print the JSON string representation of the object
print InternalUnmappedTaskInstance.to_json()

# convert the object into a dict
internal_unmapped_task_instance_dict = internal_unmapped_task_instance_instance.to_dict()
# create an instance of InternalUnmappedTaskInstance from a dict
internal_unmapped_task_instance_form_dict = internal_unmapped_task_instance.from_dict(internal_unmapped_task_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


