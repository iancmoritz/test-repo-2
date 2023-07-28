# CreateTeamRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**member_ids** | **List[str]** |  | [optional] 
**name** | **str** |  | 
**organization_role** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.create_team_request import CreateTeamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTeamRequest from a JSON string
create_team_request_instance = CreateTeamRequest.from_json(json)
# print the JSON string representation of the object
print CreateTeamRequest.to_json()

# convert the object into a dict
create_team_request_dict = create_team_request_instance.to_dict()
# create an instance of CreateTeamRequest from a dict
create_team_request_form_dict = create_team_request.from_dict(create_team_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


