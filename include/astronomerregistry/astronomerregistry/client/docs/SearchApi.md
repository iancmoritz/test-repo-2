# astronomerregistry.SearchApi

All URIs are relative to *https://api.astronomer.io/registryV2/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](SearchApi.md#search) | **POST** /organizations/{orgShortNameId}/search | Search for a registry object


# **search**
> RegistrySearch search(org_short_name_id, body, is_certified=is_certified, is_featured=is_featured, is_global=is_global, is_private=is_private, is_cloud_ide_compatible=is_cloud_ide_compatible, offset=offset, limit=limit, sorts=sorts)

Search for a registry object

Search for a registry object

### Example

```python
import time
import os
import astronomerregistry
from astronomerregistry.models.registry_search import RegistrySearch
from astronomerregistry.models.registry_search_request import RegistrySearchRequest
from astronomerregistry.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astronomer.io/registryV2/v1alpha1
# See configuration.py for a list of all supported configuration parameters.
configuration = astronomerregistry.Configuration(
    host = "https://api.astronomer.io/registryV2/v1alpha1"
)


# Enter a context with an instance of the API client
with astronomerregistry.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astronomerregistry.SearchApi(api_client)
    org_short_name_id = 'org_short_name_id_example' # str | organization FQN
    body = astronomerregistry.RegistrySearchRequest() # RegistrySearchRequest | request body for a registry search
    is_certified = True # bool | return only certified providers (optional)
    is_featured = True # bool | return only featured providers (optional)
    is_global = True # bool | return only global providers (optional)
    is_private = True # bool | return only private providers (optional)
    is_cloud_ide_compatible = True # bool | return only cloud ide compatible providers (optional)
    offset = 0 # int | offset for pagination (optional) (default to 0)
    limit = 20 # int | limit for pagination (optional) (default to 20)
    sorts = ['sorts_example'] # List[str] | sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc'. Default to searchRank:asc (optional)

    try:
        # Search for a registry object
        api_response = api_instance.search(org_short_name_id, body, is_certified=is_certified, is_featured=is_featured, is_global=is_global, is_private=is_private, is_cloud_ide_compatible=is_cloud_ide_compatible, offset=offset, limit=limit, sorts=sorts)
        print("The response of SearchApi->search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_short_name_id** | **str**| organization FQN | 
 **body** | [**RegistrySearchRequest**](RegistrySearchRequest.md)| request body for a registry search | 
 **is_certified** | **bool**| return only certified providers | [optional] 
 **is_featured** | **bool**| return only featured providers | [optional] 
 **is_global** | **bool**| return only global providers | [optional] 
 **is_private** | **bool**| return only private providers | [optional] 
 **is_cloud_ide_compatible** | **bool**| return only cloud ide compatible providers | [optional] 
 **offset** | **int**| offset for pagination | [optional] [default to 0]
 **limit** | **int**| limit for pagination | [optional] [default to 20]
 **sorts** | [**List[str]**](str.md)| sorting criteria, each criterion should conform to format &#39;fieldName:asc&#39; or &#39;fieldName:desc&#39;. Default to searchRank:asc | [optional] 

### Return type

[**RegistrySearch**](RegistrySearch.md)

### Authorization

No authorization required

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

