# astronomercoreapi.ClusterApi

All URIs are relative to *https://api.astronomer.io/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_aws_cluster**](ClusterApi.md#create_aws_cluster) | **POST** /organizations/{organizationId}/clusters/aws | Create AWS cluster
[**create_azure_cluster**](ClusterApi.md#create_azure_cluster) | **POST** /organizations/{organizationId}/clusters/azure | Create Azure cluster
[**create_gcp_cluster**](ClusterApi.md#create_gcp_cluster) | **POST** /organizations/{organizationId}/clusters/gcp | Create GCP cluster
[**delete_cluster**](ClusterApi.md#delete_cluster) | **DELETE** /organizations/{organizationId}/clusters/{clusterId} | Delete cluster
[**get_cluster**](ClusterApi.md#get_cluster) | **GET** /organizations/{organizationId}/clusters/{clusterId} | Get a cluster
[**get_shared_cluster**](ClusterApi.md#get_shared_cluster) | **GET** /clusters/shared | Get a shared cluster for a given provider/region
[**list_clusters**](ClusterApi.md#list_clusters) | **GET** /organizations/{organizationId}/clusters | List clusters
[**update_aws_cluster**](ClusterApi.md#update_aws_cluster) | **POST** /organizations/{organizationId}/clusters/aws/{clusterId} | Update AWS cluster
[**update_azure_cluster**](ClusterApi.md#update_azure_cluster) | **POST** /organizations/{organizationId}/clusters/azure/{clusterId} | Update Azure cluster
[**update_gcp_cluster**](ClusterApi.md#update_gcp_cluster) | **POST** /organizations/{organizationId}/clusters/gcp/{clusterId} | Update GCP cluster


# **create_aws_cluster**
> Cluster create_aws_cluster(organization_id, body)

Create AWS cluster

Create AWS cluster

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.cluster import Cluster
from astronomercoreapi.models.create_aws_cluster_request import CreateAwsClusterRequest
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
    api_instance = astronomercoreapi.ClusterApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    body = astronomercoreapi.CreateAwsClusterRequest() # CreateAwsClusterRequest | request body for creating a new AWS cluster

    try:
        # Create AWS cluster
        api_response = api_instance.create_aws_cluster(organization_id, body)
        print("The response of ClusterApi->create_aws_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->create_aws_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **body** | [**CreateAwsClusterRequest**](CreateAwsClusterRequest.md)| request body for creating a new AWS cluster | 

### Return type

[**Cluster**](Cluster.md)

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
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_azure_cluster**
> Cluster create_azure_cluster(organization_id, body)

Create Azure cluster

Create Azure cluster

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.cluster import Cluster
from astronomercoreapi.models.create_azure_cluster_request import CreateAzureClusterRequest
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
    api_instance = astronomercoreapi.ClusterApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    body = astronomercoreapi.CreateAzureClusterRequest() # CreateAzureClusterRequest | request body for creating a new Azure cluster

    try:
        # Create Azure cluster
        api_response = api_instance.create_azure_cluster(organization_id, body)
        print("The response of ClusterApi->create_azure_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->create_azure_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **body** | [**CreateAzureClusterRequest**](CreateAzureClusterRequest.md)| request body for creating a new Azure cluster | 

### Return type

[**Cluster**](Cluster.md)

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
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_gcp_cluster**
> Cluster create_gcp_cluster(organization_id, body)

Create GCP cluster

Create GCP cluster

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.cluster import Cluster
from astronomercoreapi.models.create_gcp_cluster_request import CreateGcpClusterRequest
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
    api_instance = astronomercoreapi.ClusterApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    body = astronomercoreapi.CreateGcpClusterRequest() # CreateGcpClusterRequest | request body for creating a new GCP cluster

    try:
        # Create GCP cluster
        api_response = api_instance.create_gcp_cluster(organization_id, body)
        print("The response of ClusterApi->create_gcp_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->create_gcp_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **body** | [**CreateGcpClusterRequest**](CreateGcpClusterRequest.md)| request body for creating a new GCP cluster | 

### Return type

[**Cluster**](Cluster.md)

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
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster**
> delete_cluster(organization_id, cluster_id)

Delete cluster

Delete cluster

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
    api_instance = astronomercoreapi.ClusterApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    cluster_id = 'cluster_id_example' # str | cluster ID

    try:
        # Delete cluster
        api_instance.delete_cluster(organization_id, cluster_id)
    except Exception as e:
        print("Exception when calling ClusterApi->delete_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **cluster_id** | **str**| cluster ID | 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster**
> ClusterDetailed get_cluster(organization_id, cluster_id)

Get a cluster

Get a cluster in an organization

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.cluster_detailed import ClusterDetailed
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
    api_instance = astronomercoreapi.ClusterApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    cluster_id = 'cluster_id_example' # str | cluster ID to fetch

    try:
        # Get a cluster
        api_response = api_instance.get_cluster(organization_id, cluster_id)
        print("The response of ClusterApi->get_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->get_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **cluster_id** | **str**| cluster ID to fetch | 

### Return type

[**ClusterDetailed**](ClusterDetailed.md)

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

# **get_shared_cluster**
> SharedCluster get_shared_cluster(region, cloud_provider)

Get a shared cluster for a given provider/region

Get a shared cluster for a given provider/region

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.shared_cluster import SharedCluster
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
    api_instance = astronomercoreapi.ClusterApi(api_client)
    region = 'region_example' # str | region
    cloud_provider = 'cloud_provider_example' # str | cloud provider

    try:
        # Get a shared cluster for a given provider/region
        api_response = api_instance.get_shared_cluster(region, cloud_provider)
        print("The response of ClusterApi->get_shared_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->get_shared_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**| region | 
 **cloud_provider** | **str**| cloud provider | 

### Return type

[**SharedCluster**](SharedCluster.md)

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

# **list_clusters**
> ClustersPaginated list_clusters(organization_id, provider=provider, types=types, status=status, search=search, offset=offset, limit=limit, sorts=sorts)

List clusters

List clusters in an organization

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.clusters_paginated import ClustersPaginated
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
    api_instance = astronomercoreapi.ClusterApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    provider = 'provider_example' # str | cloud provider to filter clusters on (optional)
    types = ['types_example'] # List[str] | type to filter clusters on (optional)
    status = 'status_example' # str | status to filter clusters on (optional)
    search = 'search_example' # str | string to search for when listing clusters (optional)
    offset = 0 # int | offset for pagination (optional) (default to 0)
    limit = 20 # int | limit for pagination (optional) (default to 20)
    sorts = ['sorts_example'] # List[str] | sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc' (optional)

    try:
        # List clusters
        api_response = api_instance.list_clusters(organization_id, provider=provider, types=types, status=status, search=search, offset=offset, limit=limit, sorts=sorts)
        print("The response of ClusterApi->list_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->list_clusters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **provider** | **str**| cloud provider to filter clusters on | [optional] 
 **types** | [**List[str]**](str.md)| type to filter clusters on | [optional] 
 **status** | **str**| status to filter clusters on | [optional] 
 **search** | **str**| string to search for when listing clusters | [optional] 
 **offset** | **int**| offset for pagination | [optional] [default to 0]
 **limit** | **int**| limit for pagination | [optional] [default to 20]
 **sorts** | [**List[str]**](str.md)| sorting criteria, each criterion should conform to format &#39;fieldName:asc&#39; or &#39;fieldName:desc&#39; | [optional] 

### Return type

[**ClustersPaginated**](ClustersPaginated.md)

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

# **update_aws_cluster**
> Cluster update_aws_cluster(organization_id, cluster_id, body)

Update AWS cluster

Update AWS cluster

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.cluster import Cluster
from astronomercoreapi.models.update_aws_cluster_request import UpdateAwsClusterRequest
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
    api_instance = astronomercoreapi.ClusterApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    cluster_id = 'cluster_id_example' # str | cluster ID
    body = astronomercoreapi.UpdateAwsClusterRequest() # UpdateAwsClusterRequest | request body for updating an AWS cluster

    try:
        # Update AWS cluster
        api_response = api_instance.update_aws_cluster(organization_id, cluster_id, body)
        print("The response of ClusterApi->update_aws_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->update_aws_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **cluster_id** | **str**| cluster ID | 
 **body** | [**UpdateAwsClusterRequest**](UpdateAwsClusterRequest.md)| request body for updating an AWS cluster | 

### Return type

[**Cluster**](Cluster.md)

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
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_azure_cluster**
> Cluster update_azure_cluster(organization_id, cluster_id, body)

Update Azure cluster

Update Azure cluster

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.cluster import Cluster
from astronomercoreapi.models.update_azure_cluster_request import UpdateAzureClusterRequest
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
    api_instance = astronomercoreapi.ClusterApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    cluster_id = 'cluster_id_example' # str | cluster ID
    body = astronomercoreapi.UpdateAzureClusterRequest() # UpdateAzureClusterRequest | request body for updating an Azure cluster

    try:
        # Update Azure cluster
        api_response = api_instance.update_azure_cluster(organization_id, cluster_id, body)
        print("The response of ClusterApi->update_azure_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->update_azure_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **cluster_id** | **str**| cluster ID | 
 **body** | [**UpdateAzureClusterRequest**](UpdateAzureClusterRequest.md)| request body for updating an Azure cluster | 

### Return type

[**Cluster**](Cluster.md)

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
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_gcp_cluster**
> Cluster update_gcp_cluster(organization_id, cluster_id, body)

Update GCP cluster

Update GCP cluster

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.cluster import Cluster
from astronomercoreapi.models.update_gcp_cluster_request import UpdateGcpClusterRequest
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
    api_instance = astronomercoreapi.ClusterApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    cluster_id = 'cluster_id_example' # str | cluster ID
    body = astronomercoreapi.UpdateGcpClusterRequest() # UpdateGcpClusterRequest | request body for updating a GCP cluster

    try:
        # Update GCP cluster
        api_response = api_instance.update_gcp_cluster(organization_id, cluster_id, body)
        print("The response of ClusterApi->update_gcp_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->update_gcp_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **cluster_id** | **str**| cluster ID | 
 **body** | [**UpdateGcpClusterRequest**](UpdateGcpClusterRequest.md)| request body for updating a GCP cluster | 

### Return type

[**Cluster**](Cluster.md)

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
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

