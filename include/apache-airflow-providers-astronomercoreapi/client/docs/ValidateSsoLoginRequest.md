# ValidateSsoLoginRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**PostLoginEvent**](PostLoginEvent.md) |  | 

## Example

```python
from astronomercoreapi.models.validate_sso_login_request import ValidateSsoLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateSsoLoginRequest from a JSON string
validate_sso_login_request_instance = ValidateSsoLoginRequest.from_json(json)
# print the JSON string representation of the object
print ValidateSsoLoginRequest.to_json()

# convert the object into a dict
validate_sso_login_request_dict = validate_sso_login_request_instance.to_dict()
# create an instance of ValidateSsoLoginRequest from a dict
validate_sso_login_request_form_dict = validate_sso_login_request.from_dict(validate_sso_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


