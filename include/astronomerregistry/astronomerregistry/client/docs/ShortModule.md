# ShortModule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**logo** | **str** |  | 
**name** | **str** |  | 
**provider_search_id** | **str** |  | 
**search_id** | **str** |  | 

## Example

```python
from astronomerregistry.models.short_module import ShortModule

# TODO update the JSON string below
json = "{}"
# create an instance of ShortModule from a JSON string
short_module_instance = ShortModule.from_json(json)
# print the JSON string representation of the object
print ShortModule.to_json()

# convert the object into a dict
short_module_dict = short_module_instance.to_dict()
# create an instance of ShortModule from a dict
short_module_form_dict = short_module.from_dict(short_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


