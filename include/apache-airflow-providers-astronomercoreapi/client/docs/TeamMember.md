# TeamMember


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_url** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**user_id** | **str** |  | 
**username** | **str** |  | 

## Example

```python
from astronomercoreapi.models.team_member import TeamMember

# TODO update the JSON string below
json = "{}"
# create an instance of TeamMember from a JSON string
team_member_instance = TeamMember.from_json(json)
# print the JSON string representation of the object
print TeamMember.to_json()

# convert the object into a dict
team_member_dict = team_member_instance.to_dict()
# create an instance of TeamMember from a dict
team_member_form_dict = team_member.from_dict(team_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


