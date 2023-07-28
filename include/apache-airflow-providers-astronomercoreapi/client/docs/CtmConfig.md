# CtmConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicability** | [**CtmConfigApplicability**](CtmConfigApplicability.md) |  | [optional] 
**data_type** | **str** |  | 
**display** | [**CtmConfigDisplay**](CtmConfigDisplay.md) |  | [optional] 
**generation** | [**CtmConfigGeneration**](CtmConfigGeneration.md) |  | [optional] 
**key** | **str** |  | 
**validity** | [**CtmConfigValidity**](CtmConfigValidity.md) |  | [optional] 

## Example

```python
from astronomercoreapi.models.ctm_config import CtmConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CtmConfig from a JSON string
ctm_config_instance = CtmConfig.from_json(json)
# print the JSON string representation of the object
print CtmConfig.to_json()

# convert the object into a dict
ctm_config_dict = ctm_config_instance.to_dict()
# create an instance of CtmConfig from a dict
ctm_config_form_dict = ctm_config.from_dict(ctm_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


