# RegistrySearch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registry_objects** | [**List[RegistrySearchHit]**](RegistrySearchHit.md) | @iancmoritz TODO TEMPORARY, need a way to combine the results of the three different types of searches | 
**total_dag_count** | **int** |  | 
**total_module_count** | **int** |  | 
**total_provider_count** | **int** |  | 

## Example

```python
from astronomerregistry.models.registry_search import RegistrySearch

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrySearch from a JSON string
registry_search_instance = RegistrySearch.from_json(json)
# print the JSON string representation of the object
print RegistrySearch.to_json()

# convert the object into a dict
registry_search_dict = registry_search_instance.to_dict()
# create an instance of RegistrySearch from a dict
registry_search_form_dict = registry_search.from_dict(registry_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


