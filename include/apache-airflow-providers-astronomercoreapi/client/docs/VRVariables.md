# VRVariables


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variables** | [**List[VRVariable]**](VRVariable.md) |  | 

## Example

```python
from astronomercoreapi.models.vr_variables import VRVariables

# TODO update the JSON string below
json = "{}"
# create an instance of VRVariables from a JSON string
vr_variables_instance = VRVariables.from_json(json)
# print the JSON string representation of the object
print VRVariables.to_json()

# convert the object into a dict
vr_variables_dict = vr_variables_instance.to_dict()
# create an instance of VRVariables from a dict
vr_variables_form_dict = vr_variables.from_dict(vr_variables_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


