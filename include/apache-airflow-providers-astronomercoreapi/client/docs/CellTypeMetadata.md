# CellTypeMetadata


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
from astronomercoreapi.models.cell_type_metadata import CellTypeMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CellTypeMetadata from a JSON string
cell_type_metadata_instance = CellTypeMetadata.from_json(json)
# print the JSON string representation of the object
print CellTypeMetadata.to_json()

# convert the object into a dict
cell_type_metadata_dict = cell_type_metadata_instance.to_dict()
# create an instance of CellTypeMetadata from a dict
cell_type_metadata_form_dict = cell_type_metadata.from_dict(cell_type_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


