# UserRole


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 
**scope** | [**Scope**](Scope.md) |  | 
**subject** | [**Subject**](Subject.md) |  | 

## Example

```python
from astronomercoreapi.models.user_role import UserRole

# TODO update the JSON string below
json = "{}"
# create an instance of UserRole from a JSON string
user_role_instance = UserRole.from_json(json)
# print the JSON string representation of the object
print UserRole.to_json()

# convert the object into a dict
user_role_dict = user_role_instance.to_dict()
# create an instance of UserRole from a dict
user_role_form_dict = user_role.from_dict(user_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

