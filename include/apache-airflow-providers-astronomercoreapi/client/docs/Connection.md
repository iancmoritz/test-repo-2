# Connection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_name** | **str** |  | 
**created_at** | **datetime** |  | 
**created_by_user** | [**BasicSubjectProfile**](BasicSubjectProfile.md) |  | 
**extra** | **Dict[str, str]** |  | [optional] 
**host** | **str** |  | [optional] 
**id** | **str** |  | 
**login** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**var_schema** | **str** |  | [optional] 
**type** | **str** |  | 
**updated_at** | **datetime** |  | 
**updated_by_user** | [**BasicSubjectProfile**](BasicSubjectProfile.md) |  | 

## Example

```python
from astronomercoreapi.models.connection import Connection

# TODO update the JSON string below
json = "{}"
# create an instance of Connection from a JSON string
connection_instance = Connection.from_json(json)
# print the JSON string representation of the object
print Connection.to_json()

# convert the object into a dict
connection_dict = connection_instance.to_dict()
# create an instance of Connection from a dict
connection_form_dict = connection.from_dict(connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


