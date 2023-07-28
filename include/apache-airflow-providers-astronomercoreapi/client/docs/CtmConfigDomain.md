# CtmConfigDomain


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | 
**values_string_list** | **List[str]** |  | [optional] 

## Example

```python
from astronomercoreapi.models.ctm_config_domain import CtmConfigDomain

# TODO update the JSON string below
json = "{}"
# create an instance of CtmConfigDomain from a JSON string
ctm_config_domain_instance = CtmConfigDomain.from_json(json)
# print the JSON string representation of the object
print CtmConfigDomain.to_json()

# convert the object into a dict
ctm_config_domain_dict = ctm_config_domain_instance.to_dict()
# create an instance of CtmConfigDomain from a dict
ctm_config_domain_form_dict = ctm_config_domain.from_dict(ctm_config_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


