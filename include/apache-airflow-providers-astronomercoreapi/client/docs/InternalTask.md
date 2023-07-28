# InternalTask


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_links** | **List[str]** |  | [optional] 
**has_outlet_datasets** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**is_mapped** | **bool** |  | [optional] 
**label** | **str** |  | [optional] 
**operator** | **str** |  | [optional] 
**outlets** | [**List[InternalOutlet]**](InternalOutlet.md) |  | [optional] 

## Example

```python
from astronomercoreapi.models.internal_task import InternalTask

# TODO update the JSON string below
json = "{}"
# create an instance of InternalTask from a JSON string
internal_task_instance = InternalTask.from_json(json)
# print the JSON string representation of the object
print InternalTask.to_json()

# convert the object into a dict
internal_task_dict = internal_task_instance.to_dict()
# create an instance of InternalTask from a dict
internal_task_form_dict = internal_task.from_dict(internal_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


