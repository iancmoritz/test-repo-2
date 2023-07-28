# UpdateProjectConnectionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra** | **Dict[str, str]** |  | [optional] 
**host** | **str** |  | [optional] 
**id** | **str** |  | 
**login** | **str** |  | [optional] 
**password** | **str** | nil represents no change, empty string represents blank password | [optional] 
**port** | **int** |  | [optional] 
**var_schema** | **str** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from astronomercoreapi.models.update_project_connection_request import UpdateProjectConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProjectConnectionRequest from a JSON string
update_project_connection_request_instance = UpdateProjectConnectionRequest.from_json(json)
# print the JSON string representation of the object
print UpdateProjectConnectionRequest.to_json()

# convert the object into a dict
update_project_connection_request_dict = update_project_connection_request_instance.to_dict()
# create an instance of UpdateProjectConnectionRequest from a dict
update_project_connection_request_form_dict = update_project_connection_request.from_dict(update_project_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


