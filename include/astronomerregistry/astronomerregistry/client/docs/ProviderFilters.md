# ProviderFilters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badges** | [**List[ShortLabel]**](ShortLabel.md) |  | 
**categories** | [**List[ShortLabel]**](ShortLabel.md) |  | 
**tiers** | [**List[ShortLabel]**](ShortLabel.md) |  | 

## Example

```python
from astronomerregistry.models.provider_filters import ProviderFilters

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderFilters from a JSON string
provider_filters_instance = ProviderFilters.from_json(json)
# print the JSON string representation of the object
print ProviderFilters.to_json()

# convert the object into a dict
provider_filters_dict = provider_filters_instance.to_dict()
# create an instance of ProviderFilters from a dict
provider_filters_form_dict = provider_filters.from_dict(provider_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


