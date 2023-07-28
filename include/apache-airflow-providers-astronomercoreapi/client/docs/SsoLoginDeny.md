# SsoLoginDeny


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connections** | **List[str]** |  | [optional] 
**message** | **str** |  | 
**reason** | **str** |  | 

## Example

```python
from astronomercoreapi.models.sso_login_deny import SsoLoginDeny

# TODO update the JSON string below
json = "{}"
# create an instance of SsoLoginDeny from a JSON string
sso_login_deny_instance = SsoLoginDeny.from_json(json)
# print the JSON string representation of the object
print SsoLoginDeny.to_json()

# convert the object into a dict
sso_login_deny_dict = sso_login_deny_instance.to_dict()
# create an instance of SsoLoginDeny from a dict
sso_login_deny_form_dict = sso_login_deny.from_dict(sso_login_deny_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


