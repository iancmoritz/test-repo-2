# ProjectVariable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_secret** | **bool** |  | 
**key** | **str** |  | 
**type** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from astronomercoreapi.models.project_variable import ProjectVariable

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectVariable from a JSON string
project_variable_instance = ProjectVariable.from_json(json)
# print the JSON string representation of the object
print ProjectVariable.to_json()

# convert the object into a dict
project_variable_dict = project_variable_instance.to_dict()
# create an instance of ProjectVariable from a dict
project_variable_form_dict = project_variable.from_dict(project_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


