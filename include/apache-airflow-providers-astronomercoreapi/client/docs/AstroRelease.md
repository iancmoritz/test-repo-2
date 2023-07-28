# AstroRelease


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** |  | [optional] 
**release_date** | **str** |  | 
**url** | **str** |  | [optional] 
**version** | **str** |  | 

## Example

```python
from astronomercoreapi.models.astro_release import AstroRelease

# TODO update the JSON string below
json = "{}"
# create an instance of AstroRelease from a JSON string
astro_release_instance = AstroRelease.from_json(json)
# print the JSON string representation of the object
print AstroRelease.to_json()

# convert the object into a dict
astro_release_dict = astro_release_instance.to_dict()
# create an instance of AstroRelease from a dict
astro_release_form_dict = astro_release.from_dict(astro_release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


