# Runtime


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_capabilities** | [**RuntimeApiCapabilities**](RuntimeApiCapabilities.md) |  | 
**cluster_id** | **str** |  | 
**created_at** | **datetime** |  | 
**deleted_at** | **datetime** |  | [optional] 
**description** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**organization_id** | **str** |  | 
**release_name** | **str** |  | 
**runtime_version** | **str** |  | [optional] 
**type** | **str** |  | 
**updated_at** | **datetime** |  | 
**workspace_id** | **str** |  | 

## Example

```python
from astronomercoreapi.models.runtime import Runtime

# TODO update the JSON string below
json = "{}"
# create an instance of Runtime from a JSON string
runtime_instance = Runtime.from_json(json)
# print the JSON string representation of the object
print Runtime.to_json()

# convert the object into a dict
runtime_dict = runtime_instance.to_dict()
# create an instance of Runtime from a dict
runtime_form_dict = runtime.from_dict(runtime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


