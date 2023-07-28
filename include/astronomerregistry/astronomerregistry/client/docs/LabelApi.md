# astronomerregistry.LabelApi

All URIs are relative to *https://api.astronomer.io/registryV2/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_label**](LabelApi.md#create_label) | **POST** /organizations/{orgShortNameId}/labels/{labelGroup} | Create label for registry
[**delete_label**](LabelApi.md#delete_label) | **DELETE** /organizations/{orgShortNameId}/labels/{labelGroup}/{labelName} | Delete a label
[**get_label**](LabelApi.md#get_label) | **GET** /organizations/{orgShortNameId}/labels/{labelGroup}/{labelName} | Get a label
[**list_labels**](LabelApi.md#list_labels) | **GET** /organizations/{orgShortNameId}/labels/{labelGroup} | List labels
[**update_label**](LabelApi.md#update_label) | **PUT** /organizations/{orgShortNameId}/labels/{labelGroup}/{labelName} | Update label for registry


# **create_label**
> Label create_label(org_short_name_id, label_group, body)

Create label for registry

Create label for registry

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomerregistry
from astronomerregistry.models.create_label_request import CreateLabelRequest
from astronomerregistry.models.label import Label
from astronomerregistry.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astronomer.io/registryV2/v1alpha1
# See configuration.py for a list of all supported configuration parameters.
configuration = astronomerregistry.Configuration(
    host = "https://api.astronomer.io/registryV2/v1alpha1"
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
with astronomerregistry.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astronomerregistry.LabelApi(api_client)
    org_short_name_id = 'org_short_name_id_example' # str | organization FQN
    label_group = 'label_group_example' # str | Group name of the label
    body = astronomerregistry.CreateLabelRequest() # CreateLabelRequest | request body for creating a registry label

    try:
        # Create label for registry
        api_response = api_instance.create_label(org_short_name_id, label_group, body)
        print("The response of LabelApi->create_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelApi->create_label: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_short_name_id** | **str**| organization FQN | 
 **label_group** | **str**| Group name of the label | 
 **body** | [**CreateLabelRequest**](CreateLabelRequest.md)| request body for creating a registry label | 

### Return type

[**Label**](Label.md)

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

# **delete_label**
> Label delete_label(org_short_name_id, label_group, label_name)

Delete a label

Delete a single label by name and version

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomerregistry
from astronomerregistry.models.label import Label
from astronomerregistry.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astronomer.io/registryV2/v1alpha1
# See configuration.py for a list of all supported configuration parameters.
configuration = astronomerregistry.Configuration(
    host = "https://api.astronomer.io/registryV2/v1alpha1"
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
with astronomerregistry.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astronomerregistry.LabelApi(api_client)
    org_short_name_id = 'org_short_name_id_example' # str | organization FQN
    label_group = 'label_group_example' # str | Group name of the label
    label_name = 'label_name_example' # str | The name of the label

    try:
        # Delete a label
        api_response = api_instance.delete_label(org_short_name_id, label_group, label_name)
        print("The response of LabelApi->delete_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelApi->delete_label: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_short_name_id** | **str**| organization FQN | 
 **label_group** | **str**| Group name of the label | 
 **label_name** | **str**| The name of the label | 

### Return type

[**Label**](Label.md)

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

# **get_label**
> Label get_label(org_short_name_id, label_group, label_name)

Get a label

Get a single label by name and orgId

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomerregistry
from astronomerregistry.models.label import Label
from astronomerregistry.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astronomer.io/registryV2/v1alpha1
# See configuration.py for a list of all supported configuration parameters.
configuration = astronomerregistry.Configuration(
    host = "https://api.astronomer.io/registryV2/v1alpha1"
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
with astronomerregistry.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astronomerregistry.LabelApi(api_client)
    org_short_name_id = 'org_short_name_id_example' # str | organization FQN
    label_group = 'label_group_example' # str | Group name of the label
    label_name = 'label_name_example' # str | The name of the label

    try:
        # Get a label
        api_response = api_instance.get_label(org_short_name_id, label_group, label_name)
        print("The response of LabelApi->get_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelApi->get_label: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_short_name_id** | **str**| organization FQN | 
 **label_group** | **str**| Group name of the label | 
 **label_name** | **str**| The name of the label | 

### Return type

[**Label**](Label.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_labels**
> LabelsPaginated list_labels(org_short_name_id, label_group, offset=offset, limit=limit, sorts=sorts)

List labels

List labels

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomerregistry
from astronomerregistry.models.labels_paginated import LabelsPaginated
from astronomerregistry.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astronomer.io/registryV2/v1alpha1
# See configuration.py for a list of all supported configuration parameters.
configuration = astronomerregistry.Configuration(
    host = "https://api.astronomer.io/registryV2/v1alpha1"
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
with astronomerregistry.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astronomerregistry.LabelApi(api_client)
    org_short_name_id = 'org_short_name_id_example' # str | organization FQN
    label_group = 'label_group_example' # str | Group name of the labels
    offset = 0 # int | offset for pagination (optional) (default to 0)
    limit = 20 # int | limit for pagination (optional) (default to 20)
    sorts = ['sorts_example'] # List[str] | sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc' (optional)

    try:
        # List labels
        api_response = api_instance.list_labels(org_short_name_id, label_group, offset=offset, limit=limit, sorts=sorts)
        print("The response of LabelApi->list_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelApi->list_labels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_short_name_id** | **str**| organization FQN | 
 **label_group** | **str**| Group name of the labels | 
 **offset** | **int**| offset for pagination | [optional] [default to 0]
 **limit** | **int**| limit for pagination | [optional] [default to 20]
 **sorts** | [**List[str]**](str.md)| sorting criteria, each criterion should conform to format &#39;fieldName:asc&#39; or &#39;fieldName:desc&#39; | [optional] 

### Return type

[**LabelsPaginated**](LabelsPaginated.md)

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

# **update_label**
> Label update_label(org_short_name_id, label_group, label_name, body)

Update label for registry

Update label for registry

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import astronomerregistry
from astronomerregistry.models.label import Label
from astronomerregistry.models.update_label_request import UpdateLabelRequest
from astronomerregistry.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astronomer.io/registryV2/v1alpha1
# See configuration.py for a list of all supported configuration parameters.
configuration = astronomerregistry.Configuration(
    host = "https://api.astronomer.io/registryV2/v1alpha1"
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
with astronomerregistry.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astronomerregistry.LabelApi(api_client)
    org_short_name_id = 'org_short_name_id_example' # str | organization FQN
    label_group = 'label_group_example' # str | Group name of the label
    label_name = 'label_name_example' # str | The name of the label
    body = astronomerregistry.UpdateLabelRequest() # UpdateLabelRequest | request body for updating a registry label

    try:
        # Update label for registry
        api_response = api_instance.update_label(org_short_name_id, label_group, label_name, body)
        print("The response of LabelApi->update_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelApi->update_label: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_short_name_id** | **str**| organization FQN | 
 **label_group** | **str**| Group name of the label | 
 **label_name** | **str**| The name of the label | 
 **body** | [**UpdateLabelRequest**](UpdateLabelRequest.md)| request body for updating a registry label | 

### Return type

[**Label**](Label.md)

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

