# UpdateWorkspaceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_only_deployments_default** | **bool** |  | 
**description** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from astronomercoreapi.models.update_workspace_request import UpdateWorkspaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkspaceRequest from a JSON string
update_workspace_request_instance = UpdateWorkspaceRequest.from_json(json)
# print the JSON string representation of the object
print UpdateWorkspaceRequest.to_json()

# convert the object into a dict
update_workspace_request_dict = update_workspace_request_instance.to_dict()
# create an instance of UpdateWorkspaceRequest from a dict
update_workspace_request_form_dict = update_workspace_request.from_dict(update_workspace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


