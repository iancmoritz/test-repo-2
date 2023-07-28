# ShortProvider


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**logo** | **str** |  | 
**name** | **str** |  | 
**search_id** | **str** |  | 

## Example

```python
from astronomerregistry.models.short_provider import ShortProvider

# TODO update the JSON string below
json = "{}"
# create an instance of ShortProvider from a JSON string
short_provider_instance = ShortProvider.from_json(json)
# print the JSON string representation of the object
print ShortProvider.to_json()

# convert the object into a dict
short_provider_dict = short_provider_instance.to_dict()
# create an instance of ShortProvider from a dict
short_provider_form_dict = short_provider.from_dict(short_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


