# astronomerregistry.ProviderApi

All URIs are relative to *https://api.astronomer.io/registryV2/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_provider**](ProviderApi.md#create_provider) | **POST** /organizations/{orgShortNameId}/providers | Create provider for registry
[**delete_provider**](ProviderApi.md#delete_provider) | **DELETE** /organizations/{orgShortNameId}/providers/{providerName}/versions/{version} | Delete a provider
[**get_provider**](ProviderApi.md#get_provider) | **GET** /organizations/{orgShortNameId}/providers/{providerName}/versions/{version} | Get provider
[**list_providers**](ProviderApi.md#list_providers) | **GET** /organizations/{orgShortNameId}/providers | List providers
[**update_provider**](ProviderApi.md#update_provider) | **PUT** /organizations/{orgShortNameId}/providers/{providerName}/versions/{version} | Update provider for registry


# **create_provider**
> Provider create_provider(org_short_name_id, body)

Create provider for registry

Create provider for registry

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomerregistry
from astronomerregistry.models.create_provider_request import CreateProviderRequest
from astronomerregistry.models.provider import Provider
from astronomerregistry.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astronomer.io/registryV2/v1alpha1
# See configuration.py for a list of all supported configuration parameters.
configuration = astronomerregistry.Configuration(
    host = "https://api.astronomer.io/registryV2/v1alpha1"
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
with astronomerregistry.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astronomerregistry.ProviderApi(api_client)
    org_short_name_id = 'org_short_name_id_example' # str | organization FQN
    body = astronomerregistry.CreateProviderRequest() # CreateProviderRequest | request body for creating a registry provider

    try:
        # Create provider for registry
        api_response = api_instance.create_provider(org_short_name_id, body)
        print("The response of ProviderApi->create_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderApi->create_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_short_name_id** | **str**| organization FQN | 
 **body** | [**CreateProviderRequest**](CreateProviderRequest.md)| request body for creating a registry provider | 

### Return type

[**Provider**](Provider.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_provider**
> Provider delete_provider(org_short_name_id, provider_name, version)

Delete a provider

Delete a single provider by name and version

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomerregistry
from astronomerregistry.models.provider import Provider
from astronomerregistry.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astronomer.io/registryV2/v1alpha1
# See configuration.py for a list of all supported configuration parameters.
configuration = astronomerregistry.Configuration(
    host = "https://api.astronomer.io/registryV2/v1alpha1"
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
with astronomerregistry.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astronomerregistry.ProviderApi(api_client)
    org_short_name_id = 'org_short_name_id_example' # str | organization FQN
    provider_name = 'provider_name_example' # str | The name of the provider
    version = 'version_example' # str | The version of the provider

    try:
        # Delete a provider
        api_response = api_instance.delete_provider(org_short_name_id, provider_name, version)
        print("The response of ProviderApi->delete_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderApi->delete_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_short_name_id** | **str**| organization FQN | 
 **provider_name** | **str**| The name of the provider | 
 **version** | **str**| The version of the provider | 

### Return type

[**Provider**](Provider.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provider**
> Provider get_provider(org_short_name_id, provider_name, version)

Get provider

Get a single provider by providerName and version

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomerregistry
from astronomerregistry.models.provider import Provider
from astronomerregistry.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astronomer.io/registryV2/v1alpha1
# See configuration.py for a list of all supported configuration parameters.
configuration = astronomerregistry.Configuration(
    host = "https://api.astronomer.io/registryV2/v1alpha1"
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
with astronomerregistry.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astronomerregistry.ProviderApi(api_client)
    org_short_name_id = 'org_short_name_id_example' # str | organization FQN
    provider_name = 'provider_name_example' # str | The name or display name of the provider
    version = 'version_example' # str | The version of the provider, or keyword 'latest' for latest version

    try:
        # Get provider
        api_response = api_instance.get_provider(org_short_name_id, provider_name, version)
        print("The response of ProviderApi->get_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderApi->get_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_short_name_id** | **str**| organization FQN | 
 **provider_name** | **str**| The name or display name of the provider | 
 **version** | **str**| The version of the provider, or keyword &#39;latest&#39; for latest version | 

### Return type

[**Provider**](Provider.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_providers**
> ProvidersPaginated list_providers(org_short_name_id, is_certified=is_certified, is_featured=is_featured, is_global=is_global, is_private=is_private, is_cloud_ide_compatible=is_cloud_ide_compatible, type_name=type_name, tier_id=tier_id, category_id=category_id, badge_id=badge_id, provider_id=provider_id, tier_name=tier_name, category_name=category_name, badge_name=badge_name, query=query, offset=offset, limit=limit, sorts=sorts)

List providers

List providers

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomerregistry
from astronomerregistry.models.providers_paginated import ProvidersPaginated
from astronomerregistry.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astronomer.io/registryV2/v1alpha1
# See configuration.py for a list of all supported configuration parameters.
configuration = astronomerregistry.Configuration(
    host = "https://api.astronomer.io/registryV2/v1alpha1"
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
with astronomerregistry.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astronomerregistry.ProviderApi(api_client)
    org_short_name_id = 'org_short_name_id_example' # str | organization FQN
    is_certified = True # bool | return only certified providers (optional)
    is_featured = True # bool | return only featured providers (optional)
    is_global = True # bool | return only global providers (optional)
    is_private = True # bool | return only private providers (optional)
    is_cloud_ide_compatible = True # bool | return only cloud ide compatible providers (optional)
    type_name = ['type_name_example'] # List[str] | Has at least one type in input filter list (optional)
    tier_id = ['tier_id_example'] # List[str] | Has at least one tier in input filter list (optional)
    category_id = ['category_id_example'] # List[str] | Has at least one category in input filter list (optional)
    badge_id = ['badge_id_example'] # List[str] | Has at least one badge in input filter list (optional)
    provider_id = ['provider_id_example'] # List[str] | Has one id in input filter list (optional)
    tier_name = ['tier_name_example'] # List[str] | Has at least one tier name in input filter list (optional)
    category_name = ['category_name_example'] # List[str] | Has at least one category name in input filter list (optional)
    badge_name = ['badge_name_example'] # List[str] | Has at least one badge name in input filter list (optional)
    query = 'query_example' # str | Search query for provider (optional)
    offset = 0 # int | offset for pagination (optional) (default to 0)
    limit = 20 # int | limit for pagination (optional) (default to 20)
    sorts = ['sorts_example'] # List[str] | sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc' (optional)

    try:
        # List providers
        api_response = api_instance.list_providers(org_short_name_id, is_certified=is_certified, is_featured=is_featured, is_global=is_global, is_private=is_private, is_cloud_ide_compatible=is_cloud_ide_compatible, type_name=type_name, tier_id=tier_id, category_id=category_id, badge_id=badge_id, provider_id=provider_id, tier_name=tier_name, category_name=category_name, badge_name=badge_name, query=query, offset=offset, limit=limit, sorts=sorts)
        print("The response of ProviderApi->list_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderApi->list_providers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_short_name_id** | **str**| organization FQN | 
 **is_certified** | **bool**| return only certified providers | [optional] 
 **is_featured** | **bool**| return only featured providers | [optional] 
 **is_global** | **bool**| return only global providers | [optional] 
 **is_private** | **bool**| return only private providers | [optional] 
 **is_cloud_ide_compatible** | **bool**| return only cloud ide compatible providers | [optional] 
 **type_name** | [**List[str]**](str.md)| Has at least one type in input filter list | [optional] 
 **tier_id** | [**List[str]**](str.md)| Has at least one tier in input filter list | [optional] 
 **category_id** | [**List[str]**](str.md)| Has at least one category in input filter list | [optional] 
 **badge_id** | [**List[str]**](str.md)| Has at least one badge in input filter list | [optional] 
 **provider_id** | [**List[str]**](str.md)| Has one id in input filter list | [optional] 
 **tier_name** | [**List[str]**](str.md)| Has at least one tier name in input filter list | [optional] 
 **category_name** | [**List[str]**](str.md)| Has at least one category name in input filter list | [optional] 
 **badge_name** | [**List[str]**](str.md)| Has at least one badge name in input filter list | [optional] 
 **query** | **str**| Search query for provider | [optional] 
 **offset** | **int**| offset for pagination | [optional] [default to 0]
 **limit** | **int**| limit for pagination | [optional] [default to 20]
 **sorts** | [**List[str]**](str.md)| sorting criteria, each criterion should conform to format &#39;fieldName:asc&#39; or &#39;fieldName:desc&#39; | [optional] 

### Return type

[**ProvidersPaginated**](ProvidersPaginated.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_provider**
> Provider update_provider(org_short_name_id, provider_name, version, body)

Update provider for registry

Update provider for registry

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomerregistry
from astronomerregistry.models.provider import Provider
from astronomerregistry.models.update_provider_request import UpdateProviderRequest
from astronomerregistry.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astronomer.io/registryV2/v1alpha1
# See configuration.py for a list of all supported configuration parameters.
configuration = astronomerregistry.Configuration(
    host = "https://api.astronomer.io/registryV2/v1alpha1"
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
with astronomerregistry.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astronomerregistry.ProviderApi(api_client)
    org_short_name_id = 'org_short_name_id_example' # str | organization FQN
    provider_name = 'provider_name_example' # str | The name of the provider
    version = 'version_example' # str | The version of the provider
    body = astronomerregistry.UpdateProviderRequest() # UpdateProviderRequest | request body for updating a registry provider

    try:
        # Update provider for registry
        api_response = api_instance.update_provider(org_short_name_id, provider_name, version, body)
        print("The response of ProviderApi->update_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderApi->update_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_short_name_id** | **str**| organization FQN | 
 **provider_name** | **str**| The name of the provider | 
 **version** | **str**| The version of the provider | 
 **body** | [**UpdateProviderRequest**](UpdateProviderRequest.md)| request body for updating a registry provider | 

### Return type

[**Provider**](Provider.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

