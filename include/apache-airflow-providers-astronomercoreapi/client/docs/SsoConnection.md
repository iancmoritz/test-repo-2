# SsoConnection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth0_connection_id** | **str** |  | 
**auth0_connection_name** | **str** |  | 
**configuration** | [**SsoConnectionConfig**](SsoConnectionConfig.md) |  | 
**enabled** | **bool** |  | 
**id** | **str** |  | 
**jit_policy** | [**JitPolicy**](JitPolicy.md) |  | [optional] 
**managed_domains** | [**List[ManagedDomain]**](ManagedDomain.md) |  | 
**organization_id** | **str** |  | 

## Example

```python
from astronomercoreapi.models.sso_connection import SsoConnection

# TODO update the JSON string below
json = "{}"
# create an instance of SsoConnection from a JSON string
sso_connection_instance = SsoConnection.from_json(json)
# print the JSON string representation of the object
print SsoConnection.to_json()

# convert the object into a dict
sso_connection_dict = sso_connection_instance.to_dict()
# create an instance of SsoConnection from a dict
sso_connection_form_dict = sso_connection.from_dict(sso_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


