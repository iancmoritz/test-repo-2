# astronomercoreapi.DeploymentMetricsApi

All URIs are relative to *https://api.astronomer.io/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_deployment_cpu_usage_limits**](DeploymentMetricsApi.md#get_deployment_cpu_usage_limits) | **GET** /organizations/{organizationId}/deployments/{deploymentId}/metrics/cpu-usage-limits | Get CPU usage limits metrics for a deployment
[**get_deployment_cpu_usages_per_pod**](DeploymentMetricsApi.md#get_deployment_cpu_usages_per_pod) | **GET** /organizations/{organizationId}/deployments/{deploymentId}/metrics/cpu-usages-per-pod | Get CPU usages metrics per pod for a deployment
[**get_deployment_memory_byte_limits**](DeploymentMetricsApi.md#get_deployment_memory_byte_limits) | **GET** /organizations/{organizationId}/deployments/{deploymentId}/metrics/memory-byte-limits | Get memory byte limits metrics for a deployment
[**get_deployment_memory_bytes_per_pod**](DeploymentMetricsApi.md#get_deployment_memory_bytes_per_pod) | **GET** /organizations/{organizationId}/deployments/{deploymentId}/metrics/memory-bytes-per-pod | Get memory bytes metrics per pod for a deployment
[**get_deployment_network_bytes_per_pod**](DeploymentMetricsApi.md#get_deployment_network_bytes_per_pod) | **GET** /organizations/{organizationId}/deployments/{deploymentId}/metrics/network-bytes-per-pod | Get network bytes metrics per pod for a deployment
[**get_deployment_scheduler_heartbeat**](DeploymentMetricsApi.md#get_deployment_scheduler_heartbeat) | **GET** /organizations/{organizationId}/deployments/{deploymentId}/metrics/scheduler-heartbeats | Get scheduler heartbeats (max per-minute heartbeat count over step interval) metrics for a deployment
[**get_deployments_dag_run_durations_per_status**](DeploymentMetricsApi.md#get_deployments_dag_run_durations_per_status) | **GET** /organizations/{organizationId}/deployments/{deploymentId}/metrics/dag-run-durations-per-status | Get DAG run P90 durations metrics per status for a deployment
[**get_deployments_dag_runs_per_status**](DeploymentMetricsApi.md#get_deployments_dag_runs_per_status) | **GET** /organizations/{organizationId}/deployments/{deploymentId}/metrics/dag-runs-per-status | Get DAG runs metrics per status for a deployment
[**get_deployments_task_run_durations_per_status**](DeploymentMetricsApi.md#get_deployments_task_run_durations_per_status) | **GET** /organizations/{organizationId}/deployments/{deploymentId}/metrics/task-run-durations-per-status | Get task run P90 durations metrics per status for a deployment
[**get_deployments_task_runs_per_status**](DeploymentMetricsApi.md#get_deployments_task_runs_per_status) | **GET** /organizations/{organizationId}/deployments/{deploymentId}/metrics/task-runs-per-status | Get task runs metrics per status for a deployment
[**get_pod_count_over_time**](DeploymentMetricsApi.md#get_pod_count_over_time) | **GET** /organizations/{organizationId}/deployments/{deploymentId}/metrics/pod-count-over-time | Get pod count per component and worker queue and status over time
[**list_deployments_cpu_usages**](DeploymentMetricsApi.md#list_deployments_cpu_usages) | **GET** /organizations/{organizationId}/deployments/metrics/cpu-usages | List CPU usages metrics for deployments
[**list_deployments_dag_runs**](DeploymentMetricsApi.md#list_deployments_dag_runs) | **GET** /organizations/{organizationId}/deployments/metrics/dag-runs-per-status | List DAG runs metrics for deployments
[**list_deployments_dagbag_sizes**](DeploymentMetricsApi.md#list_deployments_dagbag_sizes) | **GET** /organizations/{organizationId}/deployments/metrics/dagbag-sizes | List DAG bag sizes for deployments
[**list_deployments_memory_usages**](DeploymentMetricsApi.md#list_deployments_memory_usages) | **GET** /organizations/{organizationId}/deployments/metrics/memory-usages | List memory usages metrics for deployments
[**list_deployments_pod_count_per_status**](DeploymentMetricsApi.md#list_deployments_pod_count_per_status) | **GET** /organizations/{organizationId}/deployments/{deploymentId}/metrics/pod-count-per-status | Get pod count per status for a deployment
[**list_deployments_pool_count_per_status**](DeploymentMetricsApi.md#list_deployments_pool_count_per_status) | **GET** /organizations/{organizationId}/deployments/{deploymentId}/metrics/pool-count-per-status | Get pool count per status for a deployment
[**list_deployments_task_runs**](DeploymentMetricsApi.md#list_deployments_task_runs) | **GET** /organizations/{organizationId}/deployments/metrics/task-runs-per-status | List task runs metrics for deployments


# **get_deployment_cpu_usage_limits**
> List[RangeMetricPerComponent] get_deployment_cpu_usage_limits(organization_id, deployment_id, range, step)

Get CPU usage limits metrics for a deployment

Get CPU usage limits metrics for a deployment

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.range_metric_per_component import RangeMetricPerComponent
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
    api_instance = astronomercoreapi.DeploymentMetricsApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    deployment_id = 'deployment_id_example' # str | deployment ID corresponding to the metrics
    range = 56 # int | range of the CPU usage limits metrics in seconds
    step = 56 # int | step interval of the CPU usage limits metrics in seconds

    try:
        # Get CPU usage limits metrics for a deployment
        api_response = api_instance.get_deployment_cpu_usage_limits(organization_id, deployment_id, range, step)
        print("The response of DeploymentMetricsApi->get_deployment_cpu_usage_limits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentMetricsApi->get_deployment_cpu_usage_limits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **deployment_id** | **str**| deployment ID corresponding to the metrics | 
 **range** | **int**| range of the CPU usage limits metrics in seconds | 
 **step** | **int**| step interval of the CPU usage limits metrics in seconds | 

### Return type

[**List[RangeMetricPerComponent]**](RangeMetricPerComponent.md)

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
**499** |  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_cpu_usages_per_pod**
> List[RangeMetricPerPod] get_deployment_cpu_usages_per_pod(organization_id, deployment_id, range, step)

Get CPU usages metrics per pod for a deployment

Get CPU usages metrics per pod for a deployment

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.range_metric_per_pod import RangeMetricPerPod
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
    api_instance = astronomercoreapi.DeploymentMetricsApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    deployment_id = 'deployment_id_example' # str | deployment ID corresponding to the metrics
    range = 56 # int | range of the CPU usages metrics in seconds
    step = 56 # int | step interval of the CPU usages metrics in seconds

    try:
        # Get CPU usages metrics per pod for a deployment
        api_response = api_instance.get_deployment_cpu_usages_per_pod(organization_id, deployment_id, range, step)
        print("The response of DeploymentMetricsApi->get_deployment_cpu_usages_per_pod:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentMetricsApi->get_deployment_cpu_usages_per_pod: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **deployment_id** | **str**| deployment ID corresponding to the metrics | 
 **range** | **int**| range of the CPU usages metrics in seconds | 
 **step** | **int**| step interval of the CPU usages metrics in seconds | 

### Return type

[**List[RangeMetricPerPod]**](RangeMetricPerPod.md)

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

# **get_deployment_memory_byte_limits**
> List[RangeMetricPerComponent] get_deployment_memory_byte_limits(organization_id, deployment_id, range, step)

Get memory byte limits metrics for a deployment

Get memory byte limits metrics for a deployment

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.range_metric_per_component import RangeMetricPerComponent
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
    api_instance = astronomercoreapi.DeploymentMetricsApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    deployment_id = 'deployment_id_example' # str | deployment ID corresponding to the metrics
    range = 56 # int | range of the memory byte limits metrics in seconds
    step = 56 # int | step interval of the memory byte limits metrics in seconds

    try:
        # Get memory byte limits metrics for a deployment
        api_response = api_instance.get_deployment_memory_byte_limits(organization_id, deployment_id, range, step)
        print("The response of DeploymentMetricsApi->get_deployment_memory_byte_limits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentMetricsApi->get_deployment_memory_byte_limits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **deployment_id** | **str**| deployment ID corresponding to the metrics | 
 **range** | **int**| range of the memory byte limits metrics in seconds | 
 **step** | **int**| step interval of the memory byte limits metrics in seconds | 

### Return type

[**List[RangeMetricPerComponent]**](RangeMetricPerComponent.md)

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
**499** |  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_memory_bytes_per_pod**
> List[RangeMetricPerPod] get_deployment_memory_bytes_per_pod(organization_id, deployment_id, range, step)

Get memory bytes metrics per pod for a deployment

Get memory bytes metrics per pod for a deployment

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.range_metric_per_pod import RangeMetricPerPod
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
    api_instance = astronomercoreapi.DeploymentMetricsApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    deployment_id = 'deployment_id_example' # str | deployment ID corresponding to the metrics
    range = 56 # int | range of the memory bytes metrics in seconds
    step = 56 # int | step interval of the memory bytes metrics in seconds

    try:
        # Get memory bytes metrics per pod for a deployment
        api_response = api_instance.get_deployment_memory_bytes_per_pod(organization_id, deployment_id, range, step)
        print("The response of DeploymentMetricsApi->get_deployment_memory_bytes_per_pod:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentMetricsApi->get_deployment_memory_bytes_per_pod: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **deployment_id** | **str**| deployment ID corresponding to the metrics | 
 **range** | **int**| range of the memory bytes metrics in seconds | 
 **step** | **int**| step interval of the memory bytes metrics in seconds | 

### Return type

[**List[RangeMetricPerPod]**](RangeMetricPerPod.md)

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

# **get_deployment_network_bytes_per_pod**
> List[RangeMetricPerPod] get_deployment_network_bytes_per_pod(organization_id, deployment_id, range, step)

Get network bytes metrics per pod for a deployment

Get network bytes metrics per pod for a deployment

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.range_metric_per_pod import RangeMetricPerPod
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
    api_instance = astronomercoreapi.DeploymentMetricsApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    deployment_id = 'deployment_id_example' # str | deployment ID corresponding to the metrics
    range = 56 # int | range of the network bytes metrics in seconds
    step = 56 # int | step interval of the network bytes metrics in seconds

    try:
        # Get network bytes metrics per pod for a deployment
        api_response = api_instance.get_deployment_network_bytes_per_pod(organization_id, deployment_id, range, step)
        print("The response of DeploymentMetricsApi->get_deployment_network_bytes_per_pod:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentMetricsApi->get_deployment_network_bytes_per_pod: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **deployment_id** | **str**| deployment ID corresponding to the metrics | 
 **range** | **int**| range of the network bytes metrics in seconds | 
 **step** | **int**| step interval of the network bytes metrics in seconds | 

### Return type

[**List[RangeMetricPerPod]**](RangeMetricPerPod.md)

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

# **get_deployment_scheduler_heartbeat**
> List[RangeMetric] get_deployment_scheduler_heartbeat(organization_id, deployment_id, range, step)

Get scheduler heartbeats (max per-minute heartbeat count over step interval) metrics for a deployment

Get scheduler heartbeats (max per-minute heartbeat count over step interval) metrics for a deployment

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.range_metric import RangeMetric
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
    api_instance = astronomercoreapi.DeploymentMetricsApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    deployment_id = 'deployment_id_example' # str | deployment ID corresponding to the metrics
    range = 56 # int | range of the scheduler heartbeats metrics in seconds
    step = 56 # int | step interval to find max per-minute scheduler heartbeats metrics in seconds

    try:
        # Get scheduler heartbeats (max per-minute heartbeat count over step interval) metrics for a deployment
        api_response = api_instance.get_deployment_scheduler_heartbeat(organization_id, deployment_id, range, step)
        print("The response of DeploymentMetricsApi->get_deployment_scheduler_heartbeat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentMetricsApi->get_deployment_scheduler_heartbeat: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **deployment_id** | **str**| deployment ID corresponding to the metrics | 
 **range** | **int**| range of the scheduler heartbeats metrics in seconds | 
 **step** | **int**| step interval to find max per-minute scheduler heartbeats metrics in seconds | 

### Return type

[**List[RangeMetric]**](RangeMetric.md)

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
**499** |  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployments_dag_run_durations_per_status**
> List[RangeMetricPerStatus] get_deployments_dag_run_durations_per_status(organization_id, deployment_id, range, step, status=status)

Get DAG run P90 durations metrics per status for a deployment

Get DAG run P90 durations metrics per status for a deployment

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.range_metric_per_status import RangeMetricPerStatus
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
    api_instance = astronomercoreapi.DeploymentMetricsApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    deployment_id = 'deployment_id_example' # str | deployment ID corresponding to the metrics
    range = 56 # int | range of the DAG run durations metrics in seconds
    step = 56 # int | step interval of the DAG run durations metrics in seconds
    status = 'status_example' # str | status of dag runs (optional)

    try:
        # Get DAG run P90 durations metrics per status for a deployment
        api_response = api_instance.get_deployments_dag_run_durations_per_status(organization_id, deployment_id, range, step, status=status)
        print("The response of DeploymentMetricsApi->get_deployments_dag_run_durations_per_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentMetricsApi->get_deployments_dag_run_durations_per_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **deployment_id** | **str**| deployment ID corresponding to the metrics | 
 **range** | **int**| range of the DAG run durations metrics in seconds | 
 **step** | **int**| step interval of the DAG run durations metrics in seconds | 
 **status** | **str**| status of dag runs | [optional] 

### Return type

[**List[RangeMetricPerStatus]**](RangeMetricPerStatus.md)

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

# **get_deployments_dag_runs_per_status**
> List[RangeMetricPerStatus] get_deployments_dag_runs_per_status(organization_id, deployment_id, range, step, status=status)

Get DAG runs metrics per status for a deployment

Get DAG runs metrics per status for a deployment

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.range_metric_per_status import RangeMetricPerStatus
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
    api_instance = astronomercoreapi.DeploymentMetricsApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    deployment_id = 'deployment_id_example' # str | deployment ID corresponding to the metrics
    range = 56 # int | range of the DAG runs metrics in seconds
    step = 56 # int | step interval of the DAG runs metrics in seconds
    status = 'status_example' # str | status of dag runs (optional)

    try:
        # Get DAG runs metrics per status for a deployment
        api_response = api_instance.get_deployments_dag_runs_per_status(organization_id, deployment_id, range, step, status=status)
        print("The response of DeploymentMetricsApi->get_deployments_dag_runs_per_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentMetricsApi->get_deployments_dag_runs_per_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **deployment_id** | **str**| deployment ID corresponding to the metrics | 
 **range** | **int**| range of the DAG runs metrics in seconds | 
 **step** | **int**| step interval of the DAG runs metrics in seconds | 
 **status** | **str**| status of dag runs | [optional] 

### Return type

[**List[RangeMetricPerStatus]**](RangeMetricPerStatus.md)

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
**499** |  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployments_task_run_durations_per_status**
> List[RangeMetricPerStatus] get_deployments_task_run_durations_per_status(organization_id, deployment_id, range, step, status=status)

Get task run P90 durations metrics per status for a deployment

Get task run P90 durations metrics per status for a deployment

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.range_metric_per_status import RangeMetricPerStatus
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
    api_instance = astronomercoreapi.DeploymentMetricsApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    deployment_id = 'deployment_id_example' # str | deployment ID corresponding to the metrics
    range = 56 # int | range of the task run durations metrics in seconds
    step = 56 # int | step interval of the task run durations metrics in seconds
    status = 'status_example' # str | status of task runs (optional)

    try:
        # Get task run P90 durations metrics per status for a deployment
        api_response = api_instance.get_deployments_task_run_durations_per_status(organization_id, deployment_id, range, step, status=status)
        print("The response of DeploymentMetricsApi->get_deployments_task_run_durations_per_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentMetricsApi->get_deployments_task_run_durations_per_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **deployment_id** | **str**| deployment ID corresponding to the metrics | 
 **range** | **int**| range of the task run durations metrics in seconds | 
 **step** | **int**| step interval of the task run durations metrics in seconds | 
 **status** | **str**| status of task runs | [optional] 

### Return type

[**List[RangeMetricPerStatus]**](RangeMetricPerStatus.md)

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

# **get_deployments_task_runs_per_status**
> List[RangeMetricPerStatus] get_deployments_task_runs_per_status(organization_id, deployment_id, range, step, status=status)

Get task runs metrics per status for a deployment

Get task runs metrics per status for a deployment

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.range_metric_per_status import RangeMetricPerStatus
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
    api_instance = astronomercoreapi.DeploymentMetricsApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    deployment_id = 'deployment_id_example' # str | deployment ID corresponding to the metrics
    range = 56 # int | range of the task runs metrics in seconds
    step = 56 # int | step interval of the task runs metrics in seconds
    status = 'status_example' # str | status of task runs (optional)

    try:
        # Get task runs metrics per status for a deployment
        api_response = api_instance.get_deployments_task_runs_per_status(organization_id, deployment_id, range, step, status=status)
        print("The response of DeploymentMetricsApi->get_deployments_task_runs_per_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentMetricsApi->get_deployments_task_runs_per_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **deployment_id** | **str**| deployment ID corresponding to the metrics | 
 **range** | **int**| range of the task runs metrics in seconds | 
 **step** | **int**| step interval of the task runs metrics in seconds | 
 **status** | **str**| status of task runs | [optional] 

### Return type

[**List[RangeMetricPerStatus]**](RangeMetricPerStatus.md)

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
**499** |  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pod_count_over_time**
> List[RangeMetricPerComponentAndQueueAndStatus] get_pod_count_over_time(organization_id, deployment_id, range, step)

Get pod count per component and worker queue and status over time

Get pod count per component and worker queue and status over time

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.range_metric_per_component_and_queue_and_status import RangeMetricPerComponentAndQueueAndStatus
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
    api_instance = astronomercoreapi.DeploymentMetricsApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    deployment_id = 'deployment_id_example' # str | deployment ID corresponding to the metrics
    range = 56 # int | range of pod count metrics in seconds
    step = 56 # int | step of pod count metrics in seconds

    try:
        # Get pod count per component and worker queue and status over time
        api_response = api_instance.get_pod_count_over_time(organization_id, deployment_id, range, step)
        print("The response of DeploymentMetricsApi->get_pod_count_over_time:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentMetricsApi->get_pod_count_over_time: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **deployment_id** | **str**| deployment ID corresponding to the metrics | 
 **range** | **int**| range of pod count metrics in seconds | 
 **step** | **int**| step of pod count metrics in seconds | 

### Return type

[**List[RangeMetricPerComponentAndQueueAndStatus]**](RangeMetricPerComponentAndQueueAndStatus.md)

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

# **list_deployments_cpu_usages**
> RangeMetricsPaginated list_deployments_cpu_usages(organization_id, range, step, deployment_ids=deployment_ids, workspace_ids=workspace_ids, offset=offset, limit=limit, sorts=sorts)

List CPU usages metrics for deployments

List CPU usages metrics for deployments

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.range_metrics_paginated import RangeMetricsPaginated
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
    api_instance = astronomercoreapi.DeploymentMetricsApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    range = 56 # int | range of the CPU usages metrics in seconds
    step = 56 # int | step interval of the CPU usages metrics in seconds
    deployment_ids = ['deployment_ids_example'] # List[str] | IDs that define the deployments (optional)
    workspace_ids = ['workspace_ids_example'] # List[str] | IDs that define the workspaces where deployments belong to (optional)
    offset = 0 # int | offset for deployments pagination (optional) (default to 0)
    limit = 20 # int | limit for deployments pagination (optional) (default to 20)
    sorts = ['sorts_example'] # List[str] | sorting criteria for deployments, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc' (optional)

    try:
        # List CPU usages metrics for deployments
        api_response = api_instance.list_deployments_cpu_usages(organization_id, range, step, deployment_ids=deployment_ids, workspace_ids=workspace_ids, offset=offset, limit=limit, sorts=sorts)
        print("The response of DeploymentMetricsApi->list_deployments_cpu_usages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentMetricsApi->list_deployments_cpu_usages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **range** | **int**| range of the CPU usages metrics in seconds | 
 **step** | **int**| step interval of the CPU usages metrics in seconds | 
 **deployment_ids** | [**List[str]**](str.md)| IDs that define the deployments | [optional] 
 **workspace_ids** | [**List[str]**](str.md)| IDs that define the workspaces where deployments belong to | [optional] 
 **offset** | **int**| offset for deployments pagination | [optional] [default to 0]
 **limit** | **int**| limit for deployments pagination | [optional] [default to 20]
 **sorts** | [**List[str]**](str.md)| sorting criteria for deployments, each criterion should conform to format &#39;fieldName:asc&#39; or &#39;fieldName:desc&#39; | [optional] 

### Return type

[**RangeMetricsPaginated**](RangeMetricsPaginated.md)

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

# **list_deployments_dag_runs**
> RangeMetricsPerStatusPaginated list_deployments_dag_runs(organization_id, range, step, deployment_ids=deployment_ids, workspace_ids=workspace_ids, offset=offset, limit=limit, sorts=sorts, status=status)

List DAG runs metrics for deployments

List DAG runs metrics for deployments

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.range_metrics_per_status_paginated import RangeMetricsPerStatusPaginated
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
    api_instance = astronomercoreapi.DeploymentMetricsApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    range = 56 # int | range of the DAG runs metrics in seconds
    step = 56 # int | step interval of the DAG runs metrics in seconds
    deployment_ids = ['deployment_ids_example'] # List[str] | IDs that define the deployments (optional)
    workspace_ids = ['workspace_ids_example'] # List[str] | IDs that define the workspaces where deployments belong to (optional)
    offset = 0 # int | offset for deployments pagination (optional) (default to 0)
    limit = 20 # int | limit for deployments pagination (optional) (default to 20)
    sorts = ['sorts_example'] # List[str] | sorting criteria for deployments, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc' (optional)
    status = 'status_example' # str | status of dag runs (optional)

    try:
        # List DAG runs metrics for deployments
        api_response = api_instance.list_deployments_dag_runs(organization_id, range, step, deployment_ids=deployment_ids, workspace_ids=workspace_ids, offset=offset, limit=limit, sorts=sorts, status=status)
        print("The response of DeploymentMetricsApi->list_deployments_dag_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentMetricsApi->list_deployments_dag_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **range** | **int**| range of the DAG runs metrics in seconds | 
 **step** | **int**| step interval of the DAG runs metrics in seconds | 
 **deployment_ids** | [**List[str]**](str.md)| IDs that define the deployments | [optional] 
 **workspace_ids** | [**List[str]**](str.md)| IDs that define the workspaces where deployments belong to | [optional] 
 **offset** | **int**| offset for deployments pagination | [optional] [default to 0]
 **limit** | **int**| limit for deployments pagination | [optional] [default to 20]
 **sorts** | [**List[str]**](str.md)| sorting criteria for deployments, each criterion should conform to format &#39;fieldName:asc&#39; or &#39;fieldName:desc&#39; | [optional] 
 **status** | **str**| status of dag runs | [optional] 

### Return type

[**RangeMetricsPerStatusPaginated**](RangeMetricsPerStatusPaginated.md)

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
**499** |  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_deployments_dagbag_sizes**
> InstantMetricsPaginated list_deployments_dagbag_sizes(organization_id, deployment_ids=deployment_ids, workspace_ids=workspace_ids, offset=offset, limit=limit, sorts=sorts)

List DAG bag sizes for deployments

List DAG bag sizes for deployments

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.instant_metrics_paginated import InstantMetricsPaginated
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
    api_instance = astronomercoreapi.DeploymentMetricsApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    deployment_ids = ['deployment_ids_example'] # List[str] | IDs that define the deployments (optional)
    workspace_ids = ['workspace_ids_example'] # List[str] | IDs that define the workspaces where deployments belong to (optional)
    offset = 0 # int | offset for deployments pagination (optional) (default to 0)
    limit = 20 # int | limit for deployments pagination (optional) (default to 20)
    sorts = ['sorts_example'] # List[str] | sorting criteria for deployments, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc' (optional)

    try:
        # List DAG bag sizes for deployments
        api_response = api_instance.list_deployments_dagbag_sizes(organization_id, deployment_ids=deployment_ids, workspace_ids=workspace_ids, offset=offset, limit=limit, sorts=sorts)
        print("The response of DeploymentMetricsApi->list_deployments_dagbag_sizes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentMetricsApi->list_deployments_dagbag_sizes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **deployment_ids** | [**List[str]**](str.md)| IDs that define the deployments | [optional] 
 **workspace_ids** | [**List[str]**](str.md)| IDs that define the workspaces where deployments belong to | [optional] 
 **offset** | **int**| offset for deployments pagination | [optional] [default to 0]
 **limit** | **int**| limit for deployments pagination | [optional] [default to 20]
 **sorts** | [**List[str]**](str.md)| sorting criteria for deployments, each criterion should conform to format &#39;fieldName:asc&#39; or &#39;fieldName:desc&#39; | [optional] 

### Return type

[**InstantMetricsPaginated**](InstantMetricsPaginated.md)

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

# **list_deployments_memory_usages**
> RangeMetricsPaginated list_deployments_memory_usages(organization_id, range, step, deployment_ids=deployment_ids, workspace_ids=workspace_ids, offset=offset, limit=limit, sorts=sorts)

List memory usages metrics for deployments

List memory usages metrics for deployments

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.range_metrics_paginated import RangeMetricsPaginated
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
    api_instance = astronomercoreapi.DeploymentMetricsApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    range = 56 # int | range of the memory usages metrics in seconds
    step = 56 # int | step interval of the memory usages metrics in seconds
    deployment_ids = ['deployment_ids_example'] # List[str] | IDs that define the deployments (optional)
    workspace_ids = ['workspace_ids_example'] # List[str] | IDs that define the workspaces where deployments belong to (optional)
    offset = 0 # int | offset for deployments pagination (optional) (default to 0)
    limit = 20 # int | limit for deployments pagination (optional) (default to 20)
    sorts = ['sorts_example'] # List[str] | sorting criteria for deployments, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc' (optional)

    try:
        # List memory usages metrics for deployments
        api_response = api_instance.list_deployments_memory_usages(organization_id, range, step, deployment_ids=deployment_ids, workspace_ids=workspace_ids, offset=offset, limit=limit, sorts=sorts)
        print("The response of DeploymentMetricsApi->list_deployments_memory_usages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentMetricsApi->list_deployments_memory_usages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **range** | **int**| range of the memory usages metrics in seconds | 
 **step** | **int**| step interval of the memory usages metrics in seconds | 
 **deployment_ids** | [**List[str]**](str.md)| IDs that define the deployments | [optional] 
 **workspace_ids** | [**List[str]**](str.md)| IDs that define the workspaces where deployments belong to | [optional] 
 **offset** | **int**| offset for deployments pagination | [optional] [default to 0]
 **limit** | **int**| limit for deployments pagination | [optional] [default to 20]
 **sorts** | [**List[str]**](str.md)| sorting criteria for deployments, each criterion should conform to format &#39;fieldName:asc&#39; or &#39;fieldName:desc&#39; | [optional] 

### Return type

[**RangeMetricsPaginated**](RangeMetricsPaginated.md)

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
**499** |  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_deployments_pod_count_per_status**
> List[InstantMetricPerComponentStatus] list_deployments_pod_count_per_status(organization_id, deployment_id)

Get pod count per status for a deployment

Get pod count per status for a deployment

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.instant_metric_per_component_status import InstantMetricPerComponentStatus
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
    api_instance = astronomercoreapi.DeploymentMetricsApi(api_client)
    organization_id = 'organization_id_example' # str | organization FQN
    deployment_id = 'deployment_id_example' # str | deployment ID corresponding to the metrics

    try:
        # Get pod count per status for a deployment
        api_response = api_instance.list_deployments_pod_count_per_status(organization_id, deployment_id)
        print("The response of DeploymentMetricsApi->list_deployments_pod_count_per_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentMetricsApi->list_deployments_pod_count_per_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization FQN | 
 **deployment_id** | **str**| deployment ID corresponding to the metrics | 

### Return type

[**List[InstantMetricPerComponentStatus]**](InstantMetricPerComponentStatus.md)

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
**499** |  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_deployments_pool_count_per_status**
> List[InstantMetricPerPoolStatus] list_deployments_pool_count_per_status(organization_id, deployment_id)

Get pool count per status for a deployment

Get pool count per status for a deployment

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.instant_metric_per_pool_status import InstantMetricPerPoolStatus
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
    api_instance = astronomercoreapi.DeploymentMetricsApi(api_client)
    organization_id = 'organization_id_example' # str | organization FQN
    deployment_id = 'deployment_id_example' # str | deployment ID corresponding to the metrics

    try:
        # Get pool count per status for a deployment
        api_response = api_instance.list_deployments_pool_count_per_status(organization_id, deployment_id)
        print("The response of DeploymentMetricsApi->list_deployments_pool_count_per_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentMetricsApi->list_deployments_pool_count_per_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization FQN | 
 **deployment_id** | **str**| deployment ID corresponding to the metrics | 

### Return type

[**List[InstantMetricPerPoolStatus]**](InstantMetricPerPoolStatus.md)

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
**499** |  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_deployments_task_runs**
> RangeMetricsPerStatusPaginated list_deployments_task_runs(organization_id, range, step, deployment_ids=deployment_ids, workspace_ids=workspace_ids, offset=offset, limit=limit, sorts=sorts, status=status, include_deleted_deployments=include_deleted_deployments)

List task runs metrics for deployments

List task runs metrics for deployments

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomercoreapi
from astronomercoreapi.models.range_metrics_per_status_paginated import RangeMetricsPerStatusPaginated
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
    api_instance = astronomercoreapi.DeploymentMetricsApi(api_client)
    organization_id = 'organization_id_example' # str | organization ID
    range = 56 # int | range of the task runs metric in seconds
    step = 56 # int | step interval of task runs metric in seconds
    deployment_ids = ['deployment_ids_example'] # List[str] | IDs that define the deployments (optional)
    workspace_ids = ['workspace_ids_example'] # List[str] | IDs that define the workspaces where deployments belong to (optional)
    offset = 0 # int | offset for deployments pagination (optional) (default to 0)
    limit = 20 # int | limit for deployments pagination (optional) (default to 20)
    sorts = ['sorts_example'] # List[str] | sorting criteria for deployments, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc' (optional)
    status = 'status_example' # str | status of task runs (optional)
    include_deleted_deployments = True # bool | results should include data from soft deleted deployments (optional)

    try:
        # List task runs metrics for deployments
        api_response = api_instance.list_deployments_task_runs(organization_id, range, step, deployment_ids=deployment_ids, workspace_ids=workspace_ids, offset=offset, limit=limit, sorts=sorts, status=status, include_deleted_deployments=include_deleted_deployments)
        print("The response of DeploymentMetricsApi->list_deployments_task_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentMetricsApi->list_deployments_task_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| organization ID | 
 **range** | **int**| range of the task runs metric in seconds | 
 **step** | **int**| step interval of task runs metric in seconds | 
 **deployment_ids** | [**List[str]**](str.md)| IDs that define the deployments | [optional] 
 **workspace_ids** | [**List[str]**](str.md)| IDs that define the workspaces where deployments belong to | [optional] 
 **offset** | **int**| offset for deployments pagination | [optional] [default to 0]
 **limit** | **int**| limit for deployments pagination | [optional] [default to 20]
 **sorts** | [**List[str]**](str.md)| sorting criteria for deployments, each criterion should conform to format &#39;fieldName:asc&#39; or &#39;fieldName:desc&#39; | [optional] 
 **status** | **str**| status of task runs | [optional] 
 **include_deleted_deployments** | **bool**| results should include data from soft deleted deployments | [optional] 

### Return type

[**RangeMetricsPerStatusPaginated**](RangeMetricsPerStatusPaginated.md)

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

