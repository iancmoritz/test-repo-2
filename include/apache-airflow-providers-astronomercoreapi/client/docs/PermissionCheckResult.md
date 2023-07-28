# PermissionCheckResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorized** | **bool** |  | 
**permission** | [**Permission**](Permission.md) |  | 
**scope** | [**Scope**](Scope.md) |  | 
**subject** | [**Subject**](Subject.md) |  | 

## Example

```python
from astronomercoreapi.models.permission_check_result import PermissionCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionCheckResult from a JSON string
permission_check_result_instance = PermissionCheckResult.from_json(json)
# print the JSON string representation of the object
print PermissionCheckResult.to_json()

# convert the object into a dict
permission_check_result_dict = permission_check_result_instance.to_dict()
# create an instance of PermissionCheckResult from a dict
permission_check_result_form_dict = permission_check_result.from_dict(permission_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


