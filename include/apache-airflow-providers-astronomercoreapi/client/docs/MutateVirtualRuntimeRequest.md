# MutateVirtualRuntimeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** |  | 
**task_mem_gib** | **float** |  | 

## Example

```python
from astronomercoreapi.models.mutate_virtual_runtime_request import MutateVirtualRuntimeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MutateVirtualRuntimeRequest from a JSON string
mutate_virtual_runtime_request_instance = MutateVirtualRuntimeRequest.from_json(json)
# print the JSON string representation of the object
print MutateVirtualRuntimeRequest.to_json()

# convert the object into a dict
mutate_virtual_runtime_request_dict = mutate_virtual_runtime_request_instance.to_dict()
# create an instance of MutateVirtualRuntimeRequest from a dict
mutate_virtual_runtime_request_form_dict = mutate_virtual_runtime_request.from_dict(mutate_virtual_runtime_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


