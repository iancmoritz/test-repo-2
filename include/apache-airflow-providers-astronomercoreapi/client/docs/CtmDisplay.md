# CtmDisplay


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.ctm_display import CtmDisplay

# TODO update the JSON string below
json = "{}"
# create an instance of CtmDisplay from a JSON string
ctm_display_instance = CtmDisplay.from_json(json)
# print the JSON string representation of the object
print CtmDisplay.to_json()

# convert the object into a dict
ctm_display_dict = ctm_display_instance.to_dict()
# create an instance of CtmDisplay from a dict
ctm_display_form_dict = ctm_display.from_dict(ctm_display_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


