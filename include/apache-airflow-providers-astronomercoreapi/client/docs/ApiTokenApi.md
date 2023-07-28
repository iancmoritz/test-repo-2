# astronomercoreapi.ApiTokenApi

All URIs are relative to *https://api.astronomer.io/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization_api_token**](ApiTokenApi.md#create_organization_api_token) | **POST** /organizations/{organizationId}/api-tokens | Create Organization API token
[**create_workspace_api_token**](ApiTokenApi.md#create_workspace_api_token) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/api-tokens | Create Workspace API token
[**delete_organization_api_token**](ApiTokenApi.md#delete_organization_api_token) | **DELETE** /organizations/{organizationId}/api-tokens/{apiTokenId} | Delete organization API token
[**delete_workspace_api_token**](ApiTokenApi.md#delete_workspace_api_token) | **DELETE** /organizations/{organizationId}/workspaces/{workspaceId}/api-tokens/{apiTokenId} | Delete Workspace API token
[**get_organization_api_token**](ApiTokenApi.md#get_organization_api_token) | **GET** /organizations/{organizationId}/api-tokens/{apiTokenId} | Get Organization API token
[**get_workspace_api_token**](ApiTokenApi.md#get_workspace_api_token) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/api-tokens/{apiTokenId} | Get Workspace API token
[**list_organization_api_tokens**](ApiTokenApi.md#list_organization_api_tokens) | **GET** /organizations/{organizationId}/api-tokens | List Organization API tokens
[**list_workspace_api_tokens**](ApiTokenApi.md#list_workspace_api_tokens) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/api-tokens | List Workspace API tokens
[**rotate_organization_api_token**](ApiTokenApi.md#rotate_organization_api_token) | **POST** /organizations/{organizationId}/api-tokens/{apiTokenId}/rotate | Rotate organization API token
[**rotate_workspace_api_token**](ApiTokenApi.md#rotate_workspace_api_token) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/api-tokens/{apiTokenId}/rotate | Rotate Workspace API token
[**update_organization_api_token**](ApiTokenApi.md#update_organization_api_token) | **POST** /organizations/{organizationId}/api-tokens/{apiTokenId} | Update Organization API token
[**update_workspace_api_token**](ApiTokenApi.md#update_workspace_api_token) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/api-tokens/{apiTokenId} | Update Workspace API token


# **create_organization_api_token**
> ApiToken create_organization_api_token(organization_id, body)

Create Organization API token

Create Organization API token

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.api_token import ApiToken
from astronomercoreapi.models.create_organization_api_token_request import CreateOrganizationApiTokenRequest
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
    api_instance = astronomercoreapi.ApiTokenApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    body = astronomercoreapi.CreateOrganizationApiTokenRequest() # CreateOrganizationApiTokenRequest | request body for creating an organization API token

    try:
        # Create Organization API token
        api_response = api_instance.create_organization_api_token(organization_id, body)
        print("The response of ApiTokenApi->create_organization_api_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiTokenApi->create_organization_api_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **body** | [**CreateOrganizationApiTokenRequest**](CreateOrganizationApiTokenRequest.md)| request body for creating an organization API token | 

### Return type

[**ApiToken**](ApiToken.md)

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

# **create_workspace_api_token**
> ApiToken create_workspace_api_token(organization_id, workspace_id, body)

Create Workspace API token

Create Workspace API token

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.api_token import ApiToken
from astronomercoreapi.models.create_workspace_api_token_request import CreateWorkspaceApiTokenRequest
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
    api_instance = astronomercoreapi.ApiTokenApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    body = astronomercoreapi.CreateWorkspaceApiTokenRequest() # CreateWorkspaceApiTokenRequest | request body for creating a workspace API token

    try:
        # Create Workspace API token
        api_response = api_instance.create_workspace_api_token(organization_id, workspace_id, body)
        print("The response of ApiTokenApi->create_workspace_api_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiTokenApi->create_workspace_api_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **body** | [**CreateWorkspaceApiTokenRequest**](CreateWorkspaceApiTokenRequest.md)| request body for creating a workspace API token | 

### Return type

[**ApiToken**](ApiToken.md)

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

# **delete_organization_api_token**
> delete_organization_api_token(organization_id, api_token_id)

Delete organization API token

Delete organization API token

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
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
    api_instance = astronomercoreapi.ApiTokenApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    api_token_id = 'api_token_id_example' # str | API token ID

    try:
        # Delete organization API token
        api_instance.delete_organization_api_token(organization_id, api_token_id)
    except Exception as e:
        print("Exception when calling ApiTokenApi->delete_organization_api_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **api_token_id** | **str**| API token ID | 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace_api_token**
> delete_workspace_api_token(organization_id, workspace_id, api_token_id)

Delete Workspace API token

Delete Workspace API token

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
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
    api_instance = astronomercoreapi.ApiTokenApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    api_token_id = 'api_token_id_example' # str | ID of the API token

    try:
        # Delete Workspace API token
        api_instance.delete_workspace_api_token(organization_id, workspace_id, api_token_id)
    except Exception as e:
        print("Exception when calling ApiTokenApi->delete_workspace_api_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **api_token_id** | **str**| ID of the API token | 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_api_token**
> ApiToken get_organization_api_token(organization_id, api_token_id)

Get Organization API token

Get Organization API token

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.api_token import ApiToken
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
    api_instance = astronomercoreapi.ApiTokenApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    api_token_id = 'api_token_id_example' # str | API token ID

    try:
        # Get Organization API token
        api_response = api_instance.get_organization_api_token(organization_id, api_token_id)
        print("The response of ApiTokenApi->get_organization_api_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiTokenApi->get_organization_api_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **api_token_id** | **str**| API token ID | 

### Return type

[**ApiToken**](ApiToken.md)

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

# **get_workspace_api_token**
> ApiToken get_workspace_api_token(organization_id, workspace_id, api_token_id)

Get Workspace API token

Get Workspace API token

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.api_token import ApiToken
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
    api_instance = astronomercoreapi.ApiTokenApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    api_token_id = 'api_token_id_example' # str | API token ID

    try:
        # Get Workspace API token
        api_response = api_instance.get_workspace_api_token(organization_id, workspace_id, api_token_id)
        print("The response of ApiTokenApi->get_workspace_api_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiTokenApi->get_workspace_api_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **api_token_id** | **str**| API token ID | 

### Return type

[**ApiToken**](ApiToken.md)

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

# **list_organization_api_tokens**
> ListApiTokensPaginated list_organization_api_tokens(organization_id, offset=offset, limit=limit, sorts=sorts)

List Organization API tokens

List Organization API tokens

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.list_api_tokens_paginated import ListApiTokensPaginated
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
    api_instance = astronomercoreapi.ApiTokenApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    offset = 0 # int | Offset for pagination (optional) (default to 0)
    limit = 20 # int | Limit for pagination (optional) (default to 20)
    sorts = ['sorts_example'] # List[str] | Sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc' (optional)

    try:
        # List Organization API tokens
        api_response = api_instance.list_organization_api_tokens(organization_id, offset=offset, limit=limit, sorts=sorts)
        print("The response of ApiTokenApi->list_organization_api_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiTokenApi->list_organization_api_tokens: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **offset** | **int**| Offset for pagination | [optional] [default to 0]
 **limit** | **int**| Limit for pagination | [optional] [default to 20]
 **sorts** | [**List[str]**](str.md)| Sorting criteria, each criterion should conform to format &#39;fieldName:asc&#39; or &#39;fieldName:desc&#39; | [optional] 

### Return type

[**ListApiTokensPaginated**](ListApiTokensPaginated.md)

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

# **list_workspace_api_tokens**
> ListApiTokensPaginated list_workspace_api_tokens(organization_id, workspace_id, offset=offset, limit=limit, sorts=sorts)

List Workspace API tokens

List Workspace API tokens

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.list_api_tokens_paginated import ListApiTokensPaginated
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
    api_instance = astronomercoreapi.ApiTokenApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    offset = 0 # int | Offset for pagination (optional) (default to 0)
    limit = 20 # int | Limit for pagination (optional) (default to 20)
    sorts = ['sorts_example'] # List[str] | Sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc' (optional)

    try:
        # List Workspace API tokens
        api_response = api_instance.list_workspace_api_tokens(organization_id, workspace_id, offset=offset, limit=limit, sorts=sorts)
        print("The response of ApiTokenApi->list_workspace_api_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiTokenApi->list_workspace_api_tokens: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **offset** | **int**| Offset for pagination | [optional] [default to 0]
 **limit** | **int**| Limit for pagination | [optional] [default to 20]
 **sorts** | [**List[str]**](str.md)| Sorting criteria, each criterion should conform to format &#39;fieldName:asc&#39; or &#39;fieldName:desc&#39; | [optional] 

### Return type

[**ListApiTokensPaginated**](ListApiTokensPaginated.md)

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

# **rotate_organization_api_token**
> ApiToken rotate_organization_api_token(organization_id, api_token_id)

Rotate organization API token

Rotate organization API token

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.api_token import ApiToken
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
    api_instance = astronomercoreapi.ApiTokenApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    api_token_id = 'api_token_id_example' # str | API token ID

    try:
        # Rotate organization API token
        api_response = api_instance.rotate_organization_api_token(organization_id, api_token_id)
        print("The response of ApiTokenApi->rotate_organization_api_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiTokenApi->rotate_organization_api_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **api_token_id** | **str**| API token ID | 

### Return type

[**ApiToken**](ApiToken.md)

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

# **rotate_workspace_api_token**
> ApiToken rotate_workspace_api_token(organization_id, workspace_id, api_token_id)

Rotate Workspace API token

Rotate Workspace API token

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.api_token import ApiToken
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
    api_instance = astronomercoreapi.ApiTokenApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    api_token_id = 'api_token_id_example' # str | API token ID

    try:
        # Rotate Workspace API token
        api_response = api_instance.rotate_workspace_api_token(organization_id, workspace_id, api_token_id)
        print("The response of ApiTokenApi->rotate_workspace_api_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiTokenApi->rotate_workspace_api_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **api_token_id** | **str**| API token ID | 

### Return type

[**ApiToken**](ApiToken.md)

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

# **update_organization_api_token**
> ApiToken update_organization_api_token(organization_id, api_token_id, body)

Update Organization API token

Update Organization API token

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.api_token import ApiToken
from astronomercoreapi.models.update_organization_api_token_request import UpdateOrganizationApiTokenRequest
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
    api_instance = astronomercoreapi.ApiTokenApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    api_token_id = 'api_token_id_example' # str | API token ID
    body = astronomercoreapi.UpdateOrganizationApiTokenRequest() # UpdateOrganizationApiTokenRequest | request body for updating an organization API token

    try:
        # Update Organization API token
        api_response = api_instance.update_organization_api_token(organization_id, api_token_id, body)
        print("The response of ApiTokenApi->update_organization_api_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiTokenApi->update_organization_api_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **api_token_id** | **str**| API token ID | 
 **body** | [**UpdateOrganizationApiTokenRequest**](UpdateOrganizationApiTokenRequest.md)| request body for updating an organization API token | 

### Return type

[**ApiToken**](ApiToken.md)

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

# **update_workspace_api_token**
> ApiToken update_workspace_api_token(organization_id, workspace_id, api_token_id, body)

Update Workspace API token

Update Workspace API token

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.api_token import ApiToken
from astronomercoreapi.models.update_workspace_api_token_request import UpdateWorkspaceApiTokenRequest
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
    api_instance = astronomercoreapi.ApiTokenApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    api_token_id = 'api_token_id_example' # str | API token ID
    body = astronomercoreapi.UpdateWorkspaceApiTokenRequest() # UpdateWorkspaceApiTokenRequest | request body for updating a workspace API token

    try:
        # Update Workspace API token
        api_response = api_instance.update_workspace_api_token(organization_id, workspace_id, api_token_id, body)
        print("The response of ApiTokenApi->update_workspace_api_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiTokenApi->update_workspace_api_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **api_token_id** | **str**| API token ID | 
 **body** | [**UpdateWorkspaceApiTokenRequest**](UpdateWorkspaceApiTokenRequest.md)| request body for updating a workspace API token | 

### Return type

[**ApiToken**](ApiToken.md)

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

