# VRVariable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**created_by_user** | [**BasicSubjectProfile**](BasicSubjectProfile.md) |  | 
**is_secret** | **bool** |  | 
**key** | **str** |  | 
**updated_at** | **datetime** |  | 
**updated_by_user** | [**BasicSubjectProfile**](BasicSubjectProfile.md) |  | 
**value** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.vr_variable import VRVariable

# TODO update the JSON string below
json = "{}"
# create an instance of VRVariable from a JSON string
vr_variable_instance = VRVariable.from_json(json)
# print the JSON string representation of the object
print VRVariable.to_json()

# convert the object into a dict
vr_variable_dict = vr_variable_instance.to_dict()
# create an instance of VRVariable from a dict
vr_variable_form_dict = vr_variable.from_dict(vr_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


