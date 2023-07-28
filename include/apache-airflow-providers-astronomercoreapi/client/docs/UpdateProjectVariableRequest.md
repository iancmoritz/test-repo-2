# UpdateProjectVariableRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_secret** | **bool** |  | 
**key** | **str** |  | 
**type** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from astronomercoreapi.models.update_project_variable_request import UpdateProjectVariableRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProjectVariableRequest from a JSON string
update_project_variable_request_instance = UpdateProjectVariableRequest.from_json(json)
# print the JSON string representation of the object
print UpdateProjectVariableRequest.to_json()

# convert the object into a dict
update_project_variable_request_dict = update_project_variable_request_instance.to_dict()
# create an instance of UpdateProjectVariableRequest from a dict
update_project_variable_request_form_dict = update_project_variable_request.from_dict(update_project_variable_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


