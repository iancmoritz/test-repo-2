# ProjectInclude


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_sync_disabled** | **bool** |  | [optional] 
**git** | [**ProjectIncludesGit**](ProjectIncludesGit.md) |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from astronomercoreapi.models.project_include import ProjectInclude

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectInclude from a JSON string
project_include_instance = ProjectInclude.from_json(json)
# print the JSON string representation of the object
print ProjectInclude.to_json()

# convert the object into a dict
project_include_dict = project_include_instance.to_dict()
# create an instance of ProjectInclude from a dict
project_include_form_dict = project_include.from_dict(project_include_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


