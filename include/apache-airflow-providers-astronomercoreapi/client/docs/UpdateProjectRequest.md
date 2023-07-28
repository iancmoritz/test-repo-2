# UpdateProjectRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connections** | [**List[UpdateProjectConnectionRequest]**](UpdateProjectConnectionRequest.md) |  | [optional] 
**description** | **str** |  | [optional] 
**git** | [**UpdateProjectGitRequest**](UpdateProjectGitRequest.md) |  | [optional] 
**includes** | [**List[UpdateProjectIncludeRequest]**](UpdateProjectIncludeRequest.md) |  | [optional] 
**name** | **str** |  | 
**requirements** | **List[str]** |  | [optional] 
**variables** | [**List[UpdateProjectVariableRequest]**](UpdateProjectVariableRequest.md) |  | [optional] 

## Example

```python
from astronomercoreapi.models.update_project_request import UpdateProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProjectRequest from a JSON string
update_project_request_instance = UpdateProjectRequest.from_json(json)
# print the JSON string representation of the object
print UpdateProjectRequest.to_json()

# convert the object into a dict
update_project_request_dict = update_project_request_instance.to_dict()
# create an instance of UpdateProjectRequest from a dict
update_project_request_form_dict = update_project_request.from_dict(update_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


