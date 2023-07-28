# astronomercoreapi.CloudIDERunApi

All URIs are relative to *https://api.astronomer.io/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cell_run**](CloudIDERunApi.md#create_cell_run) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/pipelines/{pipelineId}/cells/{cellId}/runs | Create a new cell run
[**create_pipeline_session**](CloudIDERunApi.md#create_pipeline_session) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/pipelines/{pipelineId}/sessions | Create a new pipeline session
[**get_cell_run**](CloudIDERunApi.md#get_cell_run) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/pipelines/{pipelineId}/cells/{cellId}/runs/{cellRunId} | Get a cell run
[**get_cell_run_task_figures**](CloudIDERunApi.md#get_cell_run_task_figures) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/pipelines/{pipelineId}/cells/{cellId}/runs/{cellRunId}/tasks/{taskId}/figures | Get the figures for a cell run&#39;s task
[**get_cell_run_task_logs**](CloudIDERunApi.md#get_cell_run_task_logs) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/pipelines/{pipelineId}/cells/{cellId}/runs/{cellRunId}/tasks/{taskId}/logs | Get the logs for a cell run&#39;s task
[**get_cell_run_task_results**](CloudIDERunApi.md#get_cell_run_task_results) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/pipelines/{pipelineId}/cells/{cellId}/runs/{cellRunId}/tasks/{taskId}/results | Get the results for a cell run&#39;s task


# **create_cell_run**
> CreateCellRun create_cell_run(organization_id, workspace_id, project_id, pipeline_id, cell_id, data)

Create a new cell run

Create a new cell run

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.create_cell_run import CreateCellRun
from astronomercoreapi.models.create_cell_run_request import CreateCellRunRequest
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
    api_instance = astronomercoreapi.CloudIDERunApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | project ID
    pipeline_id = 'pipeline_id_example' # str | pipeline ID
    cell_id = 'cell_id_example' # str | cell ID
    data = astronomercoreapi.CreateCellRunRequest() # CreateCellRunRequest | request body for creating a new cell run

    try:
        # Create a new cell run
        api_response = api_instance.create_cell_run(organization_id, workspace_id, project_id, pipeline_id, cell_id, data)
        print("The response of CloudIDERunApi->create_cell_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDERunApi->create_cell_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| project ID | 
 **pipeline_id** | **str**| pipeline ID | 
 **cell_id** | **str**| cell ID | 
 **data** | [**CreateCellRunRequest**](CreateCellRunRequest.md)| request body for creating a new cell run | 

### Return type

[**CreateCellRun**](CreateCellRun.md)

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

# **create_pipeline_session**
> CreatePipelineSession create_pipeline_session(organization_id, workspace_id, project_id, pipeline_id)

Create a new pipeline session

Create a new pipeline session

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.create_pipeline_session import CreatePipelineSession
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
    api_instance = astronomercoreapi.CloudIDERunApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | project ID
    pipeline_id = 'pipeline_id_example' # str | pipeline ID

    try:
        # Create a new pipeline session
        api_response = api_instance.create_pipeline_session(organization_id, workspace_id, project_id, pipeline_id)
        print("The response of CloudIDERunApi->create_pipeline_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDERunApi->create_pipeline_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| project ID | 
 **pipeline_id** | **str**| pipeline ID | 

### Return type

[**CreatePipelineSession**](CreatePipelineSession.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cell_run**
> CellRun get_cell_run(organization_id, workspace_id, project_id, pipeline_id, cell_id, cell_run_id)

Get a cell run

Get a cell run

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.cell_run import CellRun
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
    api_instance = astronomercoreapi.CloudIDERunApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | The ID of the project
    pipeline_id = 'pipeline_id_example' # str | The ID of the pipeline
    cell_id = 'cell_id_example' # str | ID of the cell
    cell_run_id = 'cell_run_id_example' # str | ID of the cell run

    try:
        # Get a cell run
        api_response = api_instance.get_cell_run(organization_id, workspace_id, project_id, pipeline_id, cell_id, cell_run_id)
        print("The response of CloudIDERunApi->get_cell_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDERunApi->get_cell_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| The ID of the project | 
 **pipeline_id** | **str**| The ID of the pipeline | 
 **cell_id** | **str**| ID of the cell | 
 **cell_run_id** | **str**| ID of the cell run | 

### Return type

[**CellRun**](CellRun.md)

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

# **get_cell_run_task_figures**
> CellRunTaskFigures get_cell_run_task_figures(organization_id, workspace_id, project_id, pipeline_id, cell_id, cell_run_id, task_id)

Get the figures for a cell run's task

Get the figures for a cell run's task

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.cell_run_task_figures import CellRunTaskFigures
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
    api_instance = astronomercoreapi.CloudIDERunApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | The ID of the project
    pipeline_id = 'pipeline_id_example' # str | The ID of the pipeline
    cell_id = 'cell_id_example' # str | ID of the cell
    cell_run_id = 'cell_run_id_example' # str | ID of the cell run
    task_id = 'task_id_example' # str | ID of the task

    try:
        # Get the figures for a cell run's task
        api_response = api_instance.get_cell_run_task_figures(organization_id, workspace_id, project_id, pipeline_id, cell_id, cell_run_id, task_id)
        print("The response of CloudIDERunApi->get_cell_run_task_figures:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDERunApi->get_cell_run_task_figures: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| The ID of the project | 
 **pipeline_id** | **str**| The ID of the pipeline | 
 **cell_id** | **str**| ID of the cell | 
 **cell_run_id** | **str**| ID of the cell run | 
 **task_id** | **str**| ID of the task | 

### Return type

[**CellRunTaskFigures**](CellRunTaskFigures.md)

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

# **get_cell_run_task_logs**
> CellRunTaskLogs get_cell_run_task_logs(organization_id, workspace_id, project_id, pipeline_id, cell_id, cell_run_id, task_id, var_from=var_from)

Get the logs for a cell run's task

Get the logs for a cell run's task

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.cell_run_task_logs import CellRunTaskLogs
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
    api_instance = astronomercoreapi.CloudIDERunApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | The ID of the project
    pipeline_id = 'pipeline_id_example' # str | The ID of the pipeline
    cell_id = 'cell_id_example' # str | ID of the cell
    cell_run_id = 'cell_run_id_example' # str | ID of the cell run
    task_id = 'task_id_example' # str | ID of the task
    var_from = 56 # int | The line number to start from (optional)

    try:
        # Get the logs for a cell run's task
        api_response = api_instance.get_cell_run_task_logs(organization_id, workspace_id, project_id, pipeline_id, cell_id, cell_run_id, task_id, var_from=var_from)
        print("The response of CloudIDERunApi->get_cell_run_task_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDERunApi->get_cell_run_task_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| The ID of the project | 
 **pipeline_id** | **str**| The ID of the pipeline | 
 **cell_id** | **str**| ID of the cell | 
 **cell_run_id** | **str**| ID of the cell run | 
 **task_id** | **str**| ID of the task | 
 **var_from** | **int**| The line number to start from | [optional] 

### Return type

[**CellRunTaskLogs**](CellRunTaskLogs.md)

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

# **get_cell_run_task_results**
> CellRunTaskResults get_cell_run_task_results(organization_id, workspace_id, project_id, pipeline_id, cell_id, cell_run_id, task_id)

Get the results for a cell run's task

Get the results for a cell run's task

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.cell_run_task_results import CellRunTaskResults
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
    api_instance = astronomercoreapi.CloudIDERunApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | The ID of the project
    pipeline_id = 'pipeline_id_example' # str | The ID of the pipeline
    cell_id = 'cell_id_example' # str | ID of the cell
    cell_run_id = 'cell_run_id_example' # str | ID of the cell run
    task_id = 'task_id_example' # str | ID of the task

    try:
        # Get the results for a cell run's task
        api_response = api_instance.get_cell_run_task_results(organization_id, workspace_id, project_id, pipeline_id, cell_id, cell_run_id, task_id)
        print("The response of CloudIDERunApi->get_cell_run_task_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDERunApi->get_cell_run_task_results: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| The ID of the project | 
 **pipeline_id** | **str**| The ID of the pipeline | 
 **cell_id** | **str**| ID of the cell | 
 **cell_run_id** | **str**| ID of the cell run | 
 **task_id** | **str**| ID of the task | 

### Return type

[**CellRunTaskResults**](CellRunTaskResults.md)

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

