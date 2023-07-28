# HasPermissionsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checks** | [**List[PermissionCheckRequest]**](PermissionCheckRequest.md) |  | 

## Example

```python
from astronomercoreapi.models.has_permissions_request import HasPermissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HasPermissionsRequest from a JSON string
has_permissions_request_instance = HasPermissionsRequest.from_json(json)
# print the JSON string representation of the object
print HasPermissionsRequest.to_json()

# convert the object into a dict
has_permissions_request_dict = has_permissions_request_instance.to_dict()
# create an instance of HasPermissionsRequest from a dict
has_permissions_request_form_dict = has_permissions_request.from_dict(has_permissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


