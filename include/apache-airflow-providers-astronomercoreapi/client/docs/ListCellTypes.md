# ListCellTypes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cell_types** | [**List[CellTypeMetadata]**](CellTypeMetadata.md) |  | 

## Example

```python
from astronomercoreapi.models.list_cell_types import ListCellTypes

# TODO update the JSON string below
json = "{}"
# create an instance of ListCellTypes from a JSON string
list_cell_types_instance = ListCellTypes.from_json(json)
# print the JSON string representation of the object
print ListCellTypes.to_json()

# convert the object into a dict
list_cell_types_dict = list_cell_types_instance.to_dict()
# create an instance of ListCellTypes from a dict
list_cell_types_form_dict = list_cell_types.from_dict(list_cell_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


