# UpdateManagedDomainRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enforced_logins** | **List[str]** |  | 

## Example

```python
from astronomercoreapi.models.update_managed_domain_request import UpdateManagedDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateManagedDomainRequest from a JSON string
update_managed_domain_request_instance = UpdateManagedDomainRequest.from_json(json)
# print the JSON string representation of the object
print UpdateManagedDomainRequest.to_json()

# convert the object into a dict
update_managed_domain_request_dict = update_managed_domain_request_instance.to_dict()
# create an instance of UpdateManagedDomainRequest from a dict
update_managed_domain_request_form_dict = update_managed_domain_request.from_dict(update_managed_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


