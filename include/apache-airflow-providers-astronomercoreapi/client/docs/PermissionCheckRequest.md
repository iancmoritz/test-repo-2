# PermissionCheckRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | [**PermissionRequest**](PermissionRequest.md) |  | 
**scope** | [**ScopeRequest**](ScopeRequest.md) |  | 

## Example

```python
from astronomercoreapi.models.permission_check_request import PermissionCheckRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionCheckRequest from a JSON string
permission_check_request_instance = PermissionCheckRequest.from_json(json)
# print the JSON string representation of the object
print PermissionCheckRequest.to_json()

# convert the object into a dict
permission_check_request_dict = permission_check_request_instance.to_dict()
# create an instance of PermissionCheckRequest from a dict
permission_check_request_form_dict = permission_check_request.from_dict(permission_check_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


