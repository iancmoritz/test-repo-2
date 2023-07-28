# VRVariableRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_secret** | **bool** |  | 
**key** | **str** |  | 
**value** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.vr_variable_request import VRVariableRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VRVariableRequest from a JSON string
vr_variable_request_instance = VRVariableRequest.from_json(json)
# print the JSON string representation of the object
print VRVariableRequest.to_json()

# convert the object into a dict
vr_variable_request_dict = vr_variable_request_instance.to_dict()
# create an instance of VRVariableRequest from a dict
vr_variable_request_form_dict = vr_variable_request.from_dict(vr_variable_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


