# astronomercoreapi.AuthApi

All URIs are relative to *https://api.astronomer.io/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_invite**](AuthApi.md#get_user_invite) | **GET** /auth/invites/{inviteId} | Get user invite
[**validate_sso_bypass_key**](AuthApi.md#validate_sso_bypass_key) | **GET** /auth/sso-bypass-keys/{ssoBypassKey} | Get organization info from SSO bypass key


# **get_user_invite**
> Invite get_user_invite(invite_id)

Get user invite

Get user invite

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.invite import Invite
from astronomercoreapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astronomer.io/v1alpha1
# See configuration.py for a list of all supported configuration parameters.
configuration = astronomercoreapi.Configuration(
    host = "https://api.astronomer.io/v1alpha1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with astronomercoreapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astronomercoreapi.AuthApi(api_client)
    invite_id = 'invite_id_example' # str | invite ID or auth0 ticket ID

    try:
        # Get user invite
        api_response = api_instance.get_user_invite(invite_id)
        print("The response of AuthApi->get_user_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_user_invite: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_id** | **str**| invite ID or auth0 ticket ID | 

### Return type

[**Invite**](Invite.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_sso_bypass_key**
> SsoBypassKey validate_sso_bypass_key(sso_bypass_key)

Get organization info from SSO bypass key

Get organization info from SSO bypass key

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.sso_bypass_key import SsoBypassKey
from astronomercoreapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astronomer.io/v1alpha1
# See configuration.py for a list of all supported configuration parameters.
configuration = astronomercoreapi.Configuration(
    host = "https://api.astronomer.io/v1alpha1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with astronomercoreapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astronomercoreapi.AuthApi(api_client)
    sso_bypass_key = 'sso_bypass_key_example' # str | SSO bypass key for organization

    try:
        # Get organization info from SSO bypass key
        api_response = api_instance.validate_sso_bypass_key(sso_bypass_key)
        print("The response of AuthApi->validate_sso_bypass_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->validate_sso_bypass_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sso_bypass_key** | **str**| SSO bypass key for organization | 

### Return type

[**SsoBypassKey**](SsoBypassKey.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

