# Provider


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badges** | [**List[ShortLabel]**](ShortLabel.md) |  | 
**categories** | [**List[ShortLabel]**](ShortLabel.md) |  | 
**created_at** | **str** |  | 
**created_by** | **str** |  | 
**description** | **str** |  | 
**display_name** | **str** |  | 
**docs_url** | **str** |  | 
**github_url** | **str** |  | 
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
**provider_id** | **str** |  | 
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
from astronomerregistry.models.provider import Provider

# TODO update the JSON string below
json = "{}"
# create an instance of Provider from a JSON string
provider_instance = Provider.from_json(json)
# print the JSON string representation of the object
print Provider.to_json()

# convert the object into a dict
provider_dict = provider_instance.to_dict()
# create an instance of Provider from a dict
provider_form_dict = provider.from_dict(provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


