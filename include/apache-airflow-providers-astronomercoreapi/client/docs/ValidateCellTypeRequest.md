# ValidateCellTypeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**behavior** | [**CtmBehavior**](CtmBehavior.md) |  | [optional] 
**configs** | [**List[CtmConfig]**](CtmConfig.md) |  | [optional] 
**display** | [**CtmDisplay**](CtmDisplay.md) |  | [optional] 
**generation** | [**CtmGeneration**](CtmGeneration.md) |  | [optional] 
**name** | **str** |  | 

## Example

```python
from astronomercoreapi.models.validate_cell_type_request import ValidateCellTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateCellTypeRequest from a JSON string
validate_cell_type_request_instance = ValidateCellTypeRequest.from_json(json)
# print the JSON string representation of the object
print ValidateCellTypeRequest.to_json()

# convert the object into a dict
validate_cell_type_request_dict = validate_cell_type_request_instance.to_dict()
# create an instance of ValidateCellTypeRequest from a dict
validate_cell_type_request_form_dict = validate_cell_type_request.from_dict(validate_cell_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


