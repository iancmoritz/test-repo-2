# UpdateOrganizationApiTokenRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**name** | **str** |  | 
**roles** | [**UpdateOrganizationApiTokenRoles**](UpdateOrganizationApiTokenRoles.md) |  | 

## Example

```python
from astronomercoreapi.models.update_organization_api_token_request import UpdateOrganizationApiTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrganizationApiTokenRequest from a JSON string
update_organization_api_token_request_instance = UpdateOrganizationApiTokenRequest.from_json(json)
# print the JSON string representation of the object
print UpdateOrganizationApiTokenRequest.to_json()

# convert the object into a dict
update_organization_api_token_request_dict = update_organization_api_token_request_instance.to_dict()
# create an instance of UpdateOrganizationApiTokenRequest from a dict
update_organization_api_token_request_form_dict = update_organization_api_token_request.from_dict(update_organization_api_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


