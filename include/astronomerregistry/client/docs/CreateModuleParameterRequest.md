# CreateModuleParameterRequest


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
from astronomerregistry.models.create_module_parameter_request import CreateModuleParameterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateModuleParameterRequest from a JSON string
create_module_parameter_request_instance = CreateModuleParameterRequest.from_json(json)
# print the JSON string representation of the object
print CreateModuleParameterRequest.to_json()

# convert the object into a dict
create_module_parameter_request_dict = create_module_parameter_request_instance.to_dict()
# create an instance of CreateModuleParameterRequest from a dict
create_module_parameter_request_form_dict = create_module_parameter_request.from_dict(create_module_parameter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


