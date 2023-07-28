# ValidateCellType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**valid** | **bool** |  | 

## Example

```python
from astronomercoreapi.models.validate_cell_type import ValidateCellType

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateCellType from a JSON string
validate_cell_type_instance = ValidateCellType.from_json(json)
# print the JSON string representation of the object
print ValidateCellType.to_json()

# convert the object into a dict
validate_cell_type_dict = validate_cell_type_instance.to_dict()
# create an instance of ValidateCellType from a dict
validate_cell_type_form_dict = validate_cell_type.from_dict(validate_cell_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


