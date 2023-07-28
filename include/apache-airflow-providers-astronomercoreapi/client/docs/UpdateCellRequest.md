# UpdateCellRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependencies_explicit** | **List[str]** |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | 
**type_config_forms** | **Dict[str, str]** |  | [optional] 
**type_configs** | **object** |  | [optional] 

## Example

```python
from astronomercoreapi.models.update_cell_request import UpdateCellRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCellRequest from a JSON string
update_cell_request_instance = UpdateCellRequest.from_json(json)
# print the JSON string representation of the object
print UpdateCellRequest.to_json()

# convert the object into a dict
update_cell_request_dict = update_cell_request_instance.to_dict()
# create an instance of UpdateCellRequest from a dict
update_cell_request_form_dict = update_cell_request.from_dict(update_cell_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


