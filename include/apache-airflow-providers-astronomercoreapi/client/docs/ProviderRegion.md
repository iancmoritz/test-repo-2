# ProviderRegion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banned_instances** | **List[str]** |  | [optional] 
**limited** | **bool** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from astronomercoreapi.models.provider_region import ProviderRegion

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderRegion from a JSON string
provider_region_instance = ProviderRegion.from_json(json)
# print the JSON string representation of the object
print ProviderRegion.to_json()

# convert the object into a dict
provider_region_dict = provider_region_instance.to_dict()
# create an instance of ProviderRegion from a dict
provider_region_form_dict = provider_region.from_dict(provider_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


