# UpdateProjectGitVendorAttributesRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_dev_ops_organization** | **str** |  | [optional] 
**azure_dev_ops_project_id** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.update_project_git_vendor_attributes_request import UpdateProjectGitVendorAttributesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProjectGitVendorAttributesRequest from a JSON string
update_project_git_vendor_attributes_request_instance = UpdateProjectGitVendorAttributesRequest.from_json(json)
# print the JSON string representation of the object
print UpdateProjectGitVendorAttributesRequest.to_json()

# convert the object into a dict
update_project_git_vendor_attributes_request_dict = update_project_git_vendor_attributes_request_instance.to_dict()
# create an instance of UpdateProjectGitVendorAttributesRequest from a dict
update_project_git_vendor_attributes_request_form_dict = update_project_git_vendor_attributes_request.from_dict(update_project_git_vendor_attributes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


