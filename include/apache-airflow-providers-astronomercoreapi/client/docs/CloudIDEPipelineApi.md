# astronomercoreapi.CloudIDEPipelineApi

All URIs are relative to *https://api.astronomer.io/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pipeline**](CloudIDEPipelineApi.md#create_pipeline) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/pipelines | Create a new pipeline
[**delete_pipeline**](CloudIDEPipelineApi.md#delete_pipeline) | **DELETE** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/pipelines/{pipelineId} | Delete a pipeline
[**get_pipeline**](CloudIDEPipelineApi.md#get_pipeline) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/pipelines/{pipelineId} | Get a pipeline
[**list_pipelines**](CloudIDEPipelineApi.md#list_pipelines) | **GET** /organizations/{organizationId}/pipelines | List pipelines
[**update_pipeline**](CloudIDEPipelineApi.md#update_pipeline) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/pipelines/{pipelineId} | Update a pipeline


# **create_pipeline**
> CreatePipeline create_pipeline(organization_id, workspace_id, project_id, data)

Create a new pipeline

Create a new pipeline

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.create_pipeline import CreatePipeline
from astronomercoreapi.models.create_pipeline_request import CreatePipelineRequest
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
    api_instance = astronomercoreapi.CloudIDEPipelineApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | project ID
    data = astronomercoreapi.CreatePipelineRequest() # CreatePipelineRequest | request body for creating a new pipeline

    try:
        # Create a new pipeline
        api_response = api_instance.create_pipeline(organization_id, workspace_id, project_id, data)
        print("The response of CloudIDEPipelineApi->create_pipeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDEPipelineApi->create_pipeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| project ID | 
 **data** | [**CreatePipelineRequest**](CreatePipelineRequest.md)| request body for creating a new pipeline | 

### Return type

[**CreatePipeline**](CreatePipeline.md)

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

# **delete_pipeline**
> delete_pipeline(organization_id, workspace_id, project_id, pipeline_id)

Delete a pipeline

Delete a pipeline

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
    api_instance = astronomercoreapi.CloudIDEPipelineApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    project_id = 'project_id_example' # str | The ID of the project
    pipeline_id = 'pipeline_id_example' # str | ID of the pipeline

    try:
        # Delete a pipeline
        api_instance.delete_pipeline(organization_id, workspace_id, project_id, pipeline_id)
    except Exception as e:
        print("Exception when calling CloudIDEPipelineApi->delete_pipeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **project_id** | **str**| The ID of the project | 
 **pipeline_id** | **str**| ID of the pipeline | 

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
**204** |  |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline**
> Pipeline get_pipeline(organization_id, workspace_id, project_id, pipeline_id)

Get a pipeline

Get a pipeline

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.pipeline import Pipeline
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
    api_instance = astronomercoreapi.CloudIDEPipelineApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | The ID of the project
    pipeline_id = 'pipeline_id_example' # str | ID of the pipeline

    try:
        # Get a pipeline
        api_response = api_instance.get_pipeline(organization_id, workspace_id, project_id, pipeline_id)
        print("The response of CloudIDEPipelineApi->get_pipeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDEPipelineApi->get_pipeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| The ID of the project | 
 **pipeline_id** | **str**| ID of the pipeline | 

### Return type

[**Pipeline**](Pipeline.md)

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

# **list_pipelines**
> PipelinesPaginated list_pipelines(organization_id, workspace_ids=workspace_ids, project_ids=project_ids, offset=offset, limit=limit, search=search, sorts=sorts)

List pipelines

List pipelines

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.pipelines_paginated import PipelinesPaginated
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
    api_instance = astronomercoreapi.CloudIDEPipelineApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_ids = ['workspace_ids_example'] # List[str] | workspace IDs the pipelines belong to (optional)
    project_ids = ['project_ids_example'] # List[str] | project IDs the pipelines belong to (optional)
    offset = 0 # int | offset for pagination (optional) (default to 0)
    limit = 20 # int | limit for pagination (optional) (default to 20)
    search = 'search_example' # str | search string across pipeline name and description (optional)
    sorts = ['sorts_example'] # List[str] | sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc' (optional)

    try:
        # List pipelines
        api_response = api_instance.list_pipelines(organization_id, workspace_ids=workspace_ids, project_ids=project_ids, offset=offset, limit=limit, search=search, sorts=sorts)
        print("The response of CloudIDEPipelineApi->list_pipelines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDEPipelineApi->list_pipelines: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_ids** | [**List[str]**](str.md)| workspace IDs the pipelines belong to | [optional] 
 **project_ids** | [**List[str]**](str.md)| project IDs the pipelines belong to | [optional] 
 **offset** | **int**| offset for pagination | [optional] [default to 0]
 **limit** | **int**| limit for pagination | [optional] [default to 20]
 **search** | **str**| search string across pipeline name and description | [optional] 
 **sorts** | [**List[str]**](str.md)| sorting criteria, each criterion should conform to format &#39;fieldName:asc&#39; or &#39;fieldName:desc&#39; | [optional] 

### Return type

[**PipelinesPaginated**](PipelinesPaginated.md)

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

# **update_pipeline**
> update_pipeline(organization_id, workspace_id, project_id, pipeline_id, data)

Update a pipeline

Update a pipeline

### Example

```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.update_pipeline_request import UpdatePipelineRequest
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
    api_instance = astronomercoreapi.CloudIDEPipelineApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    project_id = 'project_id_example' # str | ID of the project
    pipeline_id = 'pipeline_id_example' # str | ID of the pipeline
    data = astronomercoreapi.UpdatePipelineRequest() # UpdatePipelineRequest | request body for updating a pipeline

    try:
        # Update a pipeline
        api_instance.update_pipeline(organization_id, workspace_id, project_id, pipeline_id, data)
    except Exception as e:
        print("Exception when calling CloudIDEPipelineApi->update_pipeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **project_id** | **str**| ID of the project | 
 **pipeline_id** | **str**| ID of the pipeline | 
 **data** | [**UpdatePipelineRequest**](UpdatePipelineRequest.md)| request body for updating a pipeline | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

