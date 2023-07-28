# BasicSubjectProfile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_token_name** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**id** | **str** |  | 
**subject_type** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.basic_subject_profile import BasicSubjectProfile

# TODO update the JSON string below
json = "{}"
# create an instance of BasicSubjectProfile from a JSON string
basic_subject_profile_instance = BasicSubjectProfile.from_json(json)
# print the JSON string representation of the object
print BasicSubjectProfile.to_json()

# convert the object into a dict
basic_subject_profile_dict = basic_subject_profile_instance.to_dict()
# create an instance of BasicSubjectProfile from a dict
basic_subject_profile_form_dict = basic_subject_profile.from_dict(basic_subject_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


