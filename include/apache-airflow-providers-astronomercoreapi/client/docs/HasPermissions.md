# HasPermissions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checks** | [**List[PermissionCheckResult]**](PermissionCheckResult.md) |  | 

## Example

```python
from astronomercoreapi.models.has_permissions import HasPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of HasPermissions from a JSON string
has_permissions_instance = HasPermissions.from_json(json)
# print the JSON string representation of the object
print HasPermissions.to_json()

# convert the object into a dict
has_permissions_dict = has_permissions_instance.to_dict()
# create an instance of HasPermissions from a dict
has_permissions_form_dict = has_permissions.from_dict(has_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


