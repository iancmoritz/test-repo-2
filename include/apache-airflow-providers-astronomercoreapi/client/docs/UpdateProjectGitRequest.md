# UpdateProjectGitRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** |  | [optional] 
**dags_path** | **str** |  | [optional] 
**git_vendor_attributes** | [**UpdateProjectGitVendorAttributesRequest**](UpdateProjectGitVendorAttributesRequest.md) |  | [optional] 
**repo** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.update_project_git_request import UpdateProjectGitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProjectGitRequest from a JSON string
update_project_git_request_instance = UpdateProjectGitRequest.from_json(json)
# print the JSON string representation of the object
print UpdateProjectGitRequest.to_json()

# convert the object into a dict
update_project_git_request_dict = update_project_git_request_instance.to_dict()
# create an instance of UpdateProjectGitRequest from a dict
update_project_git_request_form_dict = update_project_git_request.from_dict(update_project_git_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


