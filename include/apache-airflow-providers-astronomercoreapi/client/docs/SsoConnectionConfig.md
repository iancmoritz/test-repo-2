# SsoConnectionConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_client_id** | **str** |  | [optional] 
**azure_client_secret** | **str** |  | [optional] 
**azure_domain_name** | **str** |  | [optional] 
**saml_sign_in_url** | **str** |  | [optional] 
**saml_sign_out_url** | **str** |  | [optional] 
**saml_signing_cert** | **str** |  | [optional] 
**strategy** | **str** |  | 

## Example

```python
from astronomercoreapi.models.sso_connection_config import SsoConnectionConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SsoConnectionConfig from a JSON string
sso_connection_config_instance = SsoConnectionConfig.from_json(json)
# print the JSON string representation of the object
print SsoConnectionConfig.to_json()

# convert the object into a dict
sso_connection_config_dict = sso_connection_config_instance.to_dict()
# create an instance of SsoConnectionConfig from a dict
sso_connection_config_form_dict = sso_connection_config.from_dict(sso_connection_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


