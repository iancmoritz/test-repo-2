# CreateWorkspaceApiTokenRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** |  | 
**role** | **str** |  | 
**token_expiry_period_in_days** | **int** |  | [optional] 

## Example

```python
from astronomercoreapi.models.create_workspace_api_token_request import CreateWorkspaceApiTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWorkspaceApiTokenRequest from a JSON string
create_workspace_api_token_request_instance = CreateWorkspaceApiTokenRequest.from_json(json)
# print the JSON string representation of the object
print CreateWorkspaceApiTokenRequest.to_json()

# convert the object into a dict
create_workspace_api_token_request_dict = create_workspace_api_token_request_instance.to_dict()
# create an instance of CreateWorkspaceApiTokenRequest from a dict
create_workspace_api_token_request_form_dict = create_workspace_api_token_request.from_dict(create_workspace_api_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


