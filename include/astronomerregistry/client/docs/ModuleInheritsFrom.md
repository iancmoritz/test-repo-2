# ModuleInheritsFrom


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module_name** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**provider_name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from astronomerregistry.models.module_inherits_from import ModuleInheritsFrom

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleInheritsFrom from a JSON string
module_inherits_from_instance = ModuleInheritsFrom.from_json(json)
# print the JSON string representation of the object
print ModuleInheritsFrom.to_json()

# convert the object into a dict
module_inherits_from_dict = module_inherits_from_instance.to_dict()
# create an instance of ModuleInheritsFrom from a dict
module_inherits_from_form_dict = module_inherits_from.from_dict(module_inherits_from_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


