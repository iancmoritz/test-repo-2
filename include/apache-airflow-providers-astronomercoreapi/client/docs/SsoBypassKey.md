# SsoBypassKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bypass_key** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**deleted_at** | **str** |  | [optional] 
**org_short_name** | **str** | Deprecated: orgShortName has been replaced with organizationShortName | [optional] 
**organization_id** | **str** |  | 
**organization_short_name** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.sso_bypass_key import SsoBypassKey

# TODO update the JSON string below
json = "{}"
# create an instance of SsoBypassKey from a JSON string
sso_bypass_key_instance = SsoBypassKey.from_json(json)
# print the JSON string representation of the object
print SsoBypassKey.to_json()

# convert the object into a dict
sso_bypass_key_dict = sso_bypass_key_instance.to_dict()
# create an instance of SsoBypassKey from a dict
sso_bypass_key_form_dict = sso_bypass_key.from_dict(sso_bypass_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


