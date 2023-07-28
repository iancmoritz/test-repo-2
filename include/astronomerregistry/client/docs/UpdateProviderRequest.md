# UpdateProviderRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**docs_url** | **str** |  | [optional] 
**github_url** | **str** |  | [optional] 
**is_certified** | **bool** |  | [optional] 
**is_cloud_ide_compatible** | **bool** |  | [optional] 
**is_display_name_manual** | **bool** |  | [optional] 
**is_featured** | **bool** |  | [optional] 
**is_global** | **bool** |  | [optional] 
**is_logo_manual** | **bool** |  | [optional] 
**is_private** | **bool** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**logo** | **str** |  | [optional] 
**social_stats** | [**SocialStats**](SocialStats.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from astronomerregistry.models.update_provider_request import UpdateProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProviderRequest from a JSON string
update_provider_request_instance = UpdateProviderRequest.from_json(json)
# print the JSON string representation of the object
print UpdateProviderRequest.to_json()

# convert the object into a dict
update_provider_request_dict = update_provider_request_instance.to_dict()
# create an instance of UpdateProviderRequest from a dict
update_provider_request_form_dict = update_provider_request.from_dict(update_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


