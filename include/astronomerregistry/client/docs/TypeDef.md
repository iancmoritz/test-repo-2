# TypeDef


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotation_type** | **str** |  | [optional] 
**raw_annotation** | **str** |  | [optional] 
**type_variables** | [**List[TypeDef]**](TypeDef.md) |  | [optional] 

## Example

```python
from astronomerregistry.models.type_def import TypeDef

# TODO update the JSON string below
json = "{}"
# create an instance of TypeDef from a JSON string
type_def_instance = TypeDef.from_json(json)
# print the JSON string representation of the object
print TypeDef.to_json()

# convert the object into a dict
type_def_dict = type_def_instance.to_dict()
# create an instance of TypeDef from a dict
type_def_form_dict = type_def.from_dict(type_def_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


