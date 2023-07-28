# UpdateCellTypeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**behavior** | [**CtmBehavior**](CtmBehavior.md) |  | [optional] 
**configs** | [**List[CtmConfig]**](CtmConfig.md) |  | [optional] 
**display** | [**CtmDisplay**](CtmDisplay.md) |  | [optional] 
**generation** | [**CtmGeneration**](CtmGeneration.md) |  | [optional] 

## Example

```python
from astronomercoreapi.models.update_cell_type_request import UpdateCellTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCellTypeRequest from a JSON string
update_cell_type_request_instance = UpdateCellTypeRequest.from_json(json)
# print the JSON string representation of the object
print UpdateCellTypeRequest.to_json()

# convert the object into a dict
update_cell_type_request_dict = update_cell_type_request_instance.to_dict()
# create an instance of UpdateCellTypeRequest from a dict
update_cell_type_request_form_dict = update_cell_type_request.from_dict(update_cell_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


