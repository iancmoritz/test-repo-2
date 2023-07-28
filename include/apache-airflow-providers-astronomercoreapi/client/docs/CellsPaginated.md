# CellsPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cell_types** | [**List[CellTypeMetadata]**](CellTypeMetadata.md) |  | [optional] 
**cells** | [**List[Cell]**](Cell.md) |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**total_count** | **int** |  | 

## Example

```python
from astronomercoreapi.models.cells_paginated import CellsPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of CellsPaginated from a JSON string
cells_paginated_instance = CellsPaginated.from_json(json)
# print the JSON string representation of the object
print CellsPaginated.to_json()

# convert the object into a dict
cells_paginated_dict = cells_paginated_instance.to_dict()
# create an instance of CellsPaginated from a dict
cells_paginated_form_dict = cells_paginated.from_dict(cells_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


