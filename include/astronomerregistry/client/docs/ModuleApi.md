# astronomerregistry.ModuleApi

All URIs are relative to *https://api.astronomer.io/registryV2/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_module**](ModuleApi.md#create_module) | **POST** /organizations/{orgShortNameId}/providers/{providerName}/versions/{version}/modules | Create module for registry
[**delete_module**](ModuleApi.md#delete_module) | **DELETE** /organizations/{orgShortNameId}/providers/{providerName}/versions/{version}/modules/{moduleName} | Delete a module
[**get_module**](ModuleApi.md#get_module) | **GET** /organizations/{orgShortNameId}/providers/{providerName}/versions/{version}/modules/{moduleName} | Get module
[**list_modules**](ModuleApi.md#list_modules) | **GET** /organizations/{orgShortNameId}/modules | List modules
[**list_modules_internal**](ModuleApi.md#list_modules_internal) | **GET** /organizations/{orgShortNameId}/modules/{moduleName} | List any modules matching a module name
[**update_module**](ModuleApi.md#update_module) | **PUT** /organizations/{orgShortNameId}/providers/{providerName}/versions/{version}/modules/{moduleName} | Update module for registry


# **create_module**
> Module create_module(org_short_name_id, provider_name, version, body)

Create module for registry

Create module for registry

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomerregistry
from astronomerregistry.models.create_module_request import CreateModuleRequest
from astronomerregistry.models.module import Module
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
    api_instance = astronomerregistry.ModuleApi(api_client)
    org_short_name_id = 'org_short_name_id_example' # str | organization FQN
    provider_name = 'provider_name_example' # str | The name or display name of the provider
    version = 'version_example' # str | The version of the module, or keyword 'latest' for latest version
    body = astronomerregistry.CreateModuleRequest() # CreateModuleRequest | request body for creating a registry module

    try:
        # Create module for registry
        api_response = api_instance.create_module(org_short_name_id, provider_name, version, body)
        print("The response of ModuleApi->create_module:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleApi->create_module: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_short_name_id** | **str**| organization FQN | 
 **provider_name** | **str**| The name or display name of the provider | 
 **version** | **str**| The version of the module, or keyword &#39;latest&#39; for latest version | 
 **body** | [**CreateModuleRequest**](CreateModuleRequest.md)| request body for creating a registry module | 

### Return type

[**Module**](Module.md)

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

# **delete_module**
> Module delete_module(org_short_name_id, provider_name, version, module_name)

Delete a module

Delete a single module by name and version

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomerregistry
from astronomerregistry.models.module import Module
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
    api_instance = astronomerregistry.ModuleApi(api_client)
    org_short_name_id = 'org_short_name_id_example' # str | organization FQN
    provider_name = 'provider_name_example' # str | The name or display name of the provider
    version = 'version_example' # str | The version of the module, or keyword 'latest' for latest version
    module_name = 'module_name_example' # str | The name of the module

    try:
        # Delete a module
        api_response = api_instance.delete_module(org_short_name_id, provider_name, version, module_name)
        print("The response of ModuleApi->delete_module:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleApi->delete_module: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_short_name_id** | **str**| organization FQN | 
 **provider_name** | **str**| The name or display name of the provider | 
 **version** | **str**| The version of the module, or keyword &#39;latest&#39; for latest version | 
 **module_name** | **str**| The name of the module | 

### Return type

[**Module**](Module.md)

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

# **get_module**
> Module get_module(org_short_name_id, provider_name, version, module_name)

Get module

Get a single module by moduleName and version

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomerregistry
from astronomerregistry.models.module import Module
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
    api_instance = astronomerregistry.ModuleApi(api_client)
    org_short_name_id = 'org_short_name_id_example' # str | organization FQN
    provider_name = 'provider_name_example' # str | The name or display name of the provider
    version = 'version_example' # str | The version of the module, or keyword 'latest' for latest version
    module_name = 'module_name_example' # str | The name or display name of the module

    try:
        # Get module
        api_response = api_instance.get_module(org_short_name_id, provider_name, version, module_name)
        print("The response of ModuleApi->get_module:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleApi->get_module: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_short_name_id** | **str**| organization FQN | 
 **provider_name** | **str**| The name or display name of the provider | 
 **version** | **str**| The version of the module, or keyword &#39;latest&#39; for latest version | 
 **module_name** | **str**| The name or display name of the module | 

### Return type

[**Module**](Module.md)

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

# **list_modules**
> ModulesPaginated list_modules(org_short_name_id, is_certified=is_certified, is_featured=is_featured, is_global=is_global, is_private=is_private, is_cloud_ide_compatible=is_cloud_ide_compatible, type_name=type_name, tier_id=tier_id, category_id=category_id, badge_id=badge_id, dag_id=dag_id, module_id=module_id, provider_id=provider_id, tier_name=tier_name, category_name=category_name, badge_name=badge_name, provider_name=provider_name, query=query, offset=offset, limit=limit, sorts=sorts)

List modules

List modules

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomerregistry
from astronomerregistry.models.modules_paginated import ModulesPaginated
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
    api_instance = astronomerregistry.ModuleApi(api_client)
    org_short_name_id = 'org_short_name_id_example' # str | organization FQN
    is_certified = True # bool | return only certified modules (optional)
    is_featured = True # bool | return only featured modules (optional)
    is_global = True # bool | return only global modules (optional)
    is_private = True # bool | return only private modules (optional)
    is_cloud_ide_compatible = True # bool | return only cloud ide compatible modules (optional)
    type_name = ['type_name_example'] # List[str] | Has at least one type in input filter list (optional)
    tier_id = ['tier_id_example'] # List[str] | Has at least one tier in input filter list (optional)
    category_id = ['category_id_example'] # List[str] | Has at least one category in input filter list (optional)
    badge_id = ['badge_id_example'] # List[str] | Has at least one badge in input filter list (optional)
    dag_id = ['dag_id_example'] # List[str] | Has one id in input filter list (optional)
    module_id = ['module_id_example'] # List[str] | Has one module in input filter list (optional)
    provider_id = ['provider_id_example'] # List[str] | Has one provider in input filter list (optional)
    tier_name = ['tier_name_example'] # List[str] | Has at least one tier name in input filter list (optional)
    category_name = ['category_name_example'] # List[str] | Has at least one category name in input filter list (optional)
    badge_name = ['badge_name_example'] # List[str] | Has at least one badge name in input filter list (optional)
    provider_name = ['provider_name_example'] # List[str] | Has one provider name in input filter list (optional)
    query = 'query_example' # str | Search query for module (optional)
    offset = 0 # int | offset for pagination (optional) (default to 0)
    limit = 20 # int | limit for pagination (optional) (default to 20)
    sorts = ['sorts_example'] # List[str] | sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc' (optional)

    try:
        # List modules
        api_response = api_instance.list_modules(org_short_name_id, is_certified=is_certified, is_featured=is_featured, is_global=is_global, is_private=is_private, is_cloud_ide_compatible=is_cloud_ide_compatible, type_name=type_name, tier_id=tier_id, category_id=category_id, badge_id=badge_id, dag_id=dag_id, module_id=module_id, provider_id=provider_id, tier_name=tier_name, category_name=category_name, badge_name=badge_name, provider_name=provider_name, query=query, offset=offset, limit=limit, sorts=sorts)
        print("The response of ModuleApi->list_modules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleApi->list_modules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_short_name_id** | **str**| organization FQN | 
 **is_certified** | **bool**| return only certified modules | [optional] 
 **is_featured** | **bool**| return only featured modules | [optional] 
 **is_global** | **bool**| return only global modules | [optional] 
 **is_private** | **bool**| return only private modules | [optional] 
 **is_cloud_ide_compatible** | **bool**| return only cloud ide compatible modules | [optional] 
 **type_name** | [**List[str]**](str.md)| Has at least one type in input filter list | [optional] 
 **tier_id** | [**List[str]**](str.md)| Has at least one tier in input filter list | [optional] 
 **category_id** | [**List[str]**](str.md)| Has at least one category in input filter list | [optional] 
 **badge_id** | [**List[str]**](str.md)| Has at least one badge in input filter list | [optional] 
 **dag_id** | [**List[str]**](str.md)| Has one id in input filter list | [optional] 
 **module_id** | [**List[str]**](str.md)| Has one module in input filter list | [optional] 
 **provider_id** | [**List[str]**](str.md)| Has one provider in input filter list | [optional] 
 **tier_name** | [**List[str]**](str.md)| Has at least one tier name in input filter list | [optional] 
 **category_name** | [**List[str]**](str.md)| Has at least one category name in input filter list | [optional] 
 **badge_name** | [**List[str]**](str.md)| Has at least one badge name in input filter list | [optional] 
 **provider_name** | [**List[str]**](str.md)| Has one provider name in input filter list | [optional] 
 **query** | **str**| Search query for module | [optional] 
 **offset** | **int**| offset for pagination | [optional] [default to 0]
 **limit** | **int**| limit for pagination | [optional] [default to 20]
 **sorts** | [**List[str]**](str.md)| sorting criteria, each criterion should conform to format &#39;fieldName:asc&#39; or &#39;fieldName:desc&#39; | [optional] 

### Return type

[**ModulesPaginated**](ModulesPaginated.md)

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

# **list_modules_internal**
> ModulesPaginated list_modules_internal(org_short_name_id, module_name)

List any modules matching a module name

List any modules matching a module name

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomerregistry
from astronomerregistry.models.modules_paginated import ModulesPaginated
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
    api_instance = astronomerregistry.ModuleApi(api_client)
    org_short_name_id = 'org_short_name_id_example' # str | organization FQN
    module_name = 'module_name_example' # str | The name or display name of the module

    try:
        # List any modules matching a module name
        api_response = api_instance.list_modules_internal(org_short_name_id, module_name)
        print("The response of ModuleApi->list_modules_internal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleApi->list_modules_internal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_short_name_id** | **str**| organization FQN | 
 **module_name** | **str**| The name or display name of the module | 

### Return type

[**ModulesPaginated**](ModulesPaginated.md)

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

# **update_module**
> Module update_module(org_short_name_id, provider_name, version, module_name, body)

Update module for registry

Update module for registry

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomerregistry
from astronomerregistry.models.module import Module
from astronomerregistry.models.update_module_request import UpdateModuleRequest
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
    api_instance = astronomerregistry.ModuleApi(api_client)
    org_short_name_id = 'org_short_name_id_example' # str | organization FQN
    provider_name = 'provider_name_example' # str | The name of the provider
    version = 'version_example' # str | The version of the module
    module_name = 'module_name_example' # str | The name of the module
    body = astronomerregistry.UpdateModuleRequest() # UpdateModuleRequest | request body for updating a registry module

    try:
        # Update module for registry
        api_response = api_instance.update_module(org_short_name_id, provider_name, version, module_name, body)
        print("The response of ModuleApi->update_module:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleApi->update_module: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_short_name_id** | **str**| organization FQN | 
 **provider_name** | **str**| The name of the provider | 
 **version** | **str**| The version of the module | 
 **module_name** | **str**| The name of the module | 
 **body** | [**UpdateModuleRequest**](UpdateModuleRequest.md)| request body for updating a registry module | 

### Return type

[**Module**](Module.md)

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

