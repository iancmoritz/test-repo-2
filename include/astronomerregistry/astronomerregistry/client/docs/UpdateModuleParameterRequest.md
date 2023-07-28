# UpdateModuleParameterRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_value** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | 
**required** | **bool** |  | 
**type** | **str** |  | [optional] 
**type_def** | [**TypeDef**](TypeDef.md) |  | [optional] 

## Example

```python
from astronomerregistry.models.update_module_parameter_request import UpdateModuleParameterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateModuleParameterRequest from a JSON string
update_module_parameter_request_instance = UpdateModuleParameterRequest.from_json(json)
# print the JSON string representation of the object
print UpdateModuleParameterRequest.to_json()

# convert the object into a dict
update_module_parameter_request_dict = update_module_parameter_request_instance.to_dict()
# create an instance of UpdateModuleParameterRequest from a dict
update_module_parameter_request_form_dict = update_module_parameter_request.from_dict(update_module_parameter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


