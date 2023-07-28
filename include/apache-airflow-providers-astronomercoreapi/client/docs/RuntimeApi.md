# astronomercoreapi.RuntimeApi

All URIs are relative to *https://api.astronomer.io/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dag_run**](RuntimeApi.md#create_dag_run) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/runtimes/{runtimeId}/dags/{dagId}/runs | Create a dag run
[**get_dag_code**](RuntimeApi.md#get_dag_code) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/runtimes/{runtimeId}/code/{fileToken} | Get code for a dag
[**get_runtime**](RuntimeApi.md#get_runtime) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/runtimes/{runtimeId} | Get runtime
[**get_runtime_dag**](RuntimeApi.md#get_runtime_dag) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/runtimes/{runtimeId}/dags/{dagId} | Get a dag in a runtime by name
[**get_task_instance_logs**](RuntimeApi.md#get_task_instance_logs) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/runtimes/{runtimeId}/dags/{dagId}/runs/{dagRunId}/task-instances/{dagTaskId}/logs/{dagTaskTryNumber} | Get task instances logs for dag run in a runtime
[**list_dag_runs**](RuntimeApi.md#list_dag_runs) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/runtimes/{runtimeId}/dags/{dagId}/runs | List dag runs for a dag in a runtime
[**list_runtime_dags**](RuntimeApi.md#list_runtime_dags) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/runtimes/{runtimeId}/dags | List all dags in a runtime
[**list_runtime_import_errors**](RuntimeApi.md#list_runtime_import_errors) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/runtimes/{runtimeId}/import-errors | List all import errors in a runtime
[**list_runtimes**](RuntimeApi.md#list_runtimes) | **GET** /organizations/{organizationId}/runtimes | List runtimes in a workspace
[**list_task_instances**](RuntimeApi.md#list_task_instances) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/runtimes/{runtimeId}/dags/{dagId}/runs/{dagRunId}/task-instances | List task instances for dag run in a runtime
[**update_runtime_dag**](RuntimeApi.md#update_runtime_dag) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/runtimes/{runtimeId}/dags/{dagId} | Update a dag


# **create_dag_run**
> CreateDagRun create_dag_run(organization_id, workspace_id, runtime_id, dag_id, data)

Create a dag run

Create a dag run

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.create_dag_run import CreateDagRun
from astronomercoreapi.models.create_dag_run_request import CreateDagRunRequest
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
    api_instance = astronomercoreapi.RuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    runtime_id = 'runtime_id_example' # str | ID of the runtime
    dag_id = 'dag_id_example' # str | ID of the dag
    data = astronomercoreapi.CreateDagRunRequest() # CreateDagRunRequest | request body for creating a dag run

    try:
        # Create a dag run
        api_response = api_instance.create_dag_run(organization_id, workspace_id, runtime_id, dag_id, data)
        print("The response of RuntimeApi->create_dag_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimeApi->create_dag_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **runtime_id** | **str**| ID of the runtime | 
 **dag_id** | **str**| ID of the dag | 
 **data** | [**CreateDagRunRequest**](CreateDagRunRequest.md)| request body for creating a dag run | 

### Return type

[**CreateDagRun**](CreateDagRun.md)

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

# **get_dag_code**
> Code get_dag_code(organization_id, workspace_id, runtime_id, file_token)

Get code for a dag

Get code for a dag

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.code import Code
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
    api_instance = astronomercoreapi.RuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    runtime_id = 'runtime_id_example' # str | ID of the runtime
    file_token = 'file_token_example' # str | Token for the code file

    try:
        # Get code for a dag
        api_response = api_instance.get_dag_code(organization_id, workspace_id, runtime_id, file_token)
        print("The response of RuntimeApi->get_dag_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimeApi->get_dag_code: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **runtime_id** | **str**| ID of the runtime | 
 **file_token** | **str**| Token for the code file | 

### Return type

[**Code**](Code.md)

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

# **get_runtime**
> Runtime get_runtime(organization_id, workspace_id, runtime_id)

Get runtime

Get runtime

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.runtime import Runtime
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
    api_instance = astronomercoreapi.RuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    runtime_id = 'runtime_id_example' # str | ID of the runtime

    try:
        # Get runtime
        api_response = api_instance.get_runtime(organization_id, workspace_id, runtime_id)
        print("The response of RuntimeApi->get_runtime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimeApi->get_runtime: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **runtime_id** | **str**| ID of the runtime | 

### Return type

[**Runtime**](Runtime.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runtime_dag**
> RuntimeDag get_runtime_dag(organization_id, dag_id, workspace_id, runtime_id)

Get a dag in a runtime by name

Get a dag in a runtime by name

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.runtime_dag import RuntimeDag
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
    api_instance = astronomercoreapi.RuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    dag_id = 'dag_id_example' # str | dag ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    runtime_id = 'runtime_id_example' # str | ID of the runtime

    try:
        # Get a dag in a runtime by name
        api_response = api_instance.get_runtime_dag(organization_id, dag_id, workspace_id, runtime_id)
        print("The response of RuntimeApi->get_runtime_dag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimeApi->get_runtime_dag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **dag_id** | **str**| dag ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **runtime_id** | **str**| ID of the runtime | 

### Return type

[**RuntimeDag**](RuntimeDag.md)

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

# **get_task_instance_logs**
> TaskInstanceLogs get_task_instance_logs(organization_id, workspace_id, runtime_id, dag_id, dag_run_id, dag_task_id, dag_task_try_number, full_content=full_content, map_index=map_index, token=token)

Get task instances logs for dag run in a runtime

Get task instances logs for dag run in a runtime

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.task_instance_logs import TaskInstanceLogs
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
    api_instance = astronomercoreapi.RuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    runtime_id = 'runtime_id_example' # str | ID of the runtime
    dag_id = 'dag_id_example' # str | ID of the dag
    dag_run_id = 'dag_run_id_example' # str | ID of the dag run
    dag_task_id = 'dag_task_id_example' # str | ID of the dag run task
    dag_task_try_number = 56 # int | ID of the dag run task try number
    full_content = True # bool | task log full content (optional)
    map_index = 56 # int | task map index for mapped task (optional)
    token = 'token_example' # str | token that allows you to continue fetching logs (optional)

    try:
        # Get task instances logs for dag run in a runtime
        api_response = api_instance.get_task_instance_logs(organization_id, workspace_id, runtime_id, dag_id, dag_run_id, dag_task_id, dag_task_try_number, full_content=full_content, map_index=map_index, token=token)
        print("The response of RuntimeApi->get_task_instance_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimeApi->get_task_instance_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **runtime_id** | **str**| ID of the runtime | 
 **dag_id** | **str**| ID of the dag | 
 **dag_run_id** | **str**| ID of the dag run | 
 **dag_task_id** | **str**| ID of the dag run task | 
 **dag_task_try_number** | **int**| ID of the dag run task try number | 
 **full_content** | **bool**| task log full content | [optional] 
 **map_index** | **int**| task map index for mapped task | [optional] 
 **token** | **str**| token that allows you to continue fetching logs | [optional] 

### Return type

[**TaskInstanceLogs**](TaskInstanceLogs.md)

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

# **list_dag_runs**
> DagRunsPaginated list_dag_runs(organization_id, workspace_id, runtime_id, dag_id, offset=offset, limit=limit, order_by=order_by, state=state, execution_date_gte=execution_date_gte, execution_date_lte=execution_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte)

List dag runs for a dag in a runtime

List dag runs for a dag in a runtime

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.dag_runs_paginated import DagRunsPaginated
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
    api_instance = astronomercoreapi.RuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    runtime_id = 'runtime_id_example' # str | ID of the runtime
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
        # List dag runs for a dag in a runtime
        api_response = api_instance.list_dag_runs(organization_id, workspace_id, runtime_id, dag_id, offset=offset, limit=limit, order_by=order_by, state=state, execution_date_gte=execution_date_gte, execution_date_lte=execution_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte)
        print("The response of RuntimeApi->list_dag_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimeApi->list_dag_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **runtime_id** | **str**| ID of the runtime | 
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

[**DagRunsPaginated**](DagRunsPaginated.md)

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

# **list_runtime_dags**
> RuntimeDagsPaginated list_runtime_dags(organization_id, workspace_id, runtime_id, offset=offset, limit=limit, order_by=order_by, tags=tags, only_active=only_active, dag_id_pattern=dag_id_pattern)

List all dags in a runtime

List all dags in a runtime

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.runtime_dags_paginated import RuntimeDagsPaginated
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
    api_instance = astronomercoreapi.RuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    runtime_id = 'runtime_id_example' # str | ID of the runtime
    offset = 0 # int | offset for pagination (optional) (default to 0)
    limit = 20 # int | limit for pagination (optional) (default to 20)
    order_by = 'order_by_example' # str | order dags by the field name (optional)
    tags = 'tags_example' # str | tags (optional)
    only_active = True # bool | show only active dags (optional)
    dag_id_pattern = 'dag_id_pattern_example' # str | show dags that match this pattern (optional)

    try:
        # List all dags in a runtime
        api_response = api_instance.list_runtime_dags(organization_id, workspace_id, runtime_id, offset=offset, limit=limit, order_by=order_by, tags=tags, only_active=only_active, dag_id_pattern=dag_id_pattern)
        print("The response of RuntimeApi->list_runtime_dags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimeApi->list_runtime_dags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **runtime_id** | **str**| ID of the runtime | 
 **offset** | **int**| offset for pagination | [optional] [default to 0]
 **limit** | **int**| limit for pagination | [optional] [default to 20]
 **order_by** | **str**| order dags by the field name | [optional] 
 **tags** | **str**| tags | [optional] 
 **only_active** | **bool**| show only active dags | [optional] 
 **dag_id_pattern** | **str**| show dags that match this pattern | [optional] 

### Return type

[**RuntimeDagsPaginated**](RuntimeDagsPaginated.md)

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

# **list_runtime_import_errors**
> RuntimeImportErrorsPaginated list_runtime_import_errors(organization_id, workspace_id, runtime_id, offset=offset, limit=limit, order_by=order_by)

List all import errors in a runtime

List all import errors in a runtime

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.runtime_import_errors_paginated import RuntimeImportErrorsPaginated
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
    api_instance = astronomercoreapi.RuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    runtime_id = 'runtime_id_example' # str | ID of the runtime
    offset = 0 # int | offset for pagination (optional) (default to 0)
    limit = 20 # int | limit for pagination (optional) (default to 20)
    order_by = 'order_by_example' # str | order list by the field name (optional)

    try:
        # List all import errors in a runtime
        api_response = api_instance.list_runtime_import_errors(organization_id, workspace_id, runtime_id, offset=offset, limit=limit, order_by=order_by)
        print("The response of RuntimeApi->list_runtime_import_errors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimeApi->list_runtime_import_errors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **runtime_id** | **str**| ID of the runtime | 
 **offset** | **int**| offset for pagination | [optional] [default to 0]
 **limit** | **int**| limit for pagination | [optional] [default to 20]
 **order_by** | **str**| order list by the field name | [optional] 

### Return type

[**RuntimeImportErrorsPaginated**](RuntimeImportErrorsPaginated.md)

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

# **list_runtimes**
> RuntimesPaginated list_runtimes(organization_id, workspace_ids=workspace_ids, runtime_type=runtime_type, offset=offset, limit=limit, release_names=release_names, sorts=sorts)

List runtimes in a workspace

List runtimes in a workspace

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.runtimes_paginated import RuntimesPaginated
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
    api_instance = astronomercoreapi.RuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_ids = ['workspace_ids_example'] # List[str] | IDs that define the workspaces where runtimes belong to (optional)
    runtime_type = 'runtime_type_example' # str | runtimeType to filter runtimes with (optional)
    offset = 0 # int | offset for pagination (optional) (default to 0)
    limit = 20 # int | limit for pagination (optional) (default to 20)
    release_names = 'release_names_example' # str | release names to filter runtimes with, separated by comma (optional)
    sorts = ['sorts_example'] # List[str] | sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc' (optional)

    try:
        # List runtimes in a workspace
        api_response = api_instance.list_runtimes(organization_id, workspace_ids=workspace_ids, runtime_type=runtime_type, offset=offset, limit=limit, release_names=release_names, sorts=sorts)
        print("The response of RuntimeApi->list_runtimes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimeApi->list_runtimes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_ids** | [**List[str]**](str.md)| IDs that define the workspaces where runtimes belong to | [optional] 
 **runtime_type** | **str**| runtimeType to filter runtimes with | [optional] 
 **offset** | **int**| offset for pagination | [optional] [default to 0]
 **limit** | **int**| limit for pagination | [optional] [default to 20]
 **release_names** | **str**| release names to filter runtimes with, separated by comma | [optional] 
 **sorts** | [**List[str]**](str.md)| sorting criteria, each criterion should conform to format &#39;fieldName:asc&#39; or &#39;fieldName:desc&#39; | [optional] 

### Return type

[**RuntimesPaginated**](RuntimesPaginated.md)

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

# **list_task_instances**
> TaskInstancesPaginated list_task_instances(organization_id, workspace_id, runtime_id, dag_id, dag_run_id, offset=offset, limit=limit, execution_date_gte=execution_date_gte, execution_date_lte=execution_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte, duration_sec_gte=duration_sec_gte, duration_sec_lte=duration_sec_lte, states=states, pools=pools, queues=queues)

List task instances for dag run in a runtime

List task instances for dag run in a runtime

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.task_instances_paginated import TaskInstancesPaginated
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
    api_instance = astronomercoreapi.RuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    runtime_id = 'runtime_id_example' # str | ID of the runtime
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
        # List task instances for dag run in a runtime
        api_response = api_instance.list_task_instances(organization_id, workspace_id, runtime_id, dag_id, dag_run_id, offset=offset, limit=limit, execution_date_gte=execution_date_gte, execution_date_lte=execution_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte, duration_sec_gte=duration_sec_gte, duration_sec_lte=duration_sec_lte, states=states, pools=pools, queues=queues)
        print("The response of RuntimeApi->list_task_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimeApi->list_task_instances: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **runtime_id** | **str**| ID of the runtime | 
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

[**TaskInstancesPaginated**](TaskInstancesPaginated.md)

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

# **update_runtime_dag**
> UpdateRuntimeDag update_runtime_dag(organization_id, workspace_id, runtime_id, dag_id, data)

Update a dag

Update a dag

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.update_runtime_dag import UpdateRuntimeDag
from astronomercoreapi.models.update_runtime_dag_request import UpdateRuntimeDagRequest
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
    api_instance = astronomercoreapi.RuntimeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    runtime_id = 'runtime_id_example' # str | ID of the runtime
    dag_id = 'dag_id_example' # str | ID of the dag
    data = astronomercoreapi.UpdateRuntimeDagRequest() # UpdateRuntimeDagRequest | request body for updating a dag

    try:
        # Update a dag
        api_response = api_instance.update_runtime_dag(organization_id, workspace_id, runtime_id, dag_id, data)
        print("The response of RuntimeApi->update_runtime_dag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimeApi->update_runtime_dag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **runtime_id** | **str**| ID of the runtime | 
 **dag_id** | **str**| ID of the dag | 
 **data** | [**UpdateRuntimeDagRequest**](UpdateRuntimeDagRequest.md)| request body for updating a dag | 

### Return type

[**UpdateRuntimeDag**](UpdateRuntimeDag.md)

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

