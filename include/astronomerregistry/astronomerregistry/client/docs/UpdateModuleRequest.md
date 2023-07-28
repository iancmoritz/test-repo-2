# UpdateModuleRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**display_name** | **str** | Name                 string            &#x60;json:\&quot;name\&quot; validate:\&quot;required\&quot;&#x60; | [optional] 
**documentation** | **str** |  | [optional] 
**github_url** | **str** |  | [optional] 
**import_path** | **str** |  | [optional] 
**inherits_from** | [**ModuleInheritsFrom**](ModuleInheritsFrom.md) |  | [optional] 
**is_certified** | **bool** |  | [optional] 
**is_cloud_ide_compatible** | **bool** |  | [optional] 
**is_display_name_manual** | **bool** |  | [optional] 
**is_featured** | **bool** |  | [optional] 
**is_global** | **bool** |  | [optional] 
**is_logo_manual** | **bool** |  | [optional] 
**is_private** | **bool** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**logo** | **str** |  | [optional] 
**parameters** | [**List[UpdateModuleParameterRequest]**](UpdateModuleParameterRequest.md) |  | [optional] 
**social_stats** | [**SocialStats**](SocialStats.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from astronomerregistry.models.update_module_request import UpdateModuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateModuleRequest from a JSON string
update_module_request_instance = UpdateModuleRequest.from_json(json)
# print the JSON string representation of the object
print UpdateModuleRequest.to_json()

# convert the object into a dict
update_module_request_dict = update_module_request_instance.to_dict()
# create an instance of UpdateModuleRequest from a dict
update_module_request_form_dict = update_module_request.from_dict(update_module_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


