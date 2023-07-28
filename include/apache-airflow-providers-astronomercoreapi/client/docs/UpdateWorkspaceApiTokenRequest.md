# UpdateWorkspaceApiTokenRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**name** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from astronomercoreapi.models.update_workspace_api_token_request import UpdateWorkspaceApiTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkspaceApiTokenRequest from a JSON string
update_workspace_api_token_request_instance = UpdateWorkspaceApiTokenRequest.from_json(json)
# print the JSON string representation of the object
print UpdateWorkspaceApiTokenRequest.to_json()

# convert the object into a dict
update_workspace_api_token_request_dict = update_workspace_api_token_request_instance.to_dict()
# create an instance of UpdateWorkspaceApiTokenRequest from a dict
update_workspace_api_token_request_form_dict = update_workspace_api_token_request.from_dict(update_workspace_api_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


