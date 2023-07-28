# VRRequirements


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desired_requirements** | **List[str]** |  | 
**requirements** | **List[str]** |  | 
**validation_status** | **str** |  | 

## Example

```python
from astronomercoreapi.models.vr_requirements import VRRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of VRRequirements from a JSON string
vr_requirements_instance = VRRequirements.from_json(json)
# print the JSON string representation of the object
print VRRequirements.to_json()

# convert the object into a dict
vr_requirements_dict = vr_requirements_instance.to_dict()
# create an instance of VRRequirements from a dict
vr_requirements_form_dict = vr_requirements.from_dict(vr_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


