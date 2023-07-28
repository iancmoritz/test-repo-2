# astronomercoreapi.AuthzApi

All URIs are relative to *https://api.astronomer.io/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**has_permissions**](AuthzApi.md#has_permissions) | **POST** /authz/hasPermissions | Get current user permission information


# **has_permissions**
> HasPermissions has_permissions(body)

Get current user permission information

Get current user permission information

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.has_permissions import HasPermissions
from astronomercoreapi.models.has_permissions_request import HasPermissionsRequest
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
    api_instance = astronomercoreapi.AuthzApi(api_client)
    body = astronomercoreapi.HasPermissionsRequest() # HasPermissionsRequest | request body for get permissions

    try:
        # Get current user permission information
        api_response = api_instance.has_permissions(body)
        print("The response of AuthzApi->has_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthzApi->has_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HasPermissionsRequest**](HasPermissionsRequest.md)| request body for get permissions | 

### Return type

[**HasPermissions**](HasPermissions.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
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

