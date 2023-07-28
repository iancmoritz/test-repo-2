# GetCellType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**definition** | [**CtmDefinition**](CtmDefinition.md) |  | [optional] 
**name** | **str** |  | 
**organization_id** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**source** | **str** |  | 
**updated_at** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 
**workspace_id** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.get_cell_type import GetCellType

# TODO update the JSON string below
json = "{}"
# create an instance of GetCellType from a JSON string
get_cell_type_instance = GetCellType.from_json(json)
# print the JSON string representation of the object
print GetCellType.to_json()

# convert the object into a dict
get_cell_type_dict = get_cell_type_instance.to_dict()
# create an instance of GetCellType from a dict
get_cell_type_form_dict = get_cell_type.from_dict(get_cell_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


