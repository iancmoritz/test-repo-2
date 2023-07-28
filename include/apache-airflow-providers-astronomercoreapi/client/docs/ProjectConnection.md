# ProjectConnection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra** | **Dict[str, str]** |  | [optional] 
**host** | **str** |  | [optional] 
**id** | **str** |  | 
**login** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**var_schema** | **str** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from astronomercoreapi.models.project_connection import ProjectConnection

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectConnection from a JSON string
project_connection_instance = ProjectConnection.from_json(json)
# print the JSON string representation of the object
print ProjectConnection.to_json()

# convert the object into a dict
project_connection_dict = project_connection_instance.to_dict()
# create an instance of ProjectConnection from a dict
project_connection_form_dict = project_connection.from_dict(project_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


