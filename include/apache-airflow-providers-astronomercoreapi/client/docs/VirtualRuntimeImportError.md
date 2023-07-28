# VirtualRuntimeImportError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | [optional] 
**import_error_id** | **int** |  | 
**stack_trace** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.virtual_runtime_import_error import VirtualRuntimeImportError

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualRuntimeImportError from a JSON string
virtual_runtime_import_error_instance = VirtualRuntimeImportError.from_json(json)
# print the JSON string representation of the object
print VirtualRuntimeImportError.to_json()

# convert the object into a dict
virtual_runtime_import_error_dict = virtual_runtime_import_error_instance.to_dict()
# create an instance of VirtualRuntimeImportError from a dict
virtual_runtime_import_error_form_dict = virtual_runtime_import_error.from_dict(virtual_runtime_import_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


