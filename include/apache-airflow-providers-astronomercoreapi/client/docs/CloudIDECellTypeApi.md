# astronomercoreapi.CloudIDECellTypeApi

All URIs are relative to *https://api.astronomer.io/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cell_type**](CloudIDECellTypeApi.md#create_cell_type) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/cell-types | Create a new cell type
[**delete_cell_type**](CloudIDECellTypeApi.md#delete_cell_type) | **DELETE** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/cell-types/{cellTypeName} | Delete a cell type
[**get_cell_type**](CloudIDECellTypeApi.md#get_cell_type) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/cell-types/{cellTypeName} | Get a cell type
[**list_cell_types**](CloudIDECellTypeApi.md#list_cell_types) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/cell-types | List cell types
[**update_cell_type**](CloudIDECellTypeApi.md#update_cell_type) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/cell-types/{cellTypeName} | Update a cell type
[**validate_cell_type**](CloudIDECellTypeApi.md#validate_cell_type) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/validate-cell-type | Validate a cell type


# **create_cell_type**
> CreateCellType create_cell_type(organization_id, workspace_id, project_id, data)

Create a new cell type

Create a new cell type

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.create_cell_type import CreateCellType
from astronomercoreapi.models.create_cell_type_request import CreateCellTypeRequest
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
    api_instance = astronomercoreapi.CloudIDECellTypeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | project ID
    data = astronomercoreapi.CreateCellTypeRequest() # CreateCellTypeRequest | request body for creating a new cell type

    try:
        # Create a new cell type
        api_response = api_instance.create_cell_type(organization_id, workspace_id, project_id, data)
        print("The response of CloudIDECellTypeApi->create_cell_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDECellTypeApi->create_cell_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| project ID | 
 **data** | [**CreateCellTypeRequest**](CreateCellTypeRequest.md)| request body for creating a new cell type | 

### Return type

[**CreateCellType**](CreateCellType.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cell_type**
> delete_cell_type(organization_id, workspace_id, project_id, cell_type_name)

Delete a cell type

Delete a cell type

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
    api_instance = astronomercoreapi.CloudIDECellTypeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | project ID
    cell_type_name = 'cell_type_name_example' # str | cell type name

    try:
        # Delete a cell type
        api_instance.delete_cell_type(organization_id, workspace_id, project_id, cell_type_name)
    except Exception as e:
        print("Exception when calling CloudIDECellTypeApi->delete_cell_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| project ID | 
 **cell_type_name** | **str**| cell type name | 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cell_type**
> GetCellType get_cell_type(organization_id, workspace_id, project_id, cell_type_name)

Get a cell type

Get a cell type

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.get_cell_type import GetCellType
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
    api_instance = astronomercoreapi.CloudIDECellTypeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | project ID
    cell_type_name = 'cell_type_name_example' # str | cell type name

    try:
        # Get a cell type
        api_response = api_instance.get_cell_type(organization_id, workspace_id, project_id, cell_type_name)
        print("The response of CloudIDECellTypeApi->get_cell_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDECellTypeApi->get_cell_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| project ID | 
 **cell_type_name** | **str**| cell type name | 

### Return type

[**GetCellType**](GetCellType.md)

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

# **list_cell_types**
> ListCellTypes list_cell_types(organization_id, workspace_id, project_id, names=names)

List cell types

List cell types

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.list_cell_types import ListCellTypes
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
    api_instance = astronomercoreapi.CloudIDECellTypeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | project ID
    names = 'names_example' # str | cell type names to filter by, comma-separated (optional)

    try:
        # List cell types
        api_response = api_instance.list_cell_types(organization_id, workspace_id, project_id, names=names)
        print("The response of CloudIDECellTypeApi->list_cell_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDECellTypeApi->list_cell_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| project ID | 
 **names** | **str**| cell type names to filter by, comma-separated | [optional] 

### Return type

[**ListCellTypes**](ListCellTypes.md)

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

# **update_cell_type**
> update_cell_type(organization_id, workspace_id, project_id, cell_type_name, data)

Update a cell type

Update a cell type

### Example

```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.update_cell_type_request import UpdateCellTypeRequest
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
    api_instance = astronomercoreapi.CloudIDECellTypeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | project ID
    cell_type_name = 'cell_type_name_example' # str | cell type name
    data = astronomercoreapi.UpdateCellTypeRequest() # UpdateCellTypeRequest | request body for updating a cell type

    try:
        # Update a cell type
        api_instance.update_cell_type(organization_id, workspace_id, project_id, cell_type_name, data)
    except Exception as e:
        print("Exception when calling CloudIDECellTypeApi->update_cell_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| project ID | 
 **cell_type_name** | **str**| cell type name | 
 **data** | [**UpdateCellTypeRequest**](UpdateCellTypeRequest.md)| request body for updating a cell type | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_cell_type**
> ValidateCellType validate_cell_type(organization_id, workspace_id, project_id, data)

Validate a cell type

Validate a cell type

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.validate_cell_type import ValidateCellType
from astronomercoreapi.models.validate_cell_type_request import ValidateCellTypeRequest
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
    api_instance = astronomercoreapi.CloudIDECellTypeApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | project ID
    data = astronomercoreapi.ValidateCellTypeRequest() # ValidateCellTypeRequest | request body for validating a cell type

    try:
        # Validate a cell type
        api_response = api_instance.validate_cell_type(organization_id, workspace_id, project_id, data)
        print("The response of CloudIDECellTypeApi->validate_cell_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDECellTypeApi->validate_cell_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| project ID | 
 **data** | [**ValidateCellTypeRequest**](ValidateCellTypeRequest.md)| request body for validating a cell type | 

### Return type

[**ValidateCellType**](ValidateCellType.md)

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

