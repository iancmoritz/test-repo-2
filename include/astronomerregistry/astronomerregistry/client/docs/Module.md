# Module


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badges** | [**List[ShortLabel]**](ShortLabel.md) |  | 
**categories** | [**List[ShortLabel]**](ShortLabel.md) |  | 
**created_at** | **str** |  | 
**created_by** | **str** |  | 
**description** | **str** |  | 
**display_name** | **str** |  | 
**documentation** | **str** |  | 
**github_url** | **str** |  | 
**import_path** | **str** |  | 
**is_certified** | **bool** |  | 
**is_cloud_ide_compatible** | **bool** |  | 
**is_display_name_manual** | **bool** |  | 
**is_featured** | **bool** |  | 
**is_global** | **bool** |  | 
**is_latest_version** | **bool** |  | 
**is_logo_manual** | **bool** |  | 
**is_private** | **bool** |  | 
**logo** | **str** |  | 
**name** | **str** |  | 
**organization_id** | **str** |  | 
**other_versions** | **List[str]** |  | 
**parameters** | [**List[ModuleParameter]**](ModuleParameter.md) |  | 
**provider_display_name** | **str** |  | 
**provider_name** | **str** |  | 
**search_id** | **str** |  | 
**search_rank** | **int** |  | [optional] 
**short_name_id** | **str** |  | 
**social_stats** | [**SocialStats**](SocialStats.md) |  | 
**tiers** | [**List[ShortLabel]**](ShortLabel.md) |  | 
**type** | **str** |  | 
**updated_at** | **str** |  | 
**updated_by** | **str** |  | 
**version** | **str** |  | 

## Example

```python
from astronomerregistry.models.module import Module

# TODO update the JSON string below
json = "{}"
# create an instance of Module from a JSON string
module_instance = Module.from_json(json)
# print the JSON string representation of the object
print Module.to_json()

# convert the object into a dict
module_dict = module_instance.to_dict()
# create an instance of Module from a dict
module_form_dict = module.from_dict(module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


