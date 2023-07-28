# astronomercoreapi.CloudIDEProjectApi

All URIs are relative to *https://api.astronomer.io/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](CloudIDEProjectApi.md#create_project) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/projects | Create a new project
[**create_project_git_branch**](CloudIDEProjectApi.md#create_project_git_branch) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/git/branches | Create a new Git branch for the project repository
[**create_project_git_commit**](CloudIDEProjectApi.md#create_project_git_commit) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/git/commits | Create a new Git commit for the project
[**delete_project**](CloudIDEProjectApi.md#delete_project) | **DELETE** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId} | Delete a project
[**get_project**](CloudIDEProjectApi.md#get_project) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId} | Get project
[**get_project_git_comparison**](CloudIDEProjectApi.md#get_project_git_comparison) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/git/comparison | Get project Git comparison
[**list_project_git_branches**](CloudIDEProjectApi.md#list_project_git_branches) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/git/branches | List project Git branches
[**list_project_git_commits**](CloudIDEProjectApi.md#list_project_git_commits) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/git/commits | List project Git commits
[**list_projects**](CloudIDEProjectApi.md#list_projects) | **GET** /organizations/{organizationId}/projects | List projects
[**sync_project_include**](CloudIDEProjectApi.md#sync_project_include) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/includes/{includeId}/sync | Synchronize an include of a project
[**test_connection**](CloudIDEProjectApi.md#test_connection) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/test-connection | Test a connection against a project
[**test_project_connection**](CloudIDEProjectApi.md#test_project_connection) | **GET** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId}/connections/{connectionId}/test | Test an existing project connection
[**update_project**](CloudIDEProjectApi.md#update_project) | **POST** /organizations/{organizationId}/workspaces/{workspaceId}/projects/{projectId} | Update a project


# **create_project**
> CreateProject create_project(organization_id, workspace_id, data)

Create a new project

Create a new project

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.create_project import CreateProject
from astronomercoreapi.models.create_project_request import CreateProjectRequest
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
    api_instance = astronomercoreapi.CloudIDEProjectApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    data = astronomercoreapi.CreateProjectRequest() # CreateProjectRequest | request body for creating a new project

    try:
        # Create a new project
        api_response = api_instance.create_project(organization_id, workspace_id, data)
        print("The response of CloudIDEProjectApi->create_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDEProjectApi->create_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **data** | [**CreateProjectRequest**](CreateProjectRequest.md)| request body for creating a new project | 

### Return type

[**CreateProject**](CreateProject.md)

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

# **create_project_git_branch**
> ProjectGitBranch create_project_git_branch(organization_id, workspace_id, project_id, data)

Create a new Git branch for the project repository

Create a new Git branch for the project repository

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.create_project_git_branch_request import CreateProjectGitBranchRequest
from astronomercoreapi.models.project_git_branch import ProjectGitBranch
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
    api_instance = astronomercoreapi.CloudIDEProjectApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | The ID of the project
    data = astronomercoreapi.CreateProjectGitBranchRequest() # CreateProjectGitBranchRequest | request body for creating a new branch

    try:
        # Create a new Git branch for the project repository
        api_response = api_instance.create_project_git_branch(organization_id, workspace_id, project_id, data)
        print("The response of CloudIDEProjectApi->create_project_git_branch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDEProjectApi->create_project_git_branch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| The ID of the project | 
 **data** | [**CreateProjectGitBranchRequest**](CreateProjectGitBranchRequest.md)| request body for creating a new branch | 

### Return type

[**ProjectGitBranch**](ProjectGitBranch.md)

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

# **create_project_git_commit**
> ProjectGitCommit create_project_git_commit(organization_id, workspace_id, project_id, data)

Create a new Git commit for the project

Create a new Git commit for the project

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.create_project_git_commit_request import CreateProjectGitCommitRequest
from astronomercoreapi.models.project_git_commit import ProjectGitCommit
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
    api_instance = astronomercoreapi.CloudIDEProjectApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | The ID of the project
    data = astronomercoreapi.CreateProjectGitCommitRequest() # CreateProjectGitCommitRequest | request body for creating a new commit

    try:
        # Create a new Git commit for the project
        api_response = api_instance.create_project_git_commit(organization_id, workspace_id, project_id, data)
        print("The response of CloudIDEProjectApi->create_project_git_commit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDEProjectApi->create_project_git_commit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| The ID of the project | 
 **data** | [**CreateProjectGitCommitRequest**](CreateProjectGitCommitRequest.md)| request body for creating a new commit | 

### Return type

[**ProjectGitCommit**](ProjectGitCommit.md)

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

# **delete_project**
> delete_project(organization_id, workspace_id, project_id)

Delete a project

Delete a single project by id

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
    api_instance = astronomercoreapi.CloudIDEProjectApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | The ID of the project

    try:
        # Delete a project
        api_instance.delete_project(organization_id, workspace_id, project_id)
    except Exception as e:
        print("Exception when calling CloudIDEProjectApi->delete_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| The ID of the project | 

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

# **get_project**
> Project get_project(organization_id, workspace_id, project_id, include_pipeline_count=include_pipeline_count)

Get project

Get a single project by id

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.project import Project
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
    api_instance = astronomercoreapi.CloudIDEProjectApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | The ID of the project
    include_pipeline_count = False # bool | Include pipeline count for the project (optional) (default to False)

    try:
        # Get project
        api_response = api_instance.get_project(organization_id, workspace_id, project_id, include_pipeline_count=include_pipeline_count)
        print("The response of CloudIDEProjectApi->get_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDEProjectApi->get_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| The ID of the project | 
 **include_pipeline_count** | **bool**| Include pipeline count for the project | [optional] [default to False]

### Return type

[**Project**](Project.md)

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

# **get_project_git_comparison**
> ProjectGitComparison get_project_git_comparison(organization_id, workspace_id, project_id, branch=branch, exclude_config=exclude_config, pipeline_id=pipeline_id)

Get project Git comparison

Get a comparison between the project and its associated Git branch

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.project_git_comparison import ProjectGitComparison
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
    api_instance = astronomercoreapi.CloudIDEProjectApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | The ID of the project
    branch = 'branch_example' # str | The branch to compare against, if different to the project's branch (optional)
    exclude_config = True # bool | Whether to exclude config files from the comparison (optional)
    pipeline_id = 'pipeline_id_example' # str | only include changes for this pipeline (optional)

    try:
        # Get project Git comparison
        api_response = api_instance.get_project_git_comparison(organization_id, workspace_id, project_id, branch=branch, exclude_config=exclude_config, pipeline_id=pipeline_id)
        print("The response of CloudIDEProjectApi->get_project_git_comparison:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDEProjectApi->get_project_git_comparison: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| The ID of the project | 
 **branch** | **str**| The branch to compare against, if different to the project&#39;s branch | [optional] 
 **exclude_config** | **bool**| Whether to exclude config files from the comparison | [optional] 
 **pipeline_id** | **str**| only include changes for this pipeline | [optional] 

### Return type

[**ProjectGitComparison**](ProjectGitComparison.md)

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

# **list_project_git_branches**
> ProjectGitBranchesPaginated list_project_git_branches(organization_id, workspace_id, project_id, repo=repo, vendor=vendor, azure_dev_ops_organization=azure_dev_ops_organization, azure_dev_ops_project_id=azure_dev_ops_project_id, page=page, per_page=per_page, x_git_token=x_git_token)

List project Git branches

List project Git branches

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.project_git_branches_paginated import ProjectGitBranchesPaginated
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
    api_instance = astronomercoreapi.CloudIDEProjectApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | Workspace ID that the project belong to
    project_id = 'project_id_example' # str | The ID of the project
    repo = 'repo_example' # str | a repo to override the project's repo (optional)
    vendor = 'vendor_example' # str | a vendor to override the project's git vendor (optional)
    azure_dev_ops_organization = 'azure_dev_ops_organization_example' # str | an Azure DevOps organization to override the project's git vendor attributes (optional)
    azure_dev_ops_project_id = 'azure_dev_ops_project_id_example' # str | an Azure DevOps project ID to override the project's git vendor attributes (optional)
    page = 1 # int | page number for pagination (optional) (default to 1)
    per_page = 20 # int | page size for pagination (optional) (default to 20)
    x_git_token = 'x_git_token_example' # str | a token to override the project's token (optional)

    try:
        # List project Git branches
        api_response = api_instance.list_project_git_branches(organization_id, workspace_id, project_id, repo=repo, vendor=vendor, azure_dev_ops_organization=azure_dev_ops_organization, azure_dev_ops_project_id=azure_dev_ops_project_id, page=page, per_page=per_page, x_git_token=x_git_token)
        print("The response of CloudIDEProjectApi->list_project_git_branches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDEProjectApi->list_project_git_branches: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| Workspace ID that the project belong to | 
 **project_id** | **str**| The ID of the project | 
 **repo** | **str**| a repo to override the project&#39;s repo | [optional] 
 **vendor** | **str**| a vendor to override the project&#39;s git vendor | [optional] 
 **azure_dev_ops_organization** | **str**| an Azure DevOps organization to override the project&#39;s git vendor attributes | [optional] 
 **azure_dev_ops_project_id** | **str**| an Azure DevOps project ID to override the project&#39;s git vendor attributes | [optional] 
 **page** | **int**| page number for pagination | [optional] [default to 1]
 **per_page** | **int**| page size for pagination | [optional] [default to 20]
 **x_git_token** | **str**| a token to override the project&#39;s token | [optional] 

### Return type

[**ProjectGitBranchesPaginated**](ProjectGitBranchesPaginated.md)

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

# **list_project_git_commits**
> ProjectGitCommitsPaginated list_project_git_commits(organization_id, workspace_id, project_id, branch=branch, page=page, per_page=per_page)

List project Git commits

List project Git commits

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.project_git_commits_paginated import ProjectGitCommitsPaginated
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
    api_instance = astronomercoreapi.CloudIDEProjectApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | Workspace ID that the project belong to
    project_id = 'project_id_example' # str | The ID of the project
    branch = 'branch_example' # str | The branch to list commits for, if different to the project's branch (optional)
    page = 1 # int | page number for pagination (optional) (default to 1)
    per_page = 20 # int | page size for pagination (optional) (default to 20)

    try:
        # List project Git commits
        api_response = api_instance.list_project_git_commits(organization_id, workspace_id, project_id, branch=branch, page=page, per_page=per_page)
        print("The response of CloudIDEProjectApi->list_project_git_commits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDEProjectApi->list_project_git_commits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| Workspace ID that the project belong to | 
 **project_id** | **str**| The ID of the project | 
 **branch** | **str**| The branch to list commits for, if different to the project&#39;s branch | [optional] 
 **page** | **int**| page number for pagination | [optional] [default to 1]
 **per_page** | **int**| page size for pagination | [optional] [default to 20]

### Return type

[**ProjectGitCommitsPaginated**](ProjectGitCommitsPaginated.md)

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

# **list_projects**
> ProjectsPaginated list_projects(organization_id, workspace_ids=workspace_ids, include_pipeline_counts=include_pipeline_counts, offset=offset, limit=limit, search=search, sorts=sorts)

List projects

List projects

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.projects_paginated import ProjectsPaginated
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
    api_instance = astronomercoreapi.CloudIDEProjectApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_ids = ['workspace_ids_example'] # List[str] | Workspace IDs that projects belong to (optional)
    include_pipeline_counts = False # bool | Include pipeline counts for each project (optional) (default to False)
    offset = 0 # int | offset for pagination (optional) (default to 0)
    limit = 20 # int | limit for pagination (optional) (default to 20)
    search = 'search_example' # str | search string across name and description (optional)
    sorts = ['sorts_example'] # List[str] | sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc' (optional)

    try:
        # List projects
        api_response = api_instance.list_projects(organization_id, workspace_ids=workspace_ids, include_pipeline_counts=include_pipeline_counts, offset=offset, limit=limit, search=search, sorts=sorts)
        print("The response of CloudIDEProjectApi->list_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDEProjectApi->list_projects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_ids** | [**List[str]**](str.md)| Workspace IDs that projects belong to | [optional] 
 **include_pipeline_counts** | **bool**| Include pipeline counts for each project | [optional] [default to False]
 **offset** | **int**| offset for pagination | [optional] [default to 0]
 **limit** | **int**| limit for pagination | [optional] [default to 20]
 **search** | **str**| search string across name and description | [optional] 
 **sorts** | [**List[str]**](str.md)| sorting criteria, each criterion should conform to format &#39;fieldName:asc&#39; or &#39;fieldName:desc&#39; | [optional] 

### Return type

[**ProjectsPaginated**](ProjectsPaginated.md)

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

# **sync_project_include**
> sync_project_include(organization_id, workspace_id, project_id, include_id)

Synchronize an include of a project

Synchronize an include of a project

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
    api_instance = astronomercoreapi.CloudIDEProjectApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | The ID of the project
    include_id = 'include_id_example' # str | The name of the include

    try:
        # Synchronize an include of a project
        api_instance.sync_project_include(organization_id, workspace_id, project_id, include_id)
    except Exception as e:
        print("Exception when calling CloudIDEProjectApi->sync_project_include: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| The ID of the project | 
 **include_id** | **str**| The name of the include | 

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
**200** |  |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_connection**
> TestConnection test_connection(organization_id, workspace_id, project_id, data)

Test a connection against a project

Test a connection against a project

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.test_connection import TestConnection
from astronomercoreapi.models.test_connection_request import TestConnectionRequest
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
    api_instance = astronomercoreapi.CloudIDEProjectApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | The ID of the project
    data = astronomercoreapi.TestConnectionRequest() # TestConnectionRequest | request body for testing a connection

    try:
        # Test a connection against a project
        api_response = api_instance.test_connection(organization_id, workspace_id, project_id, data)
        print("The response of CloudIDEProjectApi->test_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDEProjectApi->test_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| The ID of the project | 
 **data** | [**TestConnectionRequest**](TestConnectionRequest.md)| request body for testing a connection | 

### Return type

[**TestConnection**](TestConnection.md)

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

# **test_project_connection**
> TestConnection test_project_connection(organization_id, workspace_id, project_id, connection_id)

Test an existing project connection

Test an existing project connection

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.test_connection import TestConnection
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
    api_instance = astronomercoreapi.CloudIDEProjectApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | The ID of the project
    connection_id = 'connection_id_example' # str | The ID of the connection

    try:
        # Test an existing project connection
        api_response = api_instance.test_project_connection(organization_id, workspace_id, project_id, connection_id)
        print("The response of CloudIDEProjectApi->test_project_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudIDEProjectApi->test_project_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| The ID of the project | 
 **connection_id** | **str**| The ID of the connection | 

### Return type

[**TestConnection**](TestConnection.md)

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

# **update_project**
> update_project(organization_id, workspace_id, project_id, data)

Update a project

Update a project

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.update_project_request import UpdateProjectRequest
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
    api_instance = astronomercoreapi.CloudIDEProjectApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    workspace_id = 'workspace_id_example' # str | workspace ID
    project_id = 'project_id_example' # str | The ID of the project
    data = astronomercoreapi.UpdateProjectRequest() # UpdateProjectRequest | request body for updating a project

    try:
        # Update a project
        api_instance.update_project(organization_id, workspace_id, project_id, data)
    except Exception as e:
        print("Exception when calling CloudIDEProjectApi->update_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **workspace_id** | **str**| workspace ID | 
 **project_id** | **str**| The ID of the project | 
 **data** | [**UpdateProjectRequest**](UpdateProjectRequest.md)| request body for updating a project | 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

