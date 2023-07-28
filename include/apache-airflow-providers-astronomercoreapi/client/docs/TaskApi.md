# astronomercoreapi.TaskApi

All URIs are relative to *https://api.astronomer.io/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_task_instances**](TaskApi.md#clear_task_instances) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/runtimes/{runtimeId}/dags/{dagId}/clear-task-instances | Clear task instances for a dag
[**get_mapped_task_instance**](TaskApi.md#get_mapped_task_instance) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/runtimes/{runtimeId}/dags/{dagId}/runs/{dagRunId}/tasks/{taskId}/mapped-tasks/{mapIndex} | Get details of a mapped task instance
[**list_mapped_task_instances**](TaskApi.md#list_mapped_task_instances) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/runtimes/{runtimeId}/dags/{dagId}/runs/{dagRunId}/tasks/{taskId}/mapped-tasks | List mapped task instances
[**update_task_instance**](TaskApi.md#update_task_instance) | **PATCH** /organizations/{organizationId}/workspaces/{workspaceId}/runtimes/{runtimeId}/dags/{dagId}/runs/{dagRunId}/tasks/{taskId} | Set the state of a task
[**update_task_instances_state**](TaskApi.md#update_task_instances_state) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/runtimes/{runtimeId}/dags/{dagId}/update-task-instances-state | Update task instances state


# **clear_task_instances**
> TaskInstanceReferences clear_task_instances(organization_id, workspace_id, runtime_id, dag_id, data)

Clear task instances for a dag

Clear task instances for a dag

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.clear_task_instances_request import ClearTaskInstancesRequest
from astronomercoreapi.models.task_instance_references import TaskInstanceReferences
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
    api_instance = astronomercoreapi.TaskApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    runtime_id = 'runtime_id_example' # str | ID of the runtime
    dag_id = 'dag_id_example' # str | dag ID
    data = astronomercoreapi.ClearTaskInstancesRequest() # ClearTaskInstancesRequest | request body for clearing a dag run tasks

    try:
        # Clear task instances for a dag
        api_response = api_instance.clear_task_instances(organization_id, workspace_id, runtime_id, dag_id, data)
        print("The response of TaskApi->clear_task_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->clear_task_instances: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **runtime_id** | **str**| ID of the runtime | 
 **dag_id** | **str**| dag ID | 
 **data** | [**ClearTaskInstancesRequest**](ClearTaskInstancesRequest.md)| request body for clearing a dag run tasks | 

### Return type

[**TaskInstanceReferences**](TaskInstanceReferences.md)

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

# **get_mapped_task_instance**
> TaskInstance get_mapped_task_instance(organization_id, workspace_id, runtime_id, dag_id, dag_run_id, task_id, map_index)

Get details of a mapped task instance

Get details of a mapped task instance

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.task_instance import TaskInstance
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
    api_instance = astronomercoreapi.TaskApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    runtime_id = 'runtime_id_example' # str | ID of the runtime
    dag_id = 'dag_id_example' # str | dag ID
    dag_run_id = 'dag_run_id_example' # str | dag run ID
    task_id = 'task_id_example' # str | task ID
    map_index = 'map_index_example' # str | task map index

    try:
        # Get details of a mapped task instance
        api_response = api_instance.get_mapped_task_instance(organization_id, workspace_id, runtime_id, dag_id, dag_run_id, task_id, map_index)
        print("The response of TaskApi->get_mapped_task_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->get_mapped_task_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **runtime_id** | **str**| ID of the runtime | 
 **dag_id** | **str**| dag ID | 
 **dag_run_id** | **str**| dag run ID | 
 **task_id** | **str**| task ID | 
 **map_index** | **str**| task map index | 

### Return type

[**TaskInstance**](TaskInstance.md)

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

# **list_mapped_task_instances**
> TaskInstancesPaginated list_mapped_task_instances(organization_id, task_id, workspace_id, runtime_id, dag_id, dag_run_id, offset=offset, limit=limit, execution_date_gte=execution_date_gte, execution_date_lte=execution_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte, duration_gte=duration_gte, duration_lte=duration_lte, states=states, pools=pools, queues=queues, order_by=order_by)

List mapped task instances

List mapped task instances

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
    api_instance = astronomercoreapi.TaskApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    task_id = 'task_id_example' # str | ID of the task
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
    duration_gte = 3.4 # float | duration is greater than or equal to the specified in seconds (optional)
    duration_lte = 3.4 # float | duration is less than or equal to the specified in seconds (optional)
    states = ['states_example'] # List[str] | task states (optional)
    pools = ['pools_example'] # List[str] | task pools (optional)
    queues = ['queues_example'] # List[str] | task queues (optional)
    order_by = 'order_by_example' # str | The name of the field to order the results by. Prefix a field name with - to reverse the sort order. (optional)

    try:
        # List mapped task instances
        api_response = api_instance.list_mapped_task_instances(organization_id, task_id, workspace_id, runtime_id, dag_id, dag_run_id, offset=offset, limit=limit, execution_date_gte=execution_date_gte, execution_date_lte=execution_date_lte, start_date_gte=start_date_gte, start_date_lte=start_date_lte, end_date_gte=end_date_gte, end_date_lte=end_date_lte, duration_gte=duration_gte, duration_lte=duration_lte, states=states, pools=pools, queues=queues, order_by=order_by)
        print("The response of TaskApi->list_mapped_task_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->list_mapped_task_instances: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **task_id** | **str**| ID of the task | 
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
 **duration_gte** | **float**| duration is greater than or equal to the specified in seconds | [optional] 
 **duration_lte** | **float**| duration is less than or equal to the specified in seconds | [optional] 
 **states** | [**List[str]**](str.md)| task states | [optional] 
 **pools** | [**List[str]**](str.md)| task pools | [optional] 
 **queues** | [**List[str]**](str.md)| task queues | [optional] 
 **order_by** | **str**| The name of the field to order the results by. Prefix a field name with - to reverse the sort order. | [optional] 

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

# **update_task_instance**
> TaskInstanceReference update_task_instance(organization_id, workspace_id, runtime_id, dag_id, dag_run_id, task_id, data)

Set the state of a task

Set the state of a task

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.task_instance_reference import TaskInstanceReference
from astronomercoreapi.models.update_task_instance_request import UpdateTaskInstanceRequest
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
    api_instance = astronomercoreapi.TaskApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    runtime_id = 'runtime_id_example' # str | ID of the runtime
    dag_id = 'dag_id_example' # str | dag ID
    dag_run_id = 'dag_run_id_example' # str | dag run ID
    task_id = 'task_id_example' # str | task ID
    data = astronomercoreapi.UpdateTaskInstanceRequest() # UpdateTaskInstanceRequest | request body for updating a task

    try:
        # Set the state of a task
        api_response = api_instance.update_task_instance(organization_id, workspace_id, runtime_id, dag_id, dag_run_id, task_id, data)
        print("The response of TaskApi->update_task_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->update_task_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **runtime_id** | **str**| ID of the runtime | 
 **dag_id** | **str**| dag ID | 
 **dag_run_id** | **str**| dag run ID | 
 **task_id** | **str**| task ID | 
 **data** | [**UpdateTaskInstanceRequest**](UpdateTaskInstanceRequest.md)| request body for updating a task | 

### Return type

[**TaskInstanceReference**](TaskInstanceReference.md)

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

# **update_task_instances_state**
> TaskInstanceReferences update_task_instances_state(organization_id, workspace_id, runtime_id, dag_id, data)

Update task instances state

Update task instances state

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.task_instance_references import TaskInstanceReferences
from astronomercoreapi.models.update_task_instances_state_request import UpdateTaskInstancesStateRequest
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
    api_instance = astronomercoreapi.TaskApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    runtime_id = 'runtime_id_example' # str | ID of the runtime
    dag_id = 'dag_id_example' # str | dag ID
    data = astronomercoreapi.UpdateTaskInstancesStateRequest() # UpdateTaskInstancesStateRequest | request body for clearing a dag run tasks

    try:
        # Update task instances state
        api_response = api_instance.update_task_instances_state(organization_id, workspace_id, runtime_id, dag_id, data)
        print("The response of TaskApi->update_task_instances_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->update_task_instances_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **runtime_id** | **str**| ID of the runtime | 
 **dag_id** | **str**| dag ID | 
 **data** | [**UpdateTaskInstancesStateRequest**](UpdateTaskInstancesStateRequest.md)| request body for clearing a dag run tasks | 

### Return type

[**TaskInstanceReferences**](TaskInstanceReferences.md)

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

