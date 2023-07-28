# SsoLoginCallback


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token_claims** | **Dict[str, str]** |  | [optional] 
**deny** | [**SsoLoginDeny**](SsoLoginDeny.md) |  | [optional] 
**id_token_claims** | **Dict[str, str]** |  | [optional] 
**user_meta_data** | **object** |  | [optional] 

## Example

```python
from astronomercoreapi.models.sso_login_callback import SsoLoginCallback

# TODO update the JSON string below
json = "{}"
# create an instance of SsoLoginCallback from a JSON string
sso_login_callback_instance = SsoLoginCallback.from_json(json)
# print the JSON string representation of the object
print SsoLoginCallback.to_json()

# convert the object into a dict
sso_login_callback_dict = sso_login_callback_instance.to_dict()
# create an instance of SsoLoginCallback from a dict
sso_login_callback_form_dict = sso_login_callback.from_dict(sso_login_callback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


