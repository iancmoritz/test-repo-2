# CreateProviderRequest


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
**name** | **str** |  | 
**social_stats** | [**SocialStats**](SocialStats.md) |  | [optional] 
**type** | **str** |  | 
**version** | **str** |  | 

## Example

```python
from astronomerregistry.models.create_provider_request import CreateProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProviderRequest from a JSON string
create_provider_request_instance = CreateProviderRequest.from_json(json)
# print the JSON string representation of the object
print CreateProviderRequest.to_json()

# convert the object into a dict
create_provider_request_dict = create_provider_request_instance.to_dict()
# create an instance of CreateProviderRequest from a dict
create_provider_request_form_dict = create_provider_request.from_dict(create_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


