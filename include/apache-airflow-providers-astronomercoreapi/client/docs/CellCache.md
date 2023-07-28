# CellCache


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicable** | **bool** |  | 
**available** | **bool** |  | [optional] 
**dirty** | **bool** |  | [optional] 
**dirty_reason** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.cell_cache import CellCache

# TODO update the JSON string below
json = "{}"
# create an instance of CellCache from a JSON string
cell_cache_instance = CellCache.from_json(json)
# print the JSON string representation of the object
print CellCache.to_json()

# convert the object into a dict
cell_cache_dict = cell_cache_instance.to_dict()
# create an instance of CellCache from a dict
cell_cache_form_dict = cell_cache.from_dict(cell_cache_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


