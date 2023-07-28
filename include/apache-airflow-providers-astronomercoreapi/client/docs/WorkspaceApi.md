# astronomercoreapi.WorkspaceApi

All URIs are relative to *https://api.astronomer.io/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workspace**](WorkspaceApi.md#create_workspace) | **POST** /organizations/{organizationId}/workspaces | Create workspace
[**delete_workspace**](WorkspaceApi.md#delete_workspace) | **DELETE** /organizations/{organizationId}/workspaces/{workspaceId} | Delete workspace
[**get_workspace**](WorkspaceApi.md#get_workspace) | **GET** /organizations/{organizationId}/workspaces/{workspaceId} | Get workspace with id
[**list_workspace_dag_filters**](WorkspaceApi.md#list_workspace_dag_filters) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/dag-filters | List all tag, owner and deployment names/IDs
[**list_workspace_dags**](WorkspaceApi.md#list_workspace_dags) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/dags | List all dags in a workspace
[**list_workspaces**](WorkspaceApi.md#list_workspaces) | **GET** /organizations/{organizationId}/workspaces | List Workspaces
[**update_workspace**](WorkspaceApi.md#update_workspace) | **POST** /organizations/{organizationId}/workspaces/{workspaceId} | Update workspace


# **create_workspace**
> Workspace create_workspace(organization_id, body)

Create workspace

Create workspace

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.create_workspace_request import CreateWorkspaceRequest
from astronomercoreapi.models.workspace import Workspace
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
    api_instance = astronomercoreapi.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    body = astronomercoreapi.CreateWorkspaceRequest() # CreateWorkspaceRequest | request body for creating a new workspace

    try:
        # Create workspace
        api_response = api_instance.create_workspace(organization_id, body)
        print("The response of WorkspaceApi->create_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->create_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **body** | [**CreateWorkspaceRequest**](CreateWorkspaceRequest.md)| request body for creating a new workspace | 

### Return type

[**Workspace**](Workspace.md)

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

# **delete_workspace**
> delete_workspace(organization_id, workspace_id)

Delete workspace

Delete workspace

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
    api_instance = astronomercoreapi.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace

    try:
        # Delete workspace
        api_instance.delete_workspace(organization_id, workspace_id)
    except Exception as e:
        print("Exception when calling WorkspaceApi->delete_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 

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
**200** |  |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace**
> Workspace get_workspace(organization_id, workspace_id)

Get workspace with id

Get workspace with id

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.workspace import Workspace
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
    api_instance = astronomercoreapi.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace

    try:
        # Get workspace with id
        api_response = api_instance.get_workspace(organization_id, workspace_id)
        print("The response of WorkspaceApi->get_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->get_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 

### Return type

[**Workspace**](Workspace.md)

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

# **list_workspace_dag_filters**
> DagFilters list_workspace_dag_filters(organization_id, workspace_id)

List all tag, owner and deployment names/IDs

List all tag, owner and deployment names/IDs by which DAGs can be filtered

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.dag_filters import DagFilters
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
    api_instance = astronomercoreapi.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID

    try:
        # List all tag, owner and deployment names/IDs
        api_response = api_instance.list_workspace_dag_filters(organization_id, workspace_id)
        print("The response of WorkspaceApi->list_workspace_dag_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->list_workspace_dag_filters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 

### Return type

[**DagFilters**](DagFilters.md)

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

# **list_workspace_dags**
> ListWorkspaceDags list_workspace_dags(organization_id, workspace_id, page_size=page_size, order_by=order_by, cursor=cursor, num_runs=num_runs, name=name, name__like=name__like, owner=owner, is_paused=is_paused, is_active=is_active, last_run_state__in=last_run_state__in, run_state__in=run_state__in, run_after=run_after, tag__in=tag__in, deployment_id__in=deployment_id__in)

List all dags in a workspace

List all dags in a workspace for all deployments

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.list_workspace_dags import ListWorkspaceDags
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
    api_instance = astronomercoreapi.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    page_size = 56 # int | page size, default of 20 (optional)
    order_by = ['order_by_example'] # List[str] | order-by fields, comma separated (optional)
    cursor = 'cursor_example' # str | pagination cursor (optional)
    num_runs = 56 # int | number of runs to include per dag, default of 0 (optional)
    name = 'name_example' # str | filter by name of DAG (dagId) (optional)
    name__like = 'name__like_example' # str | filter by pattern for name of DAG (dagId),  SQL  syntax (optional)
    owner = 'owner_example' # str | filter by an owner of the dag (optional)
    is_paused = True # bool | filter by paused dags (optional)
    is_active = True # bool | filter by active dags (optional)
    last_run_state__in = ['last_run_state__in_example'] # List[str] | filter by dag runs with any of these run states for its last run (optional)
    run_state__in = ['run_state__in_example'] # List[str] | filter by dag runs with any of these run states (optional)
    run_after = '2013-10-20T19:20:30+01:00' # datetime | filter by dag run after specified datetime (RFC3339 format) (optional)
    tag__in = ['tag__in_example'] # List[str] | filter by any of these tags (optional)
    deployment_id__in = ['deployment_id__in_example'] # List[str] | filter by any of these deployment IDs (optional)

    try:
        # List all dags in a workspace
        api_response = api_instance.list_workspace_dags(organization_id, workspace_id, page_size=page_size, order_by=order_by, cursor=cursor, num_runs=num_runs, name=name, name__like=name__like, owner=owner, is_paused=is_paused, is_active=is_active, last_run_state__in=last_run_state__in, run_state__in=run_state__in, run_after=run_after, tag__in=tag__in, deployment_id__in=deployment_id__in)
        print("The response of WorkspaceApi->list_workspace_dags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->list_workspace_dags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **page_size** | **int**| page size, default of 20 | [optional] 
 **order_by** | [**List[str]**](str.md)| order-by fields, comma separated | [optional] 
 **cursor** | **str**| pagination cursor | [optional] 
 **num_runs** | **int**| number of runs to include per dag, default of 0 | [optional] 
 **name** | **str**| filter by name of DAG (dagId) | [optional] 
 **name__like** | **str**| filter by pattern for name of DAG (dagId),  SQL  syntax | [optional] 
 **owner** | **str**| filter by an owner of the dag | [optional] 
 **is_paused** | **bool**| filter by paused dags | [optional] 
 **is_active** | **bool**| filter by active dags | [optional] 
 **last_run_state__in** | [**List[str]**](str.md)| filter by dag runs with any of these run states for its last run | [optional] 
 **run_state__in** | [**List[str]**](str.md)| filter by dag runs with any of these run states | [optional] 
 **run_after** | **datetime**| filter by dag run after specified datetime (RFC3339 format) | [optional] 
 **tag__in** | [**List[str]**](str.md)| filter by any of these tags | [optional] 
 **deployment_id__in** | [**List[str]**](str.md)| filter by any of these deployment IDs | [optional] 

### Return type

[**ListWorkspaceDags**](ListWorkspaceDags.md)

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

# **list_workspaces**
> WorkspacesPaginated list_workspaces(organization_id, workspace_ids=workspace_ids, offset=offset, limit=limit, sorts=sorts, search=search)

List Workspaces

List Workspaces

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.workspaces_paginated import WorkspacesPaginated
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
    api_instance = astronomercoreapi.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_ids = ['workspace_ids_example'] # List[str] | list of workspace ids to get detail of (optional)
    offset = 0 # int | offset for pagination (optional) (default to 0)
    limit = 20 # int | limit for pagination (optional) (default to 20)
    sorts = ['sorts_example'] # List[str] | sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc' (optional)
    search = 'search_example' # str | string to search for when listing workspaces (optional)

    try:
        # List Workspaces
        api_response = api_instance.list_workspaces(organization_id, workspace_ids=workspace_ids, offset=offset, limit=limit, sorts=sorts, search=search)
        print("The response of WorkspaceApi->list_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->list_workspaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_ids** | [**List[str]**](str.md)| list of workspace ids to get detail of | [optional] 
 **offset** | **int**| offset for pagination | [optional] [default to 0]
 **limit** | **int**| limit for pagination | [optional] [default to 20]
 **sorts** | [**List[str]**](str.md)| sorting criteria, each criterion should conform to format &#39;fieldName:asc&#39; or &#39;fieldName:desc&#39; | [optional] 
 **search** | **str**| string to search for when listing workspaces | [optional] 

### Return type

[**WorkspacesPaginated**](WorkspacesPaginated.md)

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

# **update_workspace**
> Workspace update_workspace(organization_id, workspace_id, body)

Update workspace

Update workspace

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.update_workspace_request import UpdateWorkspaceRequest
from astronomercoreapi.models.workspace import Workspace
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
    api_instance = astronomercoreapi.WorkspaceApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    body = astronomercoreapi.UpdateWorkspaceRequest() # UpdateWorkspaceRequest | request body for updating a workspace

    try:
        # Update workspace
        api_response = api_instance.update_workspace(organization_id, workspace_id, body)
        print("The response of WorkspaceApi->update_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->update_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **body** | [**UpdateWorkspaceRequest**](UpdateWorkspaceRequest.md)| request body for updating a workspace | 

### Return type

[**Workspace**](Workspace.md)

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

