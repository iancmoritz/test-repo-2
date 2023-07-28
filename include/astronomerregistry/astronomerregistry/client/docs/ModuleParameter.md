# ModuleParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_value** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**inherits_from** | [**ModuleInheritsFrom**](ModuleInheritsFrom.md) |  | 
**name** | **str** |  | 
**required** | **bool** |  | 
**type** | **str** |  | [optional] 
**type_def** | [**TypeDef**](TypeDef.md) |  | [optional] 

## Example

```python
from astronomerregistry.models.module_parameter import ModuleParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleParameter from a JSON string
module_parameter_instance = ModuleParameter.from_json(json)
# print the JSON string representation of the object
print ModuleParameter.to_json()

# convert the object into a dict
module_parameter_dict = module_parameter_instance.to_dict()
# create an instance of ModuleParameter from a dict
module_parameter_form_dict = module_parameter.from_dict(module_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


