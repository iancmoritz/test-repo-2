# TeamRole


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** |  | 
**entity_type** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from astronomercoreapi.models.team_role import TeamRole

# TODO update the JSON string below
json = "{}"
# create an instance of TeamRole from a JSON string
team_role_instance = TeamRole.from_json(json)
# print the JSON string representation of the object
print TeamRole.to_json()

# convert the object into a dict
team_role_dict = team_role_instance.to_dict()
# create an instance of TeamRole from a dict
team_role_form_dict = team_role.from_dict(team_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


