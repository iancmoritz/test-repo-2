# CtmConfigDisplay


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | [**CtmValue**](CtmValue.md) |  | [optional] 
**description** | **str** |  | [optional] 
**example** | [**CtmValue**](CtmValue.md) |  | [optional] 
**fixed_width_font** | **bool** |  | [optional] 
**highlight_language** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**num_lines** | **int** |  | [optional] 
**raw_type** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.ctm_config_display import CtmConfigDisplay

# TODO update the JSON string below
json = "{}"
# create an instance of CtmConfigDisplay from a JSON string
ctm_config_display_instance = CtmConfigDisplay.from_json(json)
# print the JSON string representation of the object
print CtmConfigDisplay.to_json()

# convert the object into a dict
ctm_config_display_dict = ctm_config_display_instance.to_dict()
# create an instance of CtmConfigDisplay from a dict
ctm_config_display_form_dict = ctm_config_display.from_dict(ctm_config_display_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


