# RegistrySearchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_dags** | **bool** |  | [optional] 
**include_modules** | **bool** |  | [optional] 
**include_providers** | **bool** |  | [optional] 
**query** | **str** |  | 

## Example

```python
from astronomerregistry.models.registry_search_request import RegistrySearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrySearchRequest from a JSON string
registry_search_request_instance = RegistrySearchRequest.from_json(json)
# print the JSON string representation of the object
print RegistrySearchRequest.to_json()

# convert the object into a dict
registry_search_request_dict = registry_search_request_instance.to_dict()
# create an instance of RegistrySearchRequest from a dict
registry_search_request_form_dict = registry_search_request.from_dict(registry_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


