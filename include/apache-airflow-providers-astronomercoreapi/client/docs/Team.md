# Team


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**created_by** | [**BasicSubjectProfile**](BasicSubjectProfile.md) |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | 
**is_idp_managed** | **bool** |  | 
**members** | [**List[TeamMember]**](TeamMember.md) |  | [optional] 
**members_count** | **int** |  | [optional] 
**name** | **str** |  | 
**organization_id** | **str** |  | 
**organization_role** | **str** |  | 
**roles** | [**List[TeamRole]**](TeamRole.md) |  | [optional] 
**roles_count** | **int** |  | [optional] 
**updated_at** | **datetime** |  | 
**updated_by** | [**BasicSubjectProfile**](BasicSubjectProfile.md) |  | [optional] 

## Example

```python
from astronomercoreapi.models.team import Team

# TODO update the JSON string below
json = "{}"
# create an instance of Team from a JSON string
team_instance = Team.from_json(json)
# print the JSON string representation of the object
print Team.to_json()

# convert the object into a dict
team_dict = team_instance.to_dict()
# create an instance of Team from a dict
team_form_dict = team.from_dict(team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


