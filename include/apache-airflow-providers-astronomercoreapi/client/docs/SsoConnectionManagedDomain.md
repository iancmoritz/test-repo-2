# SsoConnectionManagedDomain


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from astronomercoreapi.models.sso_connection_managed_domain import SsoConnectionManagedDomain

# TODO update the JSON string below
json = "{}"
# create an instance of SsoConnectionManagedDomain from a JSON string
sso_connection_managed_domain_instance = SsoConnectionManagedDomain.from_json(json)
# print the JSON string representation of the object
print SsoConnectionManagedDomain.to_json()

# convert the object into a dict
sso_connection_managed_domain_dict = sso_connection_managed_domain_instance.to_dict()
# create an instance of SsoConnectionManagedDomain from a dict
sso_connection_managed_domain_form_dict = sso_connection_managed_domain.from_dict(sso_connection_managed_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


