# astronomerregistry.DagApi

All URIs are relative to *https://api.astronomer.io/registryV2/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dag**](DagApi.md#create_dag) | **POST** /organizations/{orgShortNameId}/dags | Create dag for registry
[**delete_dag**](DagApi.md#delete_dag) | **DELETE** /organizations/{orgShortNameId}/dags/{dagName}/versions/{version} | Delete a dag
[**get_dag**](DagApi.md#get_dag) | **GET** /organizations/{orgShortNameId}/dags/{dagName}/versions/{version} | Get dag
[**list_dags**](DagApi.md#list_dags) | **GET** /organizations/{orgShortNameId}/dags | List dags
[**update_dag**](DagApi.md#update_dag) | **PUT** /organizations/{orgShortNameId}/dags/{dagName}/versions/{version} | Update dag for registry


# **create_dag**
> Dag create_dag(org_short_name_id, body)

Create dag for registry

Create dag for registry

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomerregistry
from astronomerregistry.models.create_dag_request import CreateDagRequest
from astronomerregistry.models.dag import Dag
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
    api_instance = astronomerregistry.DagApi(api_client)
    org_short_name_id = 'org_short_name_id_example' # str | organization FQN
    body = astronomerregistry.CreateDagRequest() # CreateDagRequest | request body for creating a registry dag

    try:
        # Create dag for registry
        api_response = api_instance.create_dag(org_short_name_id, body)
        print("The response of DagApi->create_dag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DagApi->create_dag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_short_name_id** | **str**| organization FQN | 
 **body** | [**CreateDagRequest**](CreateDagRequest.md)| request body for creating a registry dag | 

### Return type

[**Dag**](Dag.md)

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

# **delete_dag**
> Dag delete_dag(org_short_name_id, dag_name, version)

Delete a dag

Delete a single dag by name and version

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomerregistry
from astronomerregistry.models.dag import Dag
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
    api_instance = astronomerregistry.DagApi(api_client)
    org_short_name_id = 'org_short_name_id_example' # str | organization FQN
    dag_name = 'dag_name_example' # str | The name of the dag
    version = 'version_example' # str | The version of the dag

    try:
        # Delete a dag
        api_response = api_instance.delete_dag(org_short_name_id, dag_name, version)
        print("The response of DagApi->delete_dag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DagApi->delete_dag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_short_name_id** | **str**| organization FQN | 
 **dag_name** | **str**| The name of the dag | 
 **version** | **str**| The version of the dag | 

### Return type

[**Dag**](Dag.md)

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

# **get_dag**
> Dag get_dag(org_short_name_id, dag_name, version)

Get dag

Get a single dag by dagName and version

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomerregistry
from astronomerregistry.models.dag import Dag
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
    api_instance = astronomerregistry.DagApi(api_client)
    org_short_name_id = 'org_short_name_id_example' # str | organization FQN
    dag_name = 'dag_name_example' # str | The name or display name of the dag
    version = 'version_example' # str | The version of the dag, or keyword 'latest' for latest version

    try:
        # Get dag
        api_response = api_instance.get_dag(org_short_name_id, dag_name, version)
        print("The response of DagApi->get_dag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DagApi->get_dag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_short_name_id** | **str**| organization FQN | 
 **dag_name** | **str**| The name or display name of the dag | 
 **version** | **str**| The version of the dag, or keyword &#39;latest&#39; for latest version | 

### Return type

[**Dag**](Dag.md)

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

# **list_dags**
> DagsPaginated list_dags(org_short_name_id, is_certified=is_certified, is_featured=is_featured, is_global=is_global, is_private=is_private, is_cloud_ide_compatible=is_cloud_ide_compatible, type_name=type_name, tier_id=tier_id, category_id=category_id, badge_id=badge_id, dag_id=dag_id, module_id=module_id, provider_id=provider_id, tier_name=tier_name, category_name=category_name, badge_name=badge_name, module_name=module_name, provider_name=provider_name, query=query, offset=offset, limit=limit, sorts=sorts)

List dags

List dags

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomerregistry
from astronomerregistry.models.dags_paginated import DagsPaginated
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
    api_instance = astronomerregistry.DagApi(api_client)
    org_short_name_id = 'org_short_name_id_example' # str | organization FQN
    is_certified = True # bool | return only certified dags (optional)
    is_featured = True # bool | return only featured dags (optional)
    is_global = True # bool | return only global dags (optional)
    is_private = True # bool | return only private dags (optional)
    is_cloud_ide_compatible = True # bool | return only cloud ide compatible dags (optional)
    type_name = ['type_name_example'] # List[str] | Has at least one type in input filter list (optional)
    tier_id = ['tier_id_example'] # List[str] | Has at least one tier in input filter list (optional)
    category_id = ['category_id_example'] # List[str] | Has at least one category in input filter list (optional)
    badge_id = ['badge_id_example'] # List[str] | Has at least one badge in input filter list (optional)
    dag_id = ['dag_id_example'] # List[str] | Has one id in input filter list (optional)
    module_id = ['module_id_example'] # List[str] | Has one module in input filter list (optional)
    provider_id = ['provider_id_example'] # List[str] | Has one dag in input filter list (optional)
    tier_name = ['tier_name_example'] # List[str] | Has at least one tier name in input filter list (optional)
    category_name = ['category_name_example'] # List[str] | Has at least one category name in input filter list (optional)
    badge_name = ['badge_name_example'] # List[str] | Has at least one badge name in input filter list (optional)
    module_name = ['module_name_example'] # List[str] | Has one module name in input filter list (optional)
    provider_name = ['provider_name_example'] # List[str] | Has one provider name in input filter list (optional)
    query = 'query_example' # str | Search query for dag (optional)
    offset = 0 # int | offset for pagination (optional) (default to 0)
    limit = 20 # int | limit for pagination (optional) (default to 20)
    sorts = ['sorts_example'] # List[str] | sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc' (optional)

    try:
        # List dags
        api_response = api_instance.list_dags(org_short_name_id, is_certified=is_certified, is_featured=is_featured, is_global=is_global, is_private=is_private, is_cloud_ide_compatible=is_cloud_ide_compatible, type_name=type_name, tier_id=tier_id, category_id=category_id, badge_id=badge_id, dag_id=dag_id, module_id=module_id, provider_id=provider_id, tier_name=tier_name, category_name=category_name, badge_name=badge_name, module_name=module_name, provider_name=provider_name, query=query, offset=offset, limit=limit, sorts=sorts)
        print("The response of DagApi->list_dags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DagApi->list_dags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_short_name_id** | **str**| organization FQN | 
 **is_certified** | **bool**| return only certified dags | [optional] 
 **is_featured** | **bool**| return only featured dags | [optional] 
 **is_global** | **bool**| return only global dags | [optional] 
 **is_private** | **bool**| return only private dags | [optional] 
 **is_cloud_ide_compatible** | **bool**| return only cloud ide compatible dags | [optional] 
 **type_name** | [**List[str]**](str.md)| Has at least one type in input filter list | [optional] 
 **tier_id** | [**List[str]**](str.md)| Has at least one tier in input filter list | [optional] 
 **category_id** | [**List[str]**](str.md)| Has at least one category in input filter list | [optional] 
 **badge_id** | [**List[str]**](str.md)| Has at least one badge in input filter list | [optional] 
 **dag_id** | [**List[str]**](str.md)| Has one id in input filter list | [optional] 
 **module_id** | [**List[str]**](str.md)| Has one module in input filter list | [optional] 
 **provider_id** | [**List[str]**](str.md)| Has one dag in input filter list | [optional] 
 **tier_name** | [**List[str]**](str.md)| Has at least one tier name in input filter list | [optional] 
 **category_name** | [**List[str]**](str.md)| Has at least one category name in input filter list | [optional] 
 **badge_name** | [**List[str]**](str.md)| Has at least one badge name in input filter list | [optional] 
 **module_name** | [**List[str]**](str.md)| Has one module name in input filter list | [optional] 
 **provider_name** | [**List[str]**](str.md)| Has one provider name in input filter list | [optional] 
 **query** | **str**| Search query for dag | [optional] 
 **offset** | **int**| offset for pagination | [optional] [default to 0]
 **limit** | **int**| limit for pagination | [optional] [default to 20]
 **sorts** | [**List[str]**](str.md)| sorting criteria, each criterion should conform to format &#39;fieldName:asc&#39; or &#39;fieldName:desc&#39; | [optional] 

### Return type

[**DagsPaginated**](DagsPaginated.md)

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

# **update_dag**
> Dag update_dag(org_short_name_id, dag_name, version, body)

Update dag for registry

Update dag for registry

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomerregistry
from astronomerregistry.models.dag import Dag
from astronomerregistry.models.update_dag_request import UpdateDagRequest
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
    api_instance = astronomerregistry.DagApi(api_client)
    org_short_name_id = 'org_short_name_id_example' # str | organization FQN
    dag_name = 'dag_name_example' # str | The name of the dag
    version = 'version_example' # str | The version of the dag
    body = astronomerregistry.UpdateDagRequest() # UpdateDagRequest | request body for updating a registry dag

    try:
        # Update dag for registry
        api_response = api_instance.update_dag(org_short_name_id, dag_name, version, body)
        print("The response of DagApi->update_dag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DagApi->update_dag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_short_name_id** | **str**| organization FQN | 
 **dag_name** | **str**| The name of the dag | 
 **version** | **str**| The version of the dag | 
 **body** | [**UpdateDagRequest**](UpdateDagRequest.md)| request body for updating a registry dag | 

### Return type

[**Dag**](Dag.md)

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

