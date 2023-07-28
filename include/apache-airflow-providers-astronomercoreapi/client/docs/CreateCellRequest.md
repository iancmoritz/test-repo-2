# CreateCellRequest


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
from astronomercoreapi.models.create_cell_request import CreateCellRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCellRequest from a JSON string
create_cell_request_instance = CreateCellRequest.from_json(json)
# print the JSON string representation of the object
print CreateCellRequest.to_json()

# convert the object into a dict
create_cell_request_dict = create_cell_request_instance.to_dict()
# create an instance of CreateCellRequest from a dict
create_cell_request_form_dict = create_cell_request.from_dict(create_cell_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


