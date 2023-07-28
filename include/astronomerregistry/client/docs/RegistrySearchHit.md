# RegistrySearchHit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**id** | **str** |  | 
**logo** | **str** |  | 
**name** | **str** |  | 
**other_versions** | **List[str]** |  | [optional] 
**provider_name** | **str** |  | [optional] 
**registry_object_type** | **str** |  | 
**search_rank** | **int** |  | 
**version** | **str** |  | 

## Example

```python
from astronomerregistry.models.registry_search_hit import RegistrySearchHit

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrySearchHit from a JSON string
registry_search_hit_instance = RegistrySearchHit.from_json(json)
# print the JSON string representation of the object
print RegistrySearchHit.to_json()

# convert the object into a dict
registry_search_hit_dict = registry_search_hit_instance.to_dict()
# create an instance of RegistrySearchHit from a dict
registry_search_hit_form_dict = registry_search_hit.from_dict(registry_search_hit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


