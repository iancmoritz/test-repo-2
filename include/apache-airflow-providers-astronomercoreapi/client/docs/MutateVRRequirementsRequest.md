# MutateVRRequirementsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requirements** | **List[str]** |  | 

## Example

```python
from astronomercoreapi.models.mutate_vr_requirements_request import MutateVRRequirementsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MutateVRRequirementsRequest from a JSON string
mutate_vr_requirements_request_instance = MutateVRRequirementsRequest.from_json(json)
# print the JSON string representation of the object
print MutateVRRequirementsRequest.to_json()

# convert the object into a dict
mutate_vr_requirements_request_dict = mutate_vr_requirements_request_instance.to_dict()
# create an instance of MutateVRRequirementsRequest from a dict
mutate_vr_requirements_request_form_dict = mutate_vr_requirements_request.from_dict(mutate_vr_requirements_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


