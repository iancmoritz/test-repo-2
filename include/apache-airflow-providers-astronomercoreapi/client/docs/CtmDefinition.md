# CtmDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**behavior** | [**CtmBehavior**](CtmBehavior.md) |  | [optional] 
**configs** | [**List[CtmConfig]**](CtmConfig.md) |  | [optional] 
**display** | [**CtmDisplay**](CtmDisplay.md) |  | [optional] 
**generation** | [**CtmGeneration**](CtmGeneration.md) |  | [optional] 

## Example

```python
from astronomercoreapi.models.ctm_definition import CtmDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of CtmDefinition from a JSON string
ctm_definition_instance = CtmDefinition.from_json(json)
# print the JSON string representation of the object
print CtmDefinition.to_json()

# convert the object into a dict
ctm_definition_dict = ctm_definition_instance.to_dict()
# create an instance of CtmDefinition from a dict
ctm_definition_form_dict = ctm_definition.from_dict(ctm_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


