# User


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_url** | **str** |  | 
**color_mode_preference** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**full_name** | **str** |  | 
**id** | **str** |  | 
**invites** | [**List[Invite]**](Invite.md) |  | [optional] 
**last_login** | **str** | Only shown if admin listing users | [optional] 
**last_login_connection_name** | **str** | Only shown if admin listing users | [optional] 
**last_login_connection_type** | **str** | Only shown if admin listing users | [optional] 
**org_count** | **int** | Only shown if admin listing users | [optional] 
**org_role** | **str** | Only shown if listing org users | [optional] 
**org_user_relation_is_idp_managed** | **bool** | Only shown if listing org users | [optional] 
**roles** | [**List[UserRole]**](UserRole.md) | Only shown if admin listing users | [optional] 
**status** | **str** |  | 
**system_role** | **str** | Only shown if admin listing users | [optional] 
**updated_at** | **datetime** |  | 
**username** | **str** |  | 
**workspace_count** | **int** | Only shown if admin listing users | [optional] 
**workspace_role** | **str** | Only shown if listing workspace users | [optional] 

## Example

```python
from astronomercoreapi.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print User.to_json()

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_form_dict = user.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


