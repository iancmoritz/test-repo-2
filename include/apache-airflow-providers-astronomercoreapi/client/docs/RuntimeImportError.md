# RuntimeImportError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | [optional] 
**import_error_id** | **int** |  | 
**stack_trace** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.runtime_import_error import RuntimeImportError

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeImportError from a JSON string
runtime_import_error_instance = RuntimeImportError.from_json(json)
# print the JSON string representation of the object
print RuntimeImportError.to_json()

# convert the object into a dict
runtime_import_error_dict = runtime_import_error_instance.to_dict()
# create an instance of RuntimeImportError from a dict
runtime_import_error_form_dict = runtime_import_error.from_dict(runtime_import_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


