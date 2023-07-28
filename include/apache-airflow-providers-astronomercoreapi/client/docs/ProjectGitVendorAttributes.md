# ProjectGitVendorAttributes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_dev_ops_organization** | **str** |  | [optional] 
**azure_dev_ops_project_id** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.project_git_vendor_attributes import ProjectGitVendorAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectGitVendorAttributes from a JSON string
project_git_vendor_attributes_instance = ProjectGitVendorAttributes.from_json(json)
# print the JSON string representation of the object
print ProjectGitVendorAttributes.to_json()

# convert the object into a dict
project_git_vendor_attributes_dict = project_git_vendor_attributes_instance.to_dict()
# create an instance of ProjectGitVendorAttributes from a dict
project_git_vendor_attributes_form_dict = project_git_vendor_attributes.from_dict(project_git_vendor_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


