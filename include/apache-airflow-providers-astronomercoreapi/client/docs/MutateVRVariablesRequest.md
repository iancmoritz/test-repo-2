# MutateVRVariablesRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variables** | [**List[VRVariableRequest]**](VRVariableRequest.md) |  | 

## Example

```python
from astronomercoreapi.models.mutate_vr_variables_request import MutateVRVariablesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MutateVRVariablesRequest from a JSON string
mutate_vr_variables_request_instance = MutateVRVariablesRequest.from_json(json)
# print the JSON string representation of the object
print MutateVRVariablesRequest.to_json()

# convert the object into a dict
mutate_vr_variables_request_dict = mutate_vr_variables_request_instance.to_dict()
# create an instance of MutateVRVariablesRequest from a dict
mutate_vr_variables_request_form_dict = mutate_vr_variables_request.from_dict(mutate_vr_variables_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


