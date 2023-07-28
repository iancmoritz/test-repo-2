# CreateSsoConnectionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth0_connection_name** | **str** |  | 
**configuration** | [**SsoConnectionConfig**](SsoConnectionConfig.md) |  | 
**idp_initiated_login_enabled** | **bool** |  | [optional] 
**jit_policy** | [**JitPolicy**](JitPolicy.md) |  | [optional] 
**managed_domains** | [**List[SsoConnectionManagedDomain]**](SsoConnectionManagedDomain.md) |  | 

## Example

```python
from astronomercoreapi.models.create_sso_connection_request import CreateSsoConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSsoConnectionRequest from a JSON string
create_sso_connection_request_instance = CreateSsoConnectionRequest.from_json(json)
# print the JSON string representation of the object
print CreateSsoConnectionRequest.to_json()

# convert the object into a dict
create_sso_connection_request_dict = create_sso_connection_request_instance.to_dict()
# create an instance of CreateSsoConnectionRequest from a dict
create_sso_connection_request_form_dict = create_sso_connection_request.from_dict(create_sso_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


