# astronomercoreapi.DagApi

All URIs are relative to *https://api.astronomer.io/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_runs_with_groups**](DagApi.md#get_runs_with_groups) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/runtimes/{runtimeId}/dags/{dagId}/runs-with-groups | Get grid data for a dag in a runtime
[**list_dags**](DagApi.md#list_dags) | **GET** /organizations/{organizationId}/dags | List dags from workspaces for the last 14 days


# **get_runs_with_groups**
> RunsWithGroups get_runs_with_groups(organization_id, workspace_id, runtime_id, dag_id, root=root, run_state=run_state, run_type=run_type, base_date=base_date, num_runs=num_runs)

Get grid data for a dag in a runtime

Get grid data for a dag in a runtime

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.runs_with_groups import RunsWithGroups
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
    api_instance = astronomercoreapi.DagApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    runtime_id = 'runtime_id_example' # str | ID of the runtime
    dag_id = 'dag_id_example' # str | ID of the dag
    root = 'root_example' # str | name of parent task to get grid data for (optional)
    run_state = 'run_state_example' # str | run state to filter on (optional)
    run_type = 'run_type_example' # str | run type to filter on (optional)
    base_date = '2013-10-20T19:20:30+01:00' # datetime | base date (optional)
    num_runs = 'num_runs_example' # str | number of runs to select grid data for (optional)

    try:
        # Get grid data for a dag in a runtime
        api_response = api_instance.get_runs_with_groups(organization_id, workspace_id, runtime_id, dag_id, root=root, run_state=run_state, run_type=run_type, base_date=base_date, num_runs=num_runs)
        print("The response of DagApi->get_runs_with_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DagApi->get_runs_with_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **runtime_id** | **str**| ID of the runtime | 
 **dag_id** | **str**| ID of the dag | 
 **root** | **str**| name of parent task to get grid data for | [optional] 
 **run_state** | **str**| run state to filter on | [optional] 
 **run_type** | **str**| run type to filter on | [optional] 
 **base_date** | **datetime**| base date | [optional] 
 **num_runs** | **str**| number of runs to select grid data for | [optional] 

### Return type

[**RunsWithGroups**](RunsWithGroups.md)

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

# **list_dags**
> DagsPaginated list_dags(organization_id, workspace_ids=workspace_ids, deployment_ids=deployment_ids, offset=offset, limit=limit, sorts=sorts)

List dags from workspaces for the last 14 days

List dags from workspaces for the last 14 days

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.dags_paginated import DagsPaginated
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
    api_instance = astronomercoreapi.DagApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_ids = ['workspace_ids_example'] # List[str] | ID that defines the workspaces where dags belong to (optional)
    deployment_ids = ['deployment_ids_example'] # List[str] | ID that defines the deployments where dags belong to (optional)
    offset = 0 # int | offset for pagination (optional) (default to 0)
    limit = 20 # int | limit for pagination (optional) (default to 20)
    sorts = ['sorts_example'] # List[str] | sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc' (optional)

    try:
        # List dags from workspaces for the last 14 days
        api_response = api_instance.list_dags(organization_id, workspace_ids=workspace_ids, deployment_ids=deployment_ids, offset=offset, limit=limit, sorts=sorts)
        print("The response of DagApi->list_dags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DagApi->list_dags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_ids** | [**List[str]**](str.md)| ID that defines the workspaces where dags belong to | [optional] 
 **deployment_ids** | [**List[str]**](str.md)| ID that defines the deployments where dags belong to | [optional] 
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

