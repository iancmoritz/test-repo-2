# ApiTokenRole


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** |  | 
**entity_type** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from astronomercoreapi.models.api_token_role import ApiTokenRole

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTokenRole from a JSON string
api_token_role_instance = ApiTokenRole.from_json(json)
# print the JSON string representation of the object
print ApiTokenRole.to_json()

# convert the object into a dict
api_token_role_dict = api_token_role_instance.to_dict()
# create an instance of ApiTokenRole from a dict
api_token_role_form_dict = api_token_role.from_dict(api_token_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


