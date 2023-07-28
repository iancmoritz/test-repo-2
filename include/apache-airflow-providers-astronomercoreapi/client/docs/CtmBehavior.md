# CtmBehavior


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_from_graph** | **bool** |  | [optional] 
**generates_data** | **bool** |  | [optional] 
**naming_strategy** | **str** |  | [optional] 
**returns_raw_value** | **bool** |  | [optional] 
**runnable** | **bool** |  | [optional] 

## Example

```python
from astronomercoreapi.models.ctm_behavior import CtmBehavior

# TODO update the JSON string below
json = "{}"
# create an instance of CtmBehavior from a JSON string
ctm_behavior_instance = CtmBehavior.from_json(json)
# print the JSON string representation of the object
print CtmBehavior.to_json()

# convert the object into a dict
ctm_behavior_dict = ctm_behavior_instance.to_dict()
# create an instance of CtmBehavior from a dict
ctm_behavior_form_dict = ctm_behavior.from_dict(ctm_behavior_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


