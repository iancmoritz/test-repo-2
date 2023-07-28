# UpdateSsoConnectionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**SsoConnectionConfig**](SsoConnectionConfig.md) |  | 
**enabled** | **bool** |  | 
**idp_initiated_login_enabled** | **bool** |  | 
**jit_policy** | [**JitPolicy**](JitPolicy.md) |  | [optional] 
**managed_domains** | [**List[SsoConnectionManagedDomain]**](SsoConnectionManagedDomain.md) |  | 

## Example

```python
from astronomercoreapi.models.update_sso_connection_request import UpdateSsoConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSsoConnectionRequest from a JSON string
update_sso_connection_request_instance = UpdateSsoConnectionRequest.from_json(json)
# print the JSON string representation of the object
print UpdateSsoConnectionRequest.to_json()

# convert the object into a dict
update_sso_connection_request_dict = update_sso_connection_request_instance.to_dict()
# create an instance of UpdateSsoConnectionRequest from a dict
update_sso_connection_request_form_dict = update_sso_connection_request.from_dict(update_sso_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


