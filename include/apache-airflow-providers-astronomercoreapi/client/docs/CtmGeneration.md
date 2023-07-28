# CtmGeneration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decorator** | [**CtmGenerationDecorator**](CtmGenerationDecorator.md) |  | [optional] 
**invoke** | [**CtmGenerationInvoke**](CtmGenerationInvoke.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from astronomercoreapi.models.ctm_generation import CtmGeneration

# TODO update the JSON string below
json = "{}"
# create an instance of CtmGeneration from a JSON string
ctm_generation_instance = CtmGeneration.from_json(json)
# print the JSON string representation of the object
print CtmGeneration.to_json()

# convert the object into a dict
ctm_generation_dict = ctm_generation_instance.to_dict()
# create an instance of CtmGeneration from a dict
ctm_generation_form_dict = ctm_generation.from_dict(ctm_generation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


