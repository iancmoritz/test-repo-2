# CtmConfigValidity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | [**CtmConfigDomain**](CtmConfigDomain.md) |  | [optional] 
**mandatory** | **bool** |  | [optional] 

## Example

```python
from astronomercoreapi.models.ctm_config_validity import CtmConfigValidity

# TODO update the JSON string below
json = "{}"
# create an instance of CtmConfigValidity from a JSON string
ctm_config_validity_instance = CtmConfigValidity.from_json(json)
# print the JSON string representation of the object
print CtmConfigValidity.to_json()

# convert the object into a dict
ctm_config_validity_dict = ctm_config_validity_instance.to_dict()
# create an instance of CtmConfigValidity from a dict
ctm_config_validity_form_dict = ctm_config_validity.from_dict(ctm_config_validity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


