# CreateOrganizationApiTokenRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** |  | 
**role** | **str** |  | 
**token_expiry_period_in_days** | **int** |  | [optional] 

## Example

```python
from astronomercoreapi.models.create_organization_api_token_request import CreateOrganizationApiTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationApiTokenRequest from a JSON string
create_organization_api_token_request_instance = CreateOrganizationApiTokenRequest.from_json(json)
# print the JSON string representation of the object
print CreateOrganizationApiTokenRequest.to_json()

# convert the object into a dict
create_organization_api_token_request_dict = create_organization_api_token_request_instance.to_dict()
# create an instance of CreateOrganizationApiTokenRequest from a dict
create_organization_api_token_request_form_dict = create_organization_api_token_request.from_dict(create_organization_api_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


