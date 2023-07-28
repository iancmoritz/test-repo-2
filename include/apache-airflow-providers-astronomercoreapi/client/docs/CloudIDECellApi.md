# astronomercoreapi.CloudIDECellApi

All URIs are relative to *https://api.astronomer.io/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cell**](CloudIDECellApi.md#create_cell) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/pipelines/{pipelineId}/cells | Create a new cell
[**delete_cell**](CloudIDECellApi.md#delete_cell) | **DELETE** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/pipelines/{pipelineId}/cells/{cellId} | Delete a cell
[**duplicate_cell**](CloudIDECellApi.md#duplicate_cell) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/pipelines/{pipelineId}/cells/{cellId}/duplicate | Duplicate a cell
[**get_cell**](CloudIDECellApi.md#get_cell) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/pipelines/{pipelineId}/cells/{cellId} | Get a cell
[**list_cells**](CloudIDECellApi.md#list_cells) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/pipelines/{pipelineId}/cells | List cells for a project
[**update_cell**](CloudIDECellApi.md#update_cell) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/pipelines/{pipelineId}/cells/{cellId} | Update a cell


# **create_cell**
> CreateCell create_cell(organization_id, workspace_id, project_id, pipeline_id, data)

Create a new cell

Create a new cell

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.create_cell import CreateCell
from astronomercoreapi.models.create_cell_request import CreateCellRequest
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
    api_instance = astronomercoreapi.CloudIDECellApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | project ID
    pipeline_id = 'pipeline_id_example' # str | pipeline ID
    data = astronomercoreapi.CreateCellRequest() # CreateCellRequest | request body for creating a new cell

    try:
        # Create a new cell
        api_response = api_instance.create_cell(organization_id, workspace_id, project_id, pipeline_id, data)
        print("The response of CloudIDECellApi->create_cell:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDECellApi->create_cell: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| project ID | 
 **pipeline_id** | **str**| pipeline ID | 
 **data** | [**CreateCellRequest**](CreateCellRequest.md)| request body for creating a new cell | 

### Return type

[**CreateCell**](CreateCell.md)

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

# **delete_cell**
> delete_cell(organization_id, workspace_id, project_id, pipeline_id, cell_id)

Delete a cell

Delete a cell

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
    api_instance = astronomercoreapi.CloudIDECellApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    project_id = 'project_id_example' # str | ID of the project
    pipeline_id = 'pipeline_id_example' # str | ID of the pipeline
    cell_id = 'cell_id_example' # str | ID of the cell

    try:
        # Delete a cell
        api_instance.delete_cell(organization_id, workspace_id, project_id, pipeline_id, cell_id)
    except Exception as e:
        print("Exception when calling CloudIDECellApi->delete_cell: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **project_id** | **str**| ID of the project | 
 **pipeline_id** | **str**| ID of the pipeline | 
 **cell_id** | **str**| ID of the cell | 

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

# **duplicate_cell**
> DuplicateCell duplicate_cell(organization_id, workspace_id, project_id, pipeline_id, cell_id, data)

Duplicate a cell

Duplicate a cell

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.duplicate_cell import DuplicateCell
from astronomercoreapi.models.duplicate_cell_request import DuplicateCellRequest
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
    api_instance = astronomercoreapi.CloudIDECellApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    project_id = 'project_id_example' # str | ID of the project
    pipeline_id = 'pipeline_id_example' # str | ID of the pipeline
    cell_id = 'cell_id_example' # str | ID of the cell
    data = astronomercoreapi.DuplicateCellRequest() # DuplicateCellRequest | request body for duplicating a cell

    try:
        # Duplicate a cell
        api_response = api_instance.duplicate_cell(organization_id, workspace_id, project_id, pipeline_id, cell_id, data)
        print("The response of CloudIDECellApi->duplicate_cell:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDECellApi->duplicate_cell: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **project_id** | **str**| ID of the project | 
 **pipeline_id** | **str**| ID of the pipeline | 
 **cell_id** | **str**| ID of the cell | 
 **data** | [**DuplicateCellRequest**](DuplicateCellRequest.md)| request body for duplicating a cell | 

### Return type

[**DuplicateCell**](DuplicateCell.md)

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

# **get_cell**
> Cell get_cell(organization_id, workspace_id, project_id, pipeline_id, cell_id)

Get a cell

Get a cell

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.cell import Cell
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
    api_instance = astronomercoreapi.CloudIDECellApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | The ID of the project
    pipeline_id = 'pipeline_id_example' # str | The ID of the pipeline
    cell_id = 'cell_id_example' # str | ID of the cell

    try:
        # Get a cell
        api_response = api_instance.get_cell(organization_id, workspace_id, project_id, pipeline_id, cell_id)
        print("The response of CloudIDECellApi->get_cell:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDECellApi->get_cell: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| The ID of the project | 
 **pipeline_id** | **str**| The ID of the pipeline | 
 **cell_id** | **str**| ID of the cell | 

### Return type

[**Cell**](Cell.md)

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

# **list_cells**
> CellsPaginated list_cells(organization_id, workspace_id, project_id, pipeline_id, offset=offset, limit=limit, sorts=sorts, include_cell_types=include_cell_types, pipeline_session_id=pipeline_session_id)

List cells for a project

List cells for a project

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.cells_paginated import CellsPaginated
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
    api_instance = astronomercoreapi.CloudIDECellApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | The ID of the project
    pipeline_id = 'pipeline_id_example' # str | The ID of the pipeline
    offset = 0 # int | offset for pagination (optional) (default to 0)
    limit = 20 # int | limit for pagination (optional) (default to 20)
    sorts = ['sorts_example'] # List[str] | sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc' (optional)
    include_cell_types = True # bool | include cell types in response (optional)
    pipeline_session_id = 'pipeline_session_id_example' # str | pipeline session ID (optional)

    try:
        # List cells for a project
        api_response = api_instance.list_cells(organization_id, workspace_id, project_id, pipeline_id, offset=offset, limit=limit, sorts=sorts, include_cell_types=include_cell_types, pipeline_session_id=pipeline_session_id)
        print("The response of CloudIDECellApi->list_cells:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDECellApi->list_cells: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| The ID of the project | 
 **pipeline_id** | **str**| The ID of the pipeline | 
 **offset** | **int**| offset for pagination | [optional] [default to 0]
 **limit** | **int**| limit for pagination | [optional] [default to 20]
 **sorts** | [**List[str]**](str.md)| sorting criteria, each criterion should conform to format &#39;fieldName:asc&#39; or &#39;fieldName:desc&#39; | [optional] 
 **include_cell_types** | **bool**| include cell types in response | [optional] 
 **pipeline_session_id** | **str**| pipeline session ID | [optional] 

### Return type

[**CellsPaginated**](CellsPaginated.md)

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

# **update_cell**
> update_cell(organization_id, workspace_id, project_id, pipeline_id, cell_id, data)

Update a cell

Update a cell

### Example

```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.update_cell_request import UpdateCellRequest
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
    api_instance = astronomercoreapi.CloudIDECellApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | ID of the workspace
    project_id = 'project_id_example' # str | ID of the project
    pipeline_id = 'pipeline_id_example' # str | ID of the pipeline
    cell_id = 'cell_id_example' # str | ID of the cell
    data = astronomercoreapi.UpdateCellRequest() # UpdateCellRequest | request body for updating a cell

    try:
        # Update a cell
        api_instance.update_cell(organization_id, workspace_id, project_id, pipeline_id, cell_id, data)
    except Exception as e:
        print("Exception when calling CloudIDECellApi->update_cell: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| ID of the workspace | 
 **project_id** | **str**| ID of the project | 
 **pipeline_id** | **str**| ID of the pipeline | 
 **cell_id** | **str**| ID of the cell | 
 **data** | [**UpdateCellRequest**](UpdateCellRequest.md)| request body for updating a cell | 

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

