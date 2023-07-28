# CreateManagedDomainRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enforced_logins** | **List[str]** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from astronomercoreapi.models.create_managed_domain_request import CreateManagedDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateManagedDomainRequest from a JSON string
create_managed_domain_request_instance = CreateManagedDomainRequest.from_json(json)
# print the JSON string representation of the object
print CreateManagedDomainRequest.to_json()

# convert the object into a dict
create_managed_domain_request_dict = create_managed_domain_request_instance.to_dict()
# create an instance of CreateManagedDomainRequest from a dict
create_managed_domain_request_form_dict = create_managed_domain_request.from_dict(create_managed_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


