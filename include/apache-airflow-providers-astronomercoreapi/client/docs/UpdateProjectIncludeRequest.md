# UpdateProjectIncludeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_sync_disabled** | **bool** |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from astronomercoreapi.models.update_project_include_request import UpdateProjectIncludeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProjectIncludeRequest from a JSON string
update_project_include_request_instance = UpdateProjectIncludeRequest.from_json(json)
# print the JSON string representation of the object
print UpdateProjectIncludeRequest.to_json()

# convert the object into a dict
update_project_include_request_dict = update_project_include_request_instance.to_dict()
# create an instance of UpdateProjectIncludeRequest from a dict
update_project_include_request_form_dict = update_project_include_request.from_dict(update_project_include_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


