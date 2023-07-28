# VirtualRuntime


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_image** | **str** |  | [optional] 
**cluster_id** | **str** |  | [optional] 
**connections** | [**List[Connection]**](Connection.md) |  | [optional] 
**created_at** | **datetime** |  | 
**created_by_user** | [**BasicSubjectProfile**](BasicSubjectProfile.md) |  | 
**deleted_at** | **datetime** |  | [optional] 
**description** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**organization_id** | **str** |  | [optional] 
**organization_name** | **str** |  | [optional] 
**organization_short_name** | **str** |  | [optional] 
**release_name** | **str** |  | 
**requirements** | **List[str]** |  | [optional] 
**requirements_validate_status** | **str** |  | [optional] 
**runtime_version** | **str** |  | [optional] 
**task_mem_gib** | **float** |  | 
**updated_at** | **datetime** |  | 
**updated_by_user** | [**BasicSubjectProfile**](BasicSubjectProfile.md) |  | 
**variables** | [**List[VRVariable]**](VRVariable.md) |  | [optional] 
**web_server_ingress_hostname** | **str** |  | [optional] 
**web_server_url** | **str** |  | [optional] 
**workspace_id** | **str** |  | 
**workspace_name** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.virtual_runtime import VirtualRuntime

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualRuntime from a JSON string
virtual_runtime_instance = VirtualRuntime.from_json(json)
# print the JSON string representation of the object
print VirtualRuntime.to_json()

# convert the object into a dict
virtual_runtime_dict = virtual_runtime_instance.to_dict()
# create an instance of VirtualRuntime from a dict
virtual_runtime_form_dict = virtual_runtime.from_dict(virtual_runtime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


