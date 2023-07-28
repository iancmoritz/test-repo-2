# UpdateTeamRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from astronomercoreapi.models.update_team_request import UpdateTeamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTeamRequest from a JSON string
update_team_request_instance = UpdateTeamRequest.from_json(json)
# print the JSON string representation of the object
print UpdateTeamRequest.to_json()

# convert the object into a dict
update_team_request_dict = update_team_request_instance.to_dict()
# create an instance of UpdateTeamRequest from a dict
update_team_request_form_dict = update_team_request.from_dict(update_team_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

