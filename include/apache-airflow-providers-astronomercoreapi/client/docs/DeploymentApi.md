# astronomercoreapi.DeploymentApi

All URIs are relative to *https://api.astronomer.io/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_deployment**](DeploymentApi.md#create_deployment) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/deployments | Create deployment
[**get_deployment_dag_runs**](DeploymentApi.md#get_deployment_dag_runs) | **GET** /organizations/{organizationId}/deployments/{deploymentId}/dags/{dagId}/runs | Get dags runs
[**get_deployment_dag_structure**](DeploymentApi.md#get_deployment_dag_structure) | **GET** /organizations/{organizationId}/deployments/{deploymentId}/dags/{dagId}/structure | Get dags structure
[**get_deployment_health**](DeploymentApi.md#get_deployment_health) | **GET** /organizations/{organizationId}/deployments/{deploymentId}/health | Get deployment health
[**get_deployment_logs**](DeploymentApi.md#get_deployment_logs) | **GET** /organizations/{organizationId}/deployments/{deploymentId}/logs | Get deployment Logs
[**list_deployments**](DeploymentApi.md#list_deployments) | **GET** /organizations/{organizationId}/deployments | List deployments
[**update_deployment**](DeploymentApi.md#update_deployment) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/deployments/{deploymentId} | EXPERIMENTAL - Transfer deployment across workspaces


# **create_deployment**
> Deployment create_deployment(organization_id, workspace_id, body)

Create deployment

Create deployment

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.create_deployment_request import CreateDeploymentRequest
from astronomercoreapi.models.deployment import Deployment
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
    api_instance = astronomercoreapi.DeploymentApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    body = astronomercoreapi.CreateDeploymentRequest() # CreateDeploymentRequest | request body for create a deployment

    try:
        # Create deployment
        api_response = api_instance.create_deployment(organization_id, workspace_id, body)
        print("The response of DeploymentApi->create_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentApi->create_deployment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **body** | [**CreateDeploymentRequest**](CreateDeploymentRequest.md)| request body for create a deployment | 

### Return type

[**Deployment**](Deployment.md)

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

# **get_deployment_dag_runs**
> InternalPaginationResultDagRunWithTaskInstances get_deployment_dag_runs(organization_id, deployment_id, dag_id, page_size=page_size, cursor=cursor, run_id=run_id, logical_date__lt=logical_date__lt, logical_date__gt=logical_date__gt, start_date__lt=start_date__lt, start_date__gt=start_date__gt, end_date__lt=end_date__lt, end_date__gt=end_date__gt, state=state, run_type__in=run_type__in)

Get dags runs

Get paginated dags runs

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.internal_pagination_result_dag_run_with_task_instances import InternalPaginationResultDagRunWithTaskInstances
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
    api_instance = astronomercoreapi.DeploymentApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    deployment_id = 'deployment_id_example' # str | deployment ID to query for dags structure
    dag_id = 'dag_id_example' # str | dagId of the dags
    page_size = 56 # int | page size, default of 20 (optional)
    cursor = 'cursor_example' # str | pagination cursor (optional)
    run_id = 'run_id_example' # str | filter by ID of the dags run (optional)
    logical_date__lt = '2013-10-20T19:20:30+01:00' # datetime | filter by logical date (aka execution date)  of  the  dags  run  less     than  (RFC3339 format) (optional)
    logical_date__gt = '2013-10-20T19:20:30+01:00' # datetime | filter by logical date (aka execution date)  of  the  dags  run  greater  than  (RFC3339 format) (optional)
    start_date__lt = '2013-10-20T19:20:30+01:00' # datetime | filter by start date of the dags run less than (RFC3339 format) (optional)
    start_date__gt = '2013-10-20T19:20:30+01:00' # datetime | filter by start date of the dags run greater than (RFC3339 format) (optional)
    end_date__lt = '2013-10-20T19:20:30+01:00' # datetime | filter by end date of the dags run less than (RFC3339 format) (optional)
    end_date__gt = '2013-10-20T19:20:30+01:00' # datetime | filter by end date of the dags run greater than (RFC3339 format) (optional)
    state = ['state_example'] # List[str] | filter by dags runs with any of these run states (optional)
    run_type__in = ['run_type__in_example'] # List[str] | filter by dags runs with any of these run types (optional)

    try:
        # Get dags runs
        api_response = api_instance.get_deployment_dag_runs(organization_id, deployment_id, dag_id, page_size=page_size, cursor=cursor, run_id=run_id, logical_date__lt=logical_date__lt, logical_date__gt=logical_date__gt, start_date__lt=start_date__lt, start_date__gt=start_date__gt, end_date__lt=end_date__lt, end_date__gt=end_date__gt, state=state, run_type__in=run_type__in)
        print("The response of DeploymentApi->get_deployment_dag_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentApi->get_deployment_dag_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **deployment_id** | **str**| deployment ID to query for dags structure | 
 **dag_id** | **str**| dagId of the dags | 
 **page_size** | **int**| page size, default of 20 | [optional] 
 **cursor** | **str**| pagination cursor | [optional] 
 **run_id** | **str**| filter by ID of the dags run | [optional] 
 **logical_date__lt** | **datetime**| filter by logical date (aka execution date)  of  the  dags  run  less     than  (RFC3339 format) | [optional] 
 **logical_date__gt** | **datetime**| filter by logical date (aka execution date)  of  the  dags  run  greater  than  (RFC3339 format) | [optional] 
 **start_date__lt** | **datetime**| filter by start date of the dags run less than (RFC3339 format) | [optional] 
 **start_date__gt** | **datetime**| filter by start date of the dags run greater than (RFC3339 format) | [optional] 
 **end_date__lt** | **datetime**| filter by end date of the dags run less than (RFC3339 format) | [optional] 
 **end_date__gt** | **datetime**| filter by end date of the dags run greater than (RFC3339 format) | [optional] 
 **state** | [**List[str]**](str.md)| filter by dags runs with any of these run states | [optional] 
 **run_type__in** | [**List[str]**](str.md)| filter by dags runs with any of these run types | [optional] 

### Return type

[**InternalPaginationResultDagRunWithTaskInstances**](InternalPaginationResultDagRunWithTaskInstances.md)

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

# **get_deployment_dag_structure**
> InternalDagStructure get_deployment_dag_structure(organization_id, deployment_id, dag_id)

Get dags structure

Get the graph structure of a dag's tasks and task groups

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.internal_dag_structure import InternalDagStructure
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
    api_instance = astronomercoreapi.DeploymentApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    deployment_id = 'deployment_id_example' # str | deployment ID to query for dag structure
    dag_id = 'dag_id_example' # str | dagId of the dag

    try:
        # Get dags structure
        api_response = api_instance.get_deployment_dag_structure(organization_id, deployment_id, dag_id)
        print("The response of DeploymentApi->get_deployment_dag_structure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentApi->get_deployment_dag_structure: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **deployment_id** | **str**| deployment ID to query for dag structure | 
 **dag_id** | **str**| dagId of the dag | 

### Return type

[**InternalDagStructure**](InternalDagStructure.md)

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

# **get_deployment_health**
> Dict[str, object] get_deployment_health(organization_id, deployment_id)

Get deployment health

Get deployment health report

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
    api_instance = astronomercoreapi.DeploymentApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    deployment_id = 'deployment_id_example' # str | deployment ID for which to return health information

    try:
        # Get deployment health
        api_response = api_instance.get_deployment_health(organization_id, deployment_id)
        print("The response of DeploymentApi->get_deployment_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentApi->get_deployment_health: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **deployment_id** | **str**| deployment ID for which to return health information | 

### Return type

**Dict[str, object]**

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

# **get_deployment_logs**
> DeploymentLog get_deployment_logs(organization_id, deployment_id, sources, limit=limit, offset=offset, range=range, max_num_results=max_num_results, search_id=search_id, search_text=search_text)

Get deployment Logs

Get deployment Logs

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.deployment_log import DeploymentLog
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
    api_instance = astronomercoreapi.DeploymentApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    deployment_id = 'deployment_id_example' # str | deployment ID to get logs from
    sources = ['sources_example'] # List[str] | log sources to select logs from
    limit = 500 # int | limit of the count of the logs (optional) (default to 500)
    offset = 0 # int | offset of the log entries (optional) (default to 0)
    range = 3600 # int | range of the log search in seconds (optional) (default to 3600)
    max_num_results = 10000 # int | maximum number of results across all pages (optional) (default to 10000)
    search_id = 'search_id_example' # str | searchId to get logs from (optional)
    search_text = 'search_text_example' # str | an exact text search param used to filter the data on (optional)

    try:
        # Get deployment Logs
        api_response = api_instance.get_deployment_logs(organization_id, deployment_id, sources, limit=limit, offset=offset, range=range, max_num_results=max_num_results, search_id=search_id, search_text=search_text)
        print("The response of DeploymentApi->get_deployment_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentApi->get_deployment_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **deployment_id** | **str**| deployment ID to get logs from | 
 **sources** | [**List[str]**](str.md)| log sources to select logs from | 
 **limit** | **int**| limit of the count of the logs | [optional] [default to 500]
 **offset** | **int**| offset of the log entries | [optional] [default to 0]
 **range** | **int**| range of the log search in seconds | [optional] [default to 3600]
 **max_num_results** | **int**| maximum number of results across all pages | [optional] [default to 10000]
 **search_id** | **str**| searchId to get logs from | [optional] 
 **search_text** | **str**| an exact text search param used to filter the data on | [optional] 

### Return type

[**DeploymentLog**](DeploymentLog.md)

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

# **list_deployments**
> DeploymentsPaginated list_deployments(organization_id, deployment_ids=deployment_ids, workspace_ids=workspace_ids, offset=offset, limit=limit, sorts=sorts)

List deployments

List deployments

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.deployments_paginated import DeploymentsPaginated
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
    api_instance = astronomercoreapi.DeploymentApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    deployment_ids = ['deployment_ids_example'] # List[str] | IDs that define the deployments (optional)
    workspace_ids = ['workspace_ids_example'] # List[str] | IDs that define the workspaces where deployments belong to (optional)
    offset = 0 # int | offset for pagination (optional) (default to 0)
    limit = 20 # int | limit for pagination (optional) (default to 20)
    sorts = ['sorts_example'] # List[str] | sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc' (optional)

    try:
        # List deployments
        api_response = api_instance.list_deployments(organization_id, deployment_ids=deployment_ids, workspace_ids=workspace_ids, offset=offset, limit=limit, sorts=sorts)
        print("The response of DeploymentApi->list_deployments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentApi->list_deployments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **deployment_ids** | [**List[str]**](str.md)| IDs that define the deployments | [optional] 
 **workspace_ids** | [**List[str]**](str.md)| IDs that define the workspaces where deployments belong to | [optional] 
 **offset** | **int**| offset for pagination | [optional] [default to 0]
 **limit** | **int**| limit for pagination | [optional] [default to 20]
 **sorts** | [**List[str]**](str.md)| sorting criteria, each criterion should conform to format &#39;fieldName:asc&#39; or &#39;fieldName:desc&#39; | [optional] 

### Return type

[**DeploymentsPaginated**](DeploymentsPaginated.md)

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

# **update_deployment**
> Deployment update_deployment(organization_id, workspace_id, deployment_id, body)

EXPERIMENTAL - Transfer deployment across workspaces

EXPERIMENTAL: update deployment is only used to transfer deployments

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.deployment import Deployment
from astronomercoreapi.models.update_deployment_request import UpdateDeploymentRequest
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
    api_instance = astronomercoreapi.DeploymentApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    deployment_id = 'deployment_id_example' # str | ID of the deployment
    body = astronomercoreapi.UpdateDeploymentRequest() # UpdateDeploymentRequest | request body for updating a deployment

    try:
        # EXPERIMENTAL - Transfer deployment across workspaces
        api_response = api_instance.update_deployment(organization_id, workspace_id, deployment_id, body)
        print("The response of DeploymentApi->update_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentApi->update_deployment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **deployment_id** | **str**| ID of the deployment | 
 **body** | [**UpdateDeploymentRequest**](UpdateDeploymentRequest.md)| request body for updating a deployment | 

### Return type

[**Deployment**](Deployment.md)

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

