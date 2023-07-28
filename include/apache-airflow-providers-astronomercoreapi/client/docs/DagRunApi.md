# astronomercoreapi.DagRunApi

All URIs are relative to *https://api.astronomer.io/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_dag_run**](DagRunApi.md#clear_dag_run) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/runtimes/{runtimeId}/dags/{dagId}/runs/{dagRunId}/clear | Clear a dag run
[**update_dag_run**](DagRunApi.md#update_dag_run) | **PATCH** /organizations/{organizationId}/workspaces/{workspaceId}/runtimes/{runtimeId}/dags/{dagId}/runs/{dagRunId} | Set the state of a dag run


# **clear_dag_run**
> ClearDagRun clear_dag_run(organization_id, workspace_id, runtime_id, dag_id, dag_run_id, data)

Clear a dag run

Clear a dag run

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.clear_dag_run import ClearDagRun
from astronomercoreapi.models.clear_dag_run_request import ClearDagRunRequest
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
    api_instance = astronomercoreapi.DagRunApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    runtime_id = 'runtime_id_example' # str | ID of the runtime
    dag_id = 'dag_id_example' # str | dag ID
    dag_run_id = 'dag_run_id_example' # str | dag run ID
    data = astronomercoreapi.ClearDagRunRequest() # ClearDagRunRequest | request body for clearing a dag run

    try:
        # Clear a dag run
        api_response = api_instance.clear_dag_run(organization_id, workspace_id, runtime_id, dag_id, dag_run_id, data)
        print("The response of DagRunApi->clear_dag_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DagRunApi->clear_dag_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **runtime_id** | **str**| ID of the runtime | 
 **dag_id** | **str**| dag ID | 
 **dag_run_id** | **str**| dag run ID | 
 **data** | [**ClearDagRunRequest**](ClearDagRunRequest.md)| request body for clearing a dag run | 

### Return type

[**ClearDagRun**](ClearDagRun.md)

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

# **update_dag_run**
> DagRun update_dag_run(organization_id, workspace_id, runtime_id, dag_id, dag_run_id, data)

Set the state of a dag run

Set the state of a dag run

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.dag_run import DagRun
from astronomercoreapi.models.update_dag_run_request import UpdateDagRunRequest
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
    api_instance = astronomercoreapi.DagRunApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    runtime_id = 'runtime_id_example' # str | ID of the runtime
    dag_id = 'dag_id_example' # str | dag ID
    dag_run_id = 'dag_run_id_example' # str | dag run ID
    data = astronomercoreapi.UpdateDagRunRequest() # UpdateDagRunRequest | request body for updating a dag run

    try:
        # Set the state of a dag run
        api_response = api_instance.update_dag_run(organization_id, workspace_id, runtime_id, dag_id, dag_run_id, data)
        print("The response of DagRunApi->update_dag_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DagRunApi->update_dag_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **runtime_id** | **str**| ID of the runtime | 
 **dag_id** | **str**| dag ID | 
 **dag_run_id** | **str**| dag run ID | 
 **data** | [**UpdateDagRunRequest**](UpdateDagRunRequest.md)| request body for updating a dag run | 

### Return type

[**DagRun**](DagRun.md)

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

