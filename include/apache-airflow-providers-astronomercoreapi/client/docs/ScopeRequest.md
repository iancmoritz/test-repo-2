# ScopeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from astronomercoreapi.models.scope_request import ScopeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScopeRequest from a JSON string
scope_request_instance = ScopeRequest.from_json(json)
# print the JSON string representation of the object
print ScopeRequest.to_json()

# convert the object into a dict
scope_request_dict = scope_request_instance.to_dict()
# create an instance of ScopeRequest from a dict
scope_request_form_dict = scope_request.from_dict(scope_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


