# astronomercoreapi.WorkspaceMetricsApi

All URIs are relative to *https://api.astronomer.io/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_workspace_dag_runs**](WorkspaceMetricsApi.md#get_workspace_dag_runs) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/metrics/dag-runs-per-status | Get DAG runs metrics for a workspace
[**get_workspace_task_runs**](WorkspaceMetricsApi.md#get_workspace_task_runs) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/metrics/task-runs-per-status | Get task runs metrics for a workspace


# **get_workspace_dag_runs**
> List[WorkspaceRangeMetricPerStatus] get_workspace_dag_runs(organization_id, workspace_id, range, step, deployment_ids=deployment_ids, virtual_runtime_ids=virtual_runtime_ids, runtime_type=runtime_type, status=status)

Get DAG runs metrics for a workspace

Get DAG runs metrics for a workspace

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.workspace_range_metric_per_status import WorkspaceRangeMetricPerStatus
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
    api_instance = astronomercoreapi.WorkspaceMetricsApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID that defines the workspace
    range = 56 # int | range of the DAG runs metrics in seconds
    step = 56 # int | step interval of the DAG runs metrics in seconds
    deployment_ids = 'deployment_ids_example' # str | IDs that define the deployments, separated by comma (optional)
    virtual_runtime_ids = 'virtual_runtime_ids_example' # str | IDs that define the virtual runtimes, separated by comma (optional)
    runtime_type = 'runtime_type_example' # str | type of runtime (optional)
    status = 'status_example' # str | status of dag runs (optional)

    try:
        # Get DAG runs metrics for a workspace
        api_response = api_instance.get_workspace_dag_runs(organization_id, workspace_id, range, step, deployment_ids=deployment_ids, virtual_runtime_ids=virtual_runtime_ids, runtime_type=runtime_type, status=status)
        print("The response of WorkspaceMetricsApi->get_workspace_dag_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceMetricsApi->get_workspace_dag_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID that defines the workspace | 
 **range** | **int**| range of the DAG runs metrics in seconds | 
 **step** | **int**| step interval of the DAG runs metrics in seconds | 
 **deployment_ids** | **str**| IDs that define the deployments, separated by comma | [optional] 
 **virtual_runtime_ids** | **str**| IDs that define the virtual runtimes, separated by comma | [optional] 
 **runtime_type** | **str**| type of runtime | [optional] 
 **status** | **str**| status of dag runs | [optional] 

### Return type

[**List[WorkspaceRangeMetricPerStatus]**](WorkspaceRangeMetricPerStatus.md)

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
**499** |  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_task_runs**
> List[WorkspaceRangeMetricPerStatus] get_workspace_task_runs(organization_id, workspace_id, range, step, deployment_ids=deployment_ids, virtual_runtime_ids=virtual_runtime_ids, runtime_type=runtime_type, status=status, include_deleted_deployments=include_deleted_deployments)

Get task runs metrics for a workspace

Get task runs metrics for a workspace

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.workspace_range_metric_per_status import WorkspaceRangeMetricPerStatus
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
    api_instance = astronomercoreapi.WorkspaceMetricsApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID that defines the workspace
    range = 56 # int | range of the task runs metric in seconds
    step = 56 # int | step interval of task runs metric in seconds
    deployment_ids = 'deployment_ids_example' # str | IDs that define the deployments, separated by comma (optional)
    virtual_runtime_ids = 'virtual_runtime_ids_example' # str | IDs that define the virtual runtimes, separated by comma (optional)
    runtime_type = 'runtime_type_example' # str | type of runtime (optional)
    status = 'status_example' # str | status of task runs (optional)
    include_deleted_deployments = True # bool | results should include data from soft deleted deployments (optional)

    try:
        # Get task runs metrics for a workspace
        api_response = api_instance.get_workspace_task_runs(organization_id, workspace_id, range, step, deployment_ids=deployment_ids, virtual_runtime_ids=virtual_runtime_ids, runtime_type=runtime_type, status=status, include_deleted_deployments=include_deleted_deployments)
        print("The response of WorkspaceMetricsApi->get_workspace_task_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceMetricsApi->get_workspace_task_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID that defines the workspace | 
 **range** | **int**| range of the task runs metric in seconds | 
 **step** | **int**| step interval of task runs metric in seconds | 
 **deployment_ids** | **str**| IDs that define the deployments, separated by comma | [optional] 
 **virtual_runtime_ids** | **str**| IDs that define the virtual runtimes, separated by comma | [optional] 
 **runtime_type** | **str**| type of runtime | [optional] 
 **status** | **str**| status of task runs | [optional] 
 **include_deleted_deployments** | **bool**| results should include data from soft deleted deployments | [optional] 

### Return type

[**List[WorkspaceRangeMetricPerStatus]**](WorkspaceRangeMetricPerStatus.md)

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

