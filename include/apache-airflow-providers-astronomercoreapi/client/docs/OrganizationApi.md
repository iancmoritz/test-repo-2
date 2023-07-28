# astronomercoreapi.OrganizationApi

All URIs are relative to *https://api.astronomer.io/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_managed_domain**](OrganizationApi.md#create_managed_domain) | **POST** /organizations/{organizationId}/domains | Create managed domain
[**create_organization**](OrganizationApi.md#create_organization) | **POST** /organizations | Create organization
[**create_sso_connection**](OrganizationApi.md#create_sso_connection) | **POST** /organizations/{organizationId}/sso-connections | Create SSO connection
[**delete_managed_domain**](OrganizationApi.md#delete_managed_domain) | **DELETE** /organizations/{organizationId}/domains/{domainId} | Delete managed domain
[**delete_sso_bypass_key**](OrganizationApi.md#delete_sso_bypass_key) | **DELETE** /organizations/{organizationId}/sso-bypass-key | Delete SSO bypass key
[**delete_sso_connection**](OrganizationApi.md#delete_sso_connection) | **DELETE** /organizations/{organizationId}/sso-connections/{connectionId} | Delete SSO connection
[**get_managed_domain**](OrganizationApi.md#get_managed_domain) | **GET** /organizations/{organizationId}/domains/{domainId} | Get managed domain
[**get_organization**](OrganizationApi.md#get_organization) | **GET** /organizations/{organizationId} | Get organization
[**get_organization_audit_logs**](OrganizationApi.md#get_organization_audit_logs) | **GET** /organizations/{organizationId}/audit-logs | Get organization audit logs
[**get_sso_bypass_key**](OrganizationApi.md#get_sso_bypass_key) | **GET** /organizations/{organizationId}/sso-bypass-key | Get SSO bypass key
[**get_sso_connection**](OrganizationApi.md#get_sso_connection) | **GET** /organizations/{organizationId}/sso-connections/{connectionId} | Get SSO connection
[**list_managed_domains**](OrganizationApi.md#list_managed_domains) | **GET** /organizations/{organizationId}/domains | List managed domains
[**list_organization_auth_ids**](OrganizationApi.md#list_organization_auth_ids) | **GET** /organizationAuthIds | List organization auth IDs
[**list_organizations**](OrganizationApi.md#list_organizations) | **GET** /organizations | List organizations
[**list_sso_connections**](OrganizationApi.md#list_sso_connections) | **GET** /organizations/{organizationId}/sso-connections | List SSO connections
[**update_managed_domain**](OrganizationApi.md#update_managed_domain) | **POST** /organizations/{organizationId}/domains/{domainId} | Update managed domain
[**update_organization**](OrganizationApi.md#update_organization) | **POST** /organizations/{organizationId} | Update organization
[**update_sso_connection**](OrganizationApi.md#update_sso_connection) | **POST** /organizations/{organizationId}/sso-connections/{connectionId} | Update SSO connection
[**upsert_sso_bypass_key**](OrganizationApi.md#upsert_sso_bypass_key) | **POST** /organizations/{organizationId}/sso-bypass-key | Upsert SSO bypass key
[**validate_sso_login**](OrganizationApi.md#validate_sso_login) | **POST** /auth/post-login-callback | Validate SSO Login Callback
[**verify_managed_domain**](OrganizationApi.md#verify_managed_domain) | **POST** /organizations/{organizationId}/domains/{domainId}/verify | Verify managed domain


# **create_managed_domain**
> ManagedDomain create_managed_domain(organization_id, body)

Create managed domain

Create managed domain

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.create_managed_domain_request import CreateManagedDomainRequest
from astronomercoreapi.models.managed_domain import ManagedDomain
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
    api_instance = astronomercoreapi.OrganizationApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    body = astronomercoreapi.CreateManagedDomainRequest() # CreateManagedDomainRequest | request body for creating a managed domain

    try:
        # Create managed domain
        api_response = api_instance.create_managed_domain(organization_id, body)
        print("The response of OrganizationApi->create_managed_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->create_managed_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **body** | [**CreateManagedDomainRequest**](CreateManagedDomainRequest.md)| request body for creating a managed domain | 

### Return type

[**ManagedDomain**](ManagedDomain.md)

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

# **create_organization**
> Organization create_organization(body)

Create organization

Create organization

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.create_organization_request import CreateOrganizationRequest
from astronomercoreapi.models.organization import Organization
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
    api_instance = astronomercoreapi.OrganizationApi(api_client)
    body = astronomercoreapi.CreateOrganizationRequest() # CreateOrganizationRequest | request body for creating an organization

    try:
        # Create organization
        api_response = api_instance.create_organization(body)
        print("The response of OrganizationApi->create_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->create_organization: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrganizationRequest**](CreateOrganizationRequest.md)| request body for creating an organization | 

### Return type

[**Organization**](Organization.md)

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

# **create_sso_connection**
> SsoConnection create_sso_connection(organization_id, body)

Create SSO connection

Create SSO connection

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.create_sso_connection_request import CreateSsoConnectionRequest
from astronomercoreapi.models.sso_connection import SsoConnection
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
    api_instance = astronomercoreapi.OrganizationApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    body = astronomercoreapi.CreateSsoConnectionRequest() # CreateSsoConnectionRequest | request body for creating a sso connection

    try:
        # Create SSO connection
        api_response = api_instance.create_sso_connection(organization_id, body)
        print("The response of OrganizationApi->create_sso_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->create_sso_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **body** | [**CreateSsoConnectionRequest**](CreateSsoConnectionRequest.md)| request body for creating a sso connection | 

### Return type

[**SsoConnection**](SsoConnection.md)

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

# **delete_managed_domain**
> delete_managed_domain(organization_id, domain_id)

Delete managed domain

Delete managed domain

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
    api_instance = astronomercoreapi.OrganizationApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    domain_id = 'domain_id_example' # str | managed domain ID

    try:
        # Delete managed domain
        api_instance.delete_managed_domain(organization_id, domain_id)
    except Exception as e:
        print("Exception when calling OrganizationApi->delete_managed_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **domain_id** | **str**| managed domain ID | 

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

# **delete_sso_bypass_key**
> delete_sso_bypass_key(organization_id)

Delete SSO bypass key

Delete SSO bypass key

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
    api_instance = astronomercoreapi.OrganizationApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID

    try:
        # Delete SSO bypass key
        api_instance.delete_sso_bypass_key(organization_id)
    except Exception as e:
        print("Exception when calling OrganizationApi->delete_sso_bypass_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 

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

# **delete_sso_connection**
> delete_sso_connection(organization_id, connection_id)

Delete SSO connection

Delete SSO connection

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
    api_instance = astronomercoreapi.OrganizationApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    connection_id = 'connection_id_example' # str | connection ID

    try:
        # Delete SSO connection
        api_instance.delete_sso_connection(organization_id, connection_id)
    except Exception as e:
        print("Exception when calling OrganizationApi->delete_sso_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **connection_id** | **str**| connection ID | 

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

# **get_managed_domain**
> ManagedDomain get_managed_domain(organization_id, domain_id)

Get managed domain

Get managed domain

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.managed_domain import ManagedDomain
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
    api_instance = astronomercoreapi.OrganizationApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    domain_id = 'domain_id_example' # str | managed domain ID

    try:
        # Get managed domain
        api_response = api_instance.get_managed_domain(organization_id, domain_id)
        print("The response of OrganizationApi->get_managed_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->get_managed_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **domain_id** | **str**| managed domain ID | 

### Return type

[**ManagedDomain**](ManagedDomain.md)

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

# **get_organization**
> Organization get_organization(organization_id, is_look_up_only=is_look_up_only)

Get organization

Get organization

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.organization import Organization
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
    api_instance = astronomercoreapi.OrganizationApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    is_look_up_only = True # bool | only look up organization metadata if true (optional)

    try:
        # Get organization
        api_response = api_instance.get_organization(organization_id, is_look_up_only=is_look_up_only)
        print("The response of OrganizationApi->get_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->get_organization: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **is_look_up_only** | **bool**| only look up organization metadata if true | [optional] 

### Return type

[**Organization**](Organization.md)

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

# **get_organization_audit_logs**
> List[int] get_organization_audit_logs(organization_id, earliest=earliest)

Get organization audit logs

Get organization audit logs.

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
    api_instance = astronomercoreapi.OrganizationApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    earliest = '1' # str | starting point in days for audit logs (optional) (default to '1')

    try:
        # Get organization audit logs
        api_response = api_instance.get_organization_audit_logs(organization_id, earliest=earliest)
        print("The response of OrganizationApi->get_organization_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->get_organization_audit_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **earliest** | **str**| starting point in days for audit logs | [optional] [default to &#39;1&#39;]

### Return type

**List[int]**

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sso_bypass_key**
> SsoBypassKey get_sso_bypass_key(organization_id)

Get SSO bypass key

Get SSO bypass key

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
    api_instance = astronomercoreapi.OrganizationApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID

    try:
        # Get SSO bypass key
        api_response = api_instance.get_sso_bypass_key(organization_id)
        print("The response of OrganizationApi->get_sso_bypass_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->get_sso_bypass_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 

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

# **get_sso_connection**
> SsoConnection get_sso_connection(organization_id, connection_id)

Get SSO connection

Get SSO connection

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.sso_connection import SsoConnection
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
    api_instance = astronomercoreapi.OrganizationApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    connection_id = 'connection_id_example' # str | connection ID

    try:
        # Get SSO connection
        api_response = api_instance.get_sso_connection(organization_id, connection_id)
        print("The response of OrganizationApi->get_sso_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->get_sso_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **connection_id** | **str**| connection ID | 

### Return type

[**SsoConnection**](SsoConnection.md)

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

# **list_managed_domains**
> List[ManagedDomain] list_managed_domains(organization_id)

List managed domains

List managed domains

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.managed_domain import ManagedDomain
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
    api_instance = astronomercoreapi.OrganizationApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID

    try:
        # List managed domains
        api_response = api_instance.list_managed_domains(organization_id)
        print("The response of OrganizationApi->list_managed_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->list_managed_domains: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 

### Return type

[**List[ManagedDomain]**](ManagedDomain.md)

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

# **list_organization_auth_ids**
> List[str] list_organization_auth_ids(email)

List organization auth IDs

List organization auth IDs

### Example

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


# Enter a context with an instance of the API client
with astronomercoreapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astronomercoreapi.OrganizationApi(api_client)
    email = 'email_example' # str | User email to retrieve organization auth IDs for

    try:
        # List organization auth IDs
        api_response = api_instance.list_organization_auth_ids(email)
        print("The response of OrganizationApi->list_organization_auth_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->list_organization_auth_ids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| User email to retrieve organization auth IDs for | 

### Return type

**List[str]**

### Authorization

No authorization required

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organizations**
> List[Organization] list_organizations(search=search, trial_status=trial_status, support_plan=support_plan, product=product, sorts=sorts)

List organizations

List organizations

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.organization import Organization
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
    api_instance = astronomercoreapi.OrganizationApi(api_client)
    search = 'search_example' # str | string to search for when listing users (optional)
    trial_status = 'trial_status_example' # str | filter by trial status, null for all orgs (optional)
    support_plan = 'support_plan_example' # str | filter by support plan, should be one of INTERNAL, POV, TRIAL, BASIC, STANDARD, PREMIUM, BUSINESS_CRITICAL, or null for all orgs (optional)
    product = 'product_example' # str | filter by product, null for all orgs (optional)
    sorts = ['sorts_example'] # List[str] | sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc' (optional)

    try:
        # List organizations
        api_response = api_instance.list_organizations(search=search, trial_status=trial_status, support_plan=support_plan, product=product, sorts=sorts)
        print("The response of OrganizationApi->list_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->list_organizations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| string to search for when listing users | [optional] 
 **trial_status** | **str**| filter by trial status, null for all orgs | [optional] 
 **support_plan** | **str**| filter by support plan, should be one of INTERNAL, POV, TRIAL, BASIC, STANDARD, PREMIUM, BUSINESS_CRITICAL, or null for all orgs | [optional] 
 **product** | **str**| filter by product, null for all orgs | [optional] 
 **sorts** | [**List[str]**](str.md)| sorting criteria, each criterion should conform to format &#39;fieldName:asc&#39; or &#39;fieldName:desc&#39; | [optional] 

### Return type

[**List[Organization]**](Organization.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sso_connections**
> List[SsoConnection] list_sso_connections(organization_id)

List SSO connections

List SSO connections

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.sso_connection import SsoConnection
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
    api_instance = astronomercoreapi.OrganizationApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID

    try:
        # List SSO connections
        api_response = api_instance.list_sso_connections(organization_id)
        print("The response of OrganizationApi->list_sso_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->list_sso_connections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 

### Return type

[**List[SsoConnection]**](SsoConnection.md)

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

# **update_managed_domain**
> ManagedDomain update_managed_domain(organization_id, domain_id, body)

Update managed domain

Update managed domain

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.managed_domain import ManagedDomain
from astronomercoreapi.models.update_managed_domain_request import UpdateManagedDomainRequest
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
    api_instance = astronomercoreapi.OrganizationApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    domain_id = 'domain_id_example' # str | managed domain ID
    body = astronomercoreapi.UpdateManagedDomainRequest() # UpdateManagedDomainRequest | request body for updating a managed domain

    try:
        # Update managed domain
        api_response = api_instance.update_managed_domain(organization_id, domain_id, body)
        print("The response of OrganizationApi->update_managed_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->update_managed_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **domain_id** | **str**| managed domain ID | 
 **body** | [**UpdateManagedDomainRequest**](UpdateManagedDomainRequest.md)| request body for updating a managed domain | 

### Return type

[**ManagedDomain**](ManagedDomain.md)

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

# **update_organization**
> Organization update_organization(organization_id, body)

Update organization

Update organization

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.organization import Organization
from astronomercoreapi.models.update_organization_request import UpdateOrganizationRequest
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
    api_instance = astronomercoreapi.OrganizationApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    body = astronomercoreapi.UpdateOrganizationRequest() # UpdateOrganizationRequest | request body for updating an organization

    try:
        # Update organization
        api_response = api_instance.update_organization(organization_id, body)
        print("The response of OrganizationApi->update_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->update_organization: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **body** | [**UpdateOrganizationRequest**](UpdateOrganizationRequest.md)| request body for updating an organization | 

### Return type

[**Organization**](Organization.md)

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

# **update_sso_connection**
> SsoConnection update_sso_connection(organization_id, connection_id, body)

Update SSO connection

Update SSO connection

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.sso_connection import SsoConnection
from astronomercoreapi.models.update_sso_connection_request import UpdateSsoConnectionRequest
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
    api_instance = astronomercoreapi.OrganizationApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    connection_id = 'connection_id_example' # str | connection ID
    body = astronomercoreapi.UpdateSsoConnectionRequest() # UpdateSsoConnectionRequest | request body for updating a sso connection

    try:
        # Update SSO connection
        api_response = api_instance.update_sso_connection(organization_id, connection_id, body)
        print("The response of OrganizationApi->update_sso_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->update_sso_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **connection_id** | **str**| connection ID | 
 **body** | [**UpdateSsoConnectionRequest**](UpdateSsoConnectionRequest.md)| request body for updating a sso connection | 

### Return type

[**SsoConnection**](SsoConnection.md)

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

# **upsert_sso_bypass_key**
> SsoBypassKey upsert_sso_bypass_key(organization_id)

Upsert SSO bypass key

Upsert SSO bypass key

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
    api_instance = astronomercoreapi.OrganizationApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID

    try:
        # Upsert SSO bypass key
        api_response = api_instance.upsert_sso_bypass_key(organization_id)
        print("The response of OrganizationApi->upsert_sso_bypass_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->upsert_sso_bypass_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 

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

# **validate_sso_login**
> SsoLoginCallback validate_sso_login(body)

Validate SSO Login Callback

Validate SSO Login Callback

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.sso_login_callback import SsoLoginCallback
from astronomercoreapi.models.validate_sso_login_request import ValidateSsoLoginRequest
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
    api_instance = astronomercoreapi.OrganizationApi(api_client)
    body = astronomercoreapi.ValidateSsoLoginRequest() # ValidateSsoLoginRequest | event request body for sso login validation

    try:
        # Validate SSO Login Callback
        api_response = api_instance.validate_sso_login(body)
        print("The response of OrganizationApi->validate_sso_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->validate_sso_login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ValidateSsoLoginRequest**](ValidateSsoLoginRequest.md)| event request body for sso login validation | 

### Return type

[**SsoLoginCallback**](SsoLoginCallback.md)

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

# **verify_managed_domain**
> ManagedDomain verify_managed_domain(organization_id, domain_id)

Verify managed domain

Verify managed domain

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.managed_domain import ManagedDomain
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
    api_instance = astronomercoreapi.OrganizationApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    domain_id = 'domain_id_example' # str | managed domain ID

    try:
        # Verify managed domain
        api_response = api_instance.verify_managed_domain(organization_id, domain_id)
        print("The response of OrganizationApi->verify_managed_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->verify_managed_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **domain_id** | **str**| managed domain ID | 

### Return type

[**ManagedDomain**](ManagedDomain.md)

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

