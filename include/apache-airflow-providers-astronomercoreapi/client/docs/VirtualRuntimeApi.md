# astronomercoreapi.VirtualRuntimeApi

All URIs are relative to *https://api.astronomer.io/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connection**](VirtualRuntimeApi.md#create_connection) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/virtual-runtimes/{virtualRuntimeId}/connections | Deprecated - Create connection
[**create_virtual_runtime**](VirtualRuntimeApi.md#create_virtual_runtime) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/virtual-runtimes | Deprecated - Create virtual runtime
[**delete_connection**](VirtualRuntimeApi.md#delete_connection) | **DELETE** /organizations/{organizationId}/workspaces/{workspaceId}/virtual-runtimes/{virtualRuntimeId}/connections/{connectionId} | Deprecated - Delete connection
[**delete_virtual_runtime**](VirtualRuntimeApi.md#delete_virtual_runtime) | **DELETE** /organizations/{organizationId}/workspaces/{workspaceId}/virtual-runtimes/{virtualRuntimeId} | Deprecated - Delete virtual runtime
[**get_connection**](VirtualRuntimeApi.md#get_connection) | **GET** /organizations/{organizationId}/virtual-runtimes/{virtualRuntimeId}/connections/{connectionId} | Deprecated - Get connection
[**get_virtual_runtime**](VirtualRuntimeApi.md#get_virtual_runtime) | **GET** /organizations/{organizationId}/virtual-runtimes/{virtualRuntimeId} | Deprecated - Get virtual runtime
[**list_connections**](VirtualRuntimeApi.md#list_connections) | **GET** /organizations/{organizationId}/virtual-runtimes/{virtualRuntimeId}/connections | Deprecated - List connections for a virtual runtime
[**list_requirements**](VirtualRuntimeApi.md#list_requirements) | **GET** /organizations/{organizationId}/virtual-runtimes/{virtualRuntimeId}/requirements | Deprecated - List virtual runtime requirements
[**list_variables**](VirtualRuntimeApi.md#list_variables) | **GET** /organizations/{organizationId}/virtual-runtimes/{virtualRuntimeId}/variables | Deprecated - List virtual runtime variables
[**list_virtual_runtimes**](VirtualRuntimeApi.md#list_virtual_runtimes) | **GET** /organizations/{organizationId}/virtual-runtimes | Deprecated - List virtual runtimes in a workspace
[**list_vr_dag_run_task_instances**](VirtualRuntimeApi.md#list_vr_dag_run_task_instances) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/virtual-runtimes/{virtualRuntimeId}/dags/{dagId}/runs/{dagRunId}/task-instances | Deprecated - List task instances for dag run in a virtual runtime
[**list_vr_dag_runs**](VirtualRuntimeApi.md#list_vr_dag_runs) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/virtual-runtimes/{virtualRuntimeId}/dags/{dagId}/runs | Deprecated - List dag runs for a dag in a virtual runtime
[**list_vr_dags**](VirtualRuntimeApi.md#list_vr_dags) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/virtual-runtimes/{virtualRuntimeId}/dags | Deprecated - List all dags in a virtual runtime
[**list_vr_import_errors**](VirtualRuntimeApi.md#list_vr_import_errors) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/virtual-runtimes/{virtualRuntimeId}/import-errors | Deprecated - List all import errors in a virtual runtime
[**mutate_requirements**](VirtualRuntimeApi.md#mutate_requirements) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/virtual-runtimes/{virtualRuntimeId}/requirements | Deprecated - Mutate virtual runtime requirements
[**mutate_variables**](VirtualRuntimeApi.md#mutate_variables) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/virtual-runtimes/{virtualRuntimeId}/variables | Deprecated - Mutate virtual runtime variables
[**pause_dag**](VirtualRuntimeApi.md#pause_dag) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/virtual-runtimes/{virtualRuntimeId}/dags/{dagId}/pause | Deprecated - Pause a dag
[**post_dag_run**](VirtualRuntimeApi.md#post_dag_run) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/virtual-runtimes/{virtualRuntimeId}/dags/{dagId}/run | Deprecated - Triggers a dag run
[**resume_dag**](VirtualRuntimeApi.md#resume_dag) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/virtual-runtimes/{virtualRuntimeId}/dags/{dagId}/resume | Deprecated - Update a dag
[**update_connection**](VirtualRuntimeApi.md#update_connection) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/virtual-runtimes/{virtualRuntimeId}/connections/{connectionId} | Deprecated - Update connection
[**update_virtual_runtime**](VirtualRuntimeApi.md#update_virtual_runtime) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/virtual-runtimes/{virtualRuntimeId} | Deprecated - Update virtual runtime


# **create_connection**
> Connection create_connection(organization_id, workspace_id, virtual_runtime_id, data)

Deprecated - Create connection

Deprecated - Create connection

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.connection import Connection
from astronomercoreapi.models.mutate_connection_request import MutateConnectionRequest
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
    api_instance = astronomercoreapi.VirtualRuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    virtual_runtime_id = 'virtual_runtime_id_example' # str | ID of the virtual runtime
    data = astronomercoreapi.MutateConnectionRequest() # MutateConnectionRequest | request body for creating a new connection

    try:
        # Deprecated - Create connection
        api_response = api_instance.create_connection(organization_id, workspace_id, virtual_runtime_id, data)
        print("The response of VirtualRuntimeApi->create_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualRuntimeApi->create_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **virtual_runtime_id** | **str**| ID of the virtual runtime | 
 **data** | [**MutateConnectionRequest**](MutateConnectionRequest.md)| request body for creating a new connection | 

### Return type

[**Connection**](Connection.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_virtual_runtime**
> VirtualRuntime create_virtual_runtime(organization_id, workspace_id, body)

Deprecated - Create virtual runtime

Deprecated - Create virtual runtime

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.mutate_virtual_runtime_request import MutateVirtualRuntimeRequest
from astronomercoreapi.models.virtual_runtime import VirtualRuntime
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
    api_instance = astronomercoreapi.VirtualRuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    body = astronomercoreapi.MutateVirtualRuntimeRequest() # MutateVirtualRuntimeRequest | request body for creating a virtual runtime

    try:
        # Deprecated - Create virtual runtime
        api_response = api_instance.create_virtual_runtime(organization_id, workspace_id, body)
        print("The response of VirtualRuntimeApi->create_virtual_runtime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualRuntimeApi->create_virtual_runtime: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **body** | [**MutateVirtualRuntimeRequest**](MutateVirtualRuntimeRequest.md)| request body for creating a virtual runtime | 

### Return type

[**VirtualRuntime**](VirtualRuntime.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection**
> delete_connection(organization_id, workspace_id, virtual_runtime_id, connection_id)

Deprecated - Delete connection

Deprecated - Delete connection

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
    api_instance = astronomercoreapi.VirtualRuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    virtual_runtime_id = 'virtual_runtime_id_example' # str | ID of the virtual runtime
    connection_id = 'connection_id_example' # str | ID of the connection

    try:
        # Deprecated - Delete connection
        api_instance.delete_connection(organization_id, workspace_id, virtual_runtime_id, connection_id)
    except Exception as e:
        print("Exception when calling VirtualRuntimeApi->delete_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **virtual_runtime_id** | **str**| ID of the virtual runtime | 
 **connection_id** | **str**| ID of the connection | 

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_virtual_runtime**
> delete_virtual_runtime(organization_id, workspace_id, virtual_runtime_id)

Deprecated - Delete virtual runtime

Deprecated - Delete virtual runtime

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
    api_instance = astronomercoreapi.VirtualRuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    virtual_runtime_id = 'virtual_runtime_id_example' # str | ID of the virtual runtime

    try:
        # Deprecated - Delete virtual runtime
        api_instance.delete_virtual_runtime(organization_id, workspace_id, virtual_runtime_id)
    except Exception as e:
        print("Exception when calling VirtualRuntimeApi->delete_virtual_runtime: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **virtual_runtime_id** | **str**| ID of the virtual runtime | 

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection**
> Connection get_connection(organization_id, virtual_runtime_id, connection_id)

Deprecated - Get connection

Deprecated - Get connection

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.connection import Connection
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
    api_instance = astronomercoreapi.VirtualRuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    virtual_runtime_id = 'virtual_runtime_id_example' # str | ID of the virtual runtime
    connection_id = 'connection_id_example' # str | ID of the connection

    try:
        # Deprecated - Get connection
        api_response = api_instance.get_connection(organization_id, virtual_runtime_id, connection_id)
        print("The response of VirtualRuntimeApi->get_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualRuntimeApi->get_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **virtual_runtime_id** | **str**| ID of the virtual runtime | 
 **connection_id** | **str**| ID of the connection | 

### Return type

[**Connection**](Connection.md)

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

# **get_virtual_runtime**
> VirtualRuntime get_virtual_runtime(organization_id, virtual_runtime_id)

Deprecated - Get virtual runtime

Deprecated - Get virtual runtime

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.virtual_runtime import VirtualRuntime
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
    api_instance = astronomercoreapi.VirtualRuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    virtual_runtime_id = 'virtual_runtime_id_example' # str | ID of the virtual runtime

    try:
        # Deprecated - Get virtual runtime
        api_response = api_instance.get_virtual_runtime(organization_id, virtual_runtime_id)
        print("The response of VirtualRuntimeApi->get_virtual_runtime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualRuntimeApi->get_virtual_runtime: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **virtual_runtime_id** | **str**| ID of the virtual runtime | 

### Return type

[**VirtualRuntime**](VirtualRuntime.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connections**
> ConnectionsPaginated list_connections(organization_id, virtual_runtime_id, offset=offset, limit=limit, sorts=sorts)

Deprecated - List connections for a virtual runtime

Deprecated - List connections for a virtual runtime

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.connections_paginated import ConnectionsPaginated
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
    api_instance = astronomercoreapi.VirtualRuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    virtual_runtime_id = 'virtual_runtime_id_example' # str | ID of the virtual runtime
    offset = 0 # int | offset for pagination (optional) (default to 0)
    limit = 20 # int | limit for pagination (optional) (default to 20)
    sorts = ['sorts_example'] # List[str] | sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc' (optional)

    try:
        # Deprecated - List connections for a virtual runtime
        api_response = api_instance.list_connections(organization_id, virtual_runtime_id, offset=offset, limit=limit, sorts=sorts)
        print("The response of VirtualRuntimeApi->list_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualRuntimeApi->list_connections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **virtual_runtime_id** | **str**| ID of the virtual runtime | 
 **offset** | **int**| offset for pagination | [optional] [default to 0]
 **limit** | **int**| limit for pagination | [optional] [default to 20]
 **sorts** | [**List[str]**](str.md)| sorting criteria, each criterion should conform to format &#39;fieldName:asc&#39; or &#39;fieldName:desc&#39; | [optional] 

### Return type

[**ConnectionsPaginated**](ConnectionsPaginated.md)

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

# **list_requirements**
> VRRequirements list_requirements(organization_id, virtual_runtime_id)

Deprecated - List virtual runtime requirements

Deprecated - List virtual runtime requirements

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.vr_requirements import VRRequirements
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
    api_instance = astronomercoreapi.VirtualRuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    virtual_runtime_id = 'virtual_runtime_id_example' # str | ID of the virtual runtime

    try:
        # Deprecated - List virtual runtime requirements
        api_response = api_instance.list_requirements(organization_id, virtual_runtime_id)
        print("The response of VirtualRuntimeApi->list_requirements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualRuntimeApi->list_requirements: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **virtual_runtime_id** | **str**| ID of the virtual runtime | 

### Return type

[**VRRequirements**](VRRequirements.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_variables**
> VRVariables list_variables(organization_id, virtual_runtime_id)

Deprecated - List virtual runtime variables

Deprecated - List virtual runtime variables

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.vr_variables import VRVariables
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
    api_instance = astronomercoreapi.VirtualRuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    virtual_runtime_id = 'virtual_runtime_id_example' # str | ID of the virtual runtime

    try:
        # Deprecated - List virtual runtime variables
        api_response = api_instance.list_variables(organization_id, virtual_runtime_id)
        print("The response of VirtualRuntimeApi->list_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualRuntimeApi->list_variables: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **virtual_runtime_id** | **str**| ID of the virtual runtime | 

### Return type

[**VRVariables**](VRVariables.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtual_runtimes**
> VirtualRuntimesPaginated list_virtual_runtimes(organization_id, workspace_ids=workspace_ids, offset=offset, limit=limit, sorts=sorts)

Deprecated - List virtual runtimes in a workspace

Deprecated - List virtual runtimes in a workspace

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.virtual_runtimes_paginated import VirtualRuntimesPaginated
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
    api_instance = astronomercoreapi.VirtualRuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_ids = ['workspace_ids_example'] # List[str] | IDs that define the workspaces where virtual runtimes belong to (optional)
    offset = 0 # int | offset for pagination (optional) (default to 0)
    limit = 20 # int | limit for pagination (optional) (default to 20)
    sorts = ['sorts_example'] # List[str] | sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc' (optional)

    try:
        # Deprecated - List virtual runtimes in a workspace
        api_response = api_instance.list_virtual_runtimes(organization_id, workspace_ids=workspace_ids, offset=offset, limit=limit, sorts=sorts)
        print("The response of VirtualRuntimeApi->list_virtual_runtimes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualRuntimeApi->list_virtual_runtimes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_ids** | [**List[str]**](str.md)| IDs that define the workspaces where virtual runtimes belong to | [optional] 
 **offset** | **int**| offset for pagination | [optional] [default to 0]
 **limit** | **int**| limit for pagination | [optional] [default to 20]
 **sorts** | [**List[str]**](str.md)| sorting criteria, each criterion should conform to format &#39;fieldName:asc&#39; or &#39;fieldName:desc&#39; | [optional] 

### Return type

[**VirtualRuntimesPaginated**](VirtualRuntimesPaginated.md)

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

# **list_vr_dag_run_task_instances**
> VRDagRunTaskInstancesPaginated list_vr_dag_run_task_instances(organization_id, workspace_id, virtual_runtime_id, dag_id, dag_run_id, offset=offset, limit=limit, execution_date_gte=execution_date_gte, execution_date_lte=execution_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte, duration_sec_gte=duration_sec_gte, duration_sec_lte=duration_sec_lte, states=states, pools=pools, queues=queues)

Deprecated - List task instances for dag run in a virtual runtime

Deprecated - List task instances for dag run in a virtual runtime

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.vr_dag_run_task_instances_paginated import VRDagRunTaskInstancesPaginated
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
    api_instance = astronomercoreapi.VirtualRuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    virtual_runtime_id = 'virtual_runtime_id_example' # str | ID of the virtual runtime
    dag_id = 'dag_id_example' # str | ID of the dag
    dag_run_id = 'dag_run_id_example' # str | ID of the dag run
    offset = 0 # int | offset for pagination (optional) (default to 0)
    limit = 20 # int | limit for pagination (optional) (default to 20)
    execution_date_gte = '2013-10-20T19:20:30+01:00' # datetime | execution date is greater or equal to the specified date (optional)
    execution_date_lte = '2013-10-20T19:20:30+01:00' # datetime | execution date is less than or equal to the specified date (optional)
    start_date_gte = '2013-10-20T19:20:30+01:00' # datetime | start date is greater than or equal to the specified date (optional)
    start_date_lte = '2013-10-20T19:20:30+01:00' # datetime | start date is less than or equal to the specified date (optional)
    end_date_gte = '2013-10-20T19:20:30+01:00' # datetime | end date is greater than or equal to the specified date (optional)
    end_date_lte = '2013-10-20T19:20:30+01:00' # datetime | end date is less than or equal to the specified date (optional)
    duration_sec_gte = 3.4 # float | duration is greater than or equal to the specified in seconds (optional)
    duration_sec_lte = 3.4 # float | duration is less than or equal to the specified in seconds (optional)
    states = ['states_example'] # List[str] | task states (optional)
    pools = ['pools_example'] # List[str] | task pools (optional)
    queues = ['queues_example'] # List[str] | task queues (optional)

    try:
        # Deprecated - List task instances for dag run in a virtual runtime
        api_response = api_instance.list_vr_dag_run_task_instances(organization_id, workspace_id, virtual_runtime_id, dag_id, dag_run_id, offset=offset, limit=limit, execution_date_gte=execution_date_gte, execution_date_lte=execution_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte, duration_sec_gte=duration_sec_gte, duration_sec_lte=duration_sec_lte, states=states, pools=pools, queues=queues)
        print("The response of VirtualRuntimeApi->list_vr_dag_run_task_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualRuntimeApi->list_vr_dag_run_task_instances: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **virtual_runtime_id** | **str**| ID of the virtual runtime | 
 **dag_id** | **str**| ID of the dag | 
 **dag_run_id** | **str**| ID of the dag run | 
 **offset** | **int**| offset for pagination | [optional] [default to 0]
 **limit** | **int**| limit for pagination | [optional] [default to 20]
 **execution_date_gte** | **datetime**| execution date is greater or equal to the specified date | [optional] 
 **execution_date_lte** | **datetime**| execution date is less than or equal to the specified date | [optional] 
 **start_date_gte** | **datetime**| start date is greater than or equal to the specified date | [optional] 
 **start_date_lte** | **datetime**| start date is less than or equal to the specified date | [optional] 
 **end_date_gte** | **datetime**| end date is greater than or equal to the specified date | [optional] 
 **end_date_lte** | **datetime**| end date is less than or equal to the specified date | [optional] 
 **duration_sec_gte** | **float**| duration is greater than or equal to the specified in seconds | [optional] 
 **duration_sec_lte** | **float**| duration is less than or equal to the specified in seconds | [optional] 
 **states** | [**List[str]**](str.md)| task states | [optional] 
 **pools** | [**List[str]**](str.md)| task pools | [optional] 
 **queues** | [**List[str]**](str.md)| task queues | [optional] 

### Return type

[**VRDagRunTaskInstancesPaginated**](VRDagRunTaskInstancesPaginated.md)

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

# **list_vr_dag_runs**
> VRDagRunsPaginated list_vr_dag_runs(organization_id, workspace_id, virtual_runtime_id, dag_id, offset=offset, limit=limit, order_by=order_by, state=state, execution_date_gte=execution_date_gte, execution_date_lte=execution_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte)

Deprecated - List dag runs for a dag in a virtual runtime

Deprecated - List dag runs for a dag in a virtual runtime

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.vr_dag_runs_paginated import VRDagRunsPaginated
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
    api_instance = astronomercoreapi.VirtualRuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    virtual_runtime_id = 'virtual_runtime_id_example' # str | ID of the virtual runtime
    dag_id = 'dag_id_example' # str | ID of the dag
    offset = 0 # int | offset for pagination (optional) (default to 0)
    limit = 20 # int | limit for pagination (optional) (default to 20)
    order_by = 'order_by_example' # str | order list by the field name (optional)
    state = 'state_example' # str | list of state of dag runs, separated by comma (OR condition) (optional)
    execution_date_gte = '2013-10-20T19:20:30+01:00' # datetime | returns runs executed on date greater than or equal to specified date (optional)
    execution_date_lte = '2013-10-20T19:20:30+01:00' # datetime | returns runs executed on date less than or equal to specified date (optional)
    start_date_gte = '2013-10-20T19:20:30+01:00' # datetime | returns runs started on date greater than or equal to specified date (optional)
    start_date_lte = '2013-10-20T19:20:30+01:00' # datetime | returns runs started on date less than or equal to specified date (optional)
    end_date_gte = '2013-10-20T19:20:30+01:00' # datetime | returns runs ended on date greater than or equal to specified date (optional)
    end_date_lte = '2013-10-20T19:20:30+01:00' # datetime | returns runs ended on date less than or equal to specified date (optional)

    try:
        # Deprecated - List dag runs for a dag in a virtual runtime
        api_response = api_instance.list_vr_dag_runs(organization_id, workspace_id, virtual_runtime_id, dag_id, offset=offset, limit=limit, order_by=order_by, state=state, execution_date_gte=execution_date_gte, execution_date_lte=execution_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte)
        print("The response of VirtualRuntimeApi->list_vr_dag_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualRuntimeApi->list_vr_dag_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **virtual_runtime_id** | **str**| ID of the virtual runtime | 
 **dag_id** | **str**| ID of the dag | 
 **offset** | **int**| offset for pagination | [optional] [default to 0]
 **limit** | **int**| limit for pagination | [optional] [default to 20]
 **order_by** | **str**| order list by the field name | [optional] 
 **state** | **str**| list of state of dag runs, separated by comma (OR condition) | [optional] 
 **execution_date_gte** | **datetime**| returns runs executed on date greater than or equal to specified date | [optional] 
 **execution_date_lte** | **datetime**| returns runs executed on date less than or equal to specified date | [optional] 
 **start_date_gte** | **datetime**| returns runs started on date greater than or equal to specified date | [optional] 
 **start_date_lte** | **datetime**| returns runs started on date less than or equal to specified date | [optional] 
 **end_date_gte** | **datetime**| returns runs ended on date greater than or equal to specified date | [optional] 
 **end_date_lte** | **datetime**| returns runs ended on date less than or equal to specified date | [optional] 

### Return type

[**VRDagRunsPaginated**](VRDagRunsPaginated.md)

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

# **list_vr_dags**
> VRDagsPaginated list_vr_dags(organization_id, workspace_id, virtual_runtime_id, offset=offset, limit=limit, order_by=order_by, tags=tags, only_active=only_active, dag_id_pattern=dag_id_pattern)

Deprecated - List all dags in a virtual runtime

Deprecated - List all dags in a virtual runtime

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.vr_dags_paginated import VRDagsPaginated
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
    api_instance = astronomercoreapi.VirtualRuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    virtual_runtime_id = 'virtual_runtime_id_example' # str | ID of the virtual runtime
    offset = 0 # int | offset for pagination (optional) (default to 0)
    limit = 20 # int | limit for pagination (optional) (default to 20)
    order_by = 'order_by_example' # str | order list by the field name (optional)
    tags = 'tags_example' # str | tags (optional)
    only_active = True # bool | show only active dags (optional)
    dag_id_pattern = 'dag_id_pattern_example' # str | show dags that match this pattern (optional)

    try:
        # Deprecated - List all dags in a virtual runtime
        api_response = api_instance.list_vr_dags(organization_id, workspace_id, virtual_runtime_id, offset=offset, limit=limit, order_by=order_by, tags=tags, only_active=only_active, dag_id_pattern=dag_id_pattern)
        print("The response of VirtualRuntimeApi->list_vr_dags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualRuntimeApi->list_vr_dags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **virtual_runtime_id** | **str**| ID of the virtual runtime | 
 **offset** | **int**| offset for pagination | [optional] [default to 0]
 **limit** | **int**| limit for pagination | [optional] [default to 20]
 **order_by** | **str**| order list by the field name | [optional] 
 **tags** | **str**| tags | [optional] 
 **only_active** | **bool**| show only active dags | [optional] 
 **dag_id_pattern** | **str**| show dags that match this pattern | [optional] 

### Return type

[**VRDagsPaginated**](VRDagsPaginated.md)

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

# **list_vr_import_errors**
> VRImportErrorsPaginated list_vr_import_errors(organization_id, workspace_id, virtual_runtime_id, offset=offset, limit=limit, order_by=order_by)

Deprecated - List all import errors in a virtual runtime

Deprecated - List all import errors in a virtual runtime

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.vr_import_errors_paginated import VRImportErrorsPaginated
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
    api_instance = astronomercoreapi.VirtualRuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    virtual_runtime_id = 'virtual_runtime_id_example' # str | ID of the virtual runtime
    offset = 0 # int | offset for pagination (optional) (default to 0)
    limit = 20 # int | limit for pagination (optional) (default to 20)
    order_by = 'order_by_example' # str | order list by the field name (optional)

    try:
        # Deprecated - List all import errors in a virtual runtime
        api_response = api_instance.list_vr_import_errors(organization_id, workspace_id, virtual_runtime_id, offset=offset, limit=limit, order_by=order_by)
        print("The response of VirtualRuntimeApi->list_vr_import_errors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualRuntimeApi->list_vr_import_errors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **virtual_runtime_id** | **str**| ID of the virtual runtime | 
 **offset** | **int**| offset for pagination | [optional] [default to 0]
 **limit** | **int**| limit for pagination | [optional] [default to 20]
 **order_by** | **str**| order list by the field name | [optional] 

### Return type

[**VRImportErrorsPaginated**](VRImportErrorsPaginated.md)

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

# **mutate_requirements**
> VRRequirements mutate_requirements(organization_id, workspace_id, virtual_runtime_id, data)

Deprecated - Mutate virtual runtime requirements

Deprecated - Mutate virtual runtime requirements

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.mutate_vr_requirements_request import MutateVRRequirementsRequest
from astronomercoreapi.models.vr_requirements import VRRequirements
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
    api_instance = astronomercoreapi.VirtualRuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    virtual_runtime_id = 'virtual_runtime_id_example' # str | ID of the virtual runtime
    data = astronomercoreapi.MutateVRRequirementsRequest() # MutateVRRequirementsRequest | request body for mutating virtual runtime requirements

    try:
        # Deprecated - Mutate virtual runtime requirements
        api_response = api_instance.mutate_requirements(organization_id, workspace_id, virtual_runtime_id, data)
        print("The response of VirtualRuntimeApi->mutate_requirements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualRuntimeApi->mutate_requirements: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **virtual_runtime_id** | **str**| ID of the virtual runtime | 
 **data** | [**MutateVRRequirementsRequest**](MutateVRRequirementsRequest.md)| request body for mutating virtual runtime requirements | 

### Return type

[**VRRequirements**](VRRequirements.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mutate_variables**
> VRVariables mutate_variables(organization_id, workspace_id, virtual_runtime_id, data)

Deprecated - Mutate virtual runtime variables

Deprecated - Mutate virtual runtime variables

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.mutate_vr_variables_request import MutateVRVariablesRequest
from astronomercoreapi.models.vr_variables import VRVariables
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
    api_instance = astronomercoreapi.VirtualRuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    virtual_runtime_id = 'virtual_runtime_id_example' # str | ID of the virtual runtime
    data = astronomercoreapi.MutateVRVariablesRequest() # MutateVRVariablesRequest | request body for mutating virtual runtime variables

    try:
        # Deprecated - Mutate virtual runtime variables
        api_response = api_instance.mutate_variables(organization_id, workspace_id, virtual_runtime_id, data)
        print("The response of VirtualRuntimeApi->mutate_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualRuntimeApi->mutate_variables: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **virtual_runtime_id** | **str**| ID of the virtual runtime | 
 **data** | [**MutateVRVariablesRequest**](MutateVRVariablesRequest.md)| request body for mutating virtual runtime variables | 

### Return type

[**VRVariables**](VRVariables.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_dag**
> UpdateDag pause_dag(organization_id, workspace_id, virtual_runtime_id, dag_id)

Deprecated - Pause a dag

Deprecated - API provides a simple way for a dag to be updated with is_paused: true

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.update_dag import UpdateDag
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
    api_instance = astronomercoreapi.VirtualRuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    virtual_runtime_id = 'virtual_runtime_id_example' # str | ID of the virtual runtime
    dag_id = 'dag_id_example' # str | ID of the dag

    try:
        # Deprecated - Pause a dag
        api_response = api_instance.pause_dag(organization_id, workspace_id, virtual_runtime_id, dag_id)
        print("The response of VirtualRuntimeApi->pause_dag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualRuntimeApi->pause_dag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **virtual_runtime_id** | **str**| ID of the virtual runtime | 
 **dag_id** | **str**| ID of the dag | 

### Return type

[**UpdateDag**](UpdateDag.md)

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

# **post_dag_run**
> PostDagRun post_dag_run(organization_id, workspace_id, virtual_runtime_id, dag_id, data)

Deprecated - Triggers a dag run

Deprecated - Triggers a dag run

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.post_dag_run import PostDagRun
from astronomercoreapi.models.post_dag_run_request import PostDagRunRequest
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
    api_instance = astronomercoreapi.VirtualRuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    virtual_runtime_id = 'virtual_runtime_id_example' # str | ID of the virtual runtime
    dag_id = 'dag_id_example' # str | ID of the dag
    data = astronomercoreapi.PostDagRunRequest() # PostDagRunRequest | request body for trigger a dag run

    try:
        # Deprecated - Triggers a dag run
        api_response = api_instance.post_dag_run(organization_id, workspace_id, virtual_runtime_id, dag_id, data)
        print("The response of VirtualRuntimeApi->post_dag_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualRuntimeApi->post_dag_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **virtual_runtime_id** | **str**| ID of the virtual runtime | 
 **dag_id** | **str**| ID of the dag | 
 **data** | [**PostDagRunRequest**](PostDagRunRequest.md)| request body for trigger a dag run | 

### Return type

[**PostDagRun**](PostDagRun.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_dag**
> UpdateDag resume_dag(organization_id, workspace_id, virtual_runtime_id, dag_id)

Deprecated - Update a dag

Deprecated - API provides a way to update the is_paused field on a Dag

### Example

```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.update_dag import UpdateDag
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
    api_instance = astronomercoreapi.VirtualRuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    virtual_runtime_id = 'virtual_runtime_id_example' # str | ID of the virtual runtime
    dag_id = 'dag_id_example' # str | ID of the dag

    try:
        # Deprecated - Update a dag
        api_response = api_instance.resume_dag(organization_id, workspace_id, virtual_runtime_id, dag_id)
        print("The response of VirtualRuntimeApi->resume_dag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualRuntimeApi->resume_dag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **virtual_runtime_id** | **str**| ID of the virtual runtime | 
 **dag_id** | **str**| ID of the dag | 

### Return type

[**UpdateDag**](UpdateDag.md)

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

# **update_connection**
> Connection update_connection(organization_id, workspace_id, virtual_runtime_id, connection_id, data)

Deprecated - Update connection

Deprecated - Update connection

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.connection import Connection
from astronomercoreapi.models.mutate_connection_request import MutateConnectionRequest
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
    api_instance = astronomercoreapi.VirtualRuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    virtual_runtime_id = 'virtual_runtime_id_example' # str | ID of the virtual runtime
    connection_id = 'connection_id_example' # str | ID of the connection
    data = astronomercoreapi.MutateConnectionRequest() # MutateConnectionRequest | request body for updating a connection

    try:
        # Deprecated - Update connection
        api_response = api_instance.update_connection(organization_id, workspace_id, virtual_runtime_id, connection_id, data)
        print("The response of VirtualRuntimeApi->update_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualRuntimeApi->update_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **virtual_runtime_id** | **str**| ID of the virtual runtime | 
 **connection_id** | **str**| ID of the connection | 
 **data** | [**MutateConnectionRequest**](MutateConnectionRequest.md)| request body for updating a connection | 

### Return type

[**Connection**](Connection.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_virtual_runtime**
> VirtualRuntime update_virtual_runtime(organization_id, workspace_id, virtual_runtime_id, body)

Deprecated - Update virtual runtime

Deprecated - Update virtual runtime

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.mutate_virtual_runtime_request import MutateVirtualRuntimeRequest
from astronomercoreapi.models.virtual_runtime import VirtualRuntime
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
    api_instance = astronomercoreapi.VirtualRuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    virtual_runtime_id = 'virtual_runtime_id_example' # str | ID of the virtual runtime
    body = astronomercoreapi.MutateVirtualRuntimeRequest() # MutateVirtualRuntimeRequest | request body for updating a virtual runtime

    try:
        # Deprecated - Update virtual runtime
        api_response = api_instance.update_virtual_runtime(organization_id, workspace_id, virtual_runtime_id, body)
        print("The response of VirtualRuntimeApi->update_virtual_runtime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualRuntimeApi->update_virtual_runtime: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **virtual_runtime_id** | **str**| ID of the virtual runtime | 
 **body** | [**MutateVirtualRuntimeRequest**](MutateVirtualRuntimeRequest.md)| request body for updating a virtual runtime | 

### Return type

[**VirtualRuntime**](VirtualRuntime.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

