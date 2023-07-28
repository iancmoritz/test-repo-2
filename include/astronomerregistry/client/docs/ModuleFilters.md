# ModuleFilters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badges** | [**List[ShortLabel]**](ShortLabel.md) |  | 
**categories** | [**List[ShortLabel]**](ShortLabel.md) |  | 
**providers** | [**List[ShortProvider]**](ShortProvider.md) |  | 
**tiers** | [**List[ShortLabel]**](ShortLabel.md) |  | 

## Example

```python
from astronomerregistry.models.module_filters import ModuleFilters

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleFilters from a JSON string
module_filters_instance = ModuleFilters.from_json(json)
# print the JSON string representation of the object
print ModuleFilters.to_json()

# convert the object into a dict
module_filters_dict = module_filters_instance.to_dict()
# create an instance of ModuleFilters from a dict
module_filters_form_dict = module_filters.from_dict(module_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


