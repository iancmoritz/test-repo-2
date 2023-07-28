# UpdateDagRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**display_name** | **str** | Name                     string               &#x60;json:\&quot;name\&quot; validate:\&quot;required\&quot;&#x60; Version                  string               &#x60;json:\&quot;version\&quot; validate:\&quot;required\&quot;&#x60; | [optional] 
**documentation** | **str** |  | [optional] 
**file_path** | **str** |  | [optional] 
**github_raw_dockerfile_url** | **str** |  | [optional] 
**github_raw_requirements_url** | **str** |  | [optional] 
**github_raw_source_url** | **str** |  | [optional] 
**github_repository_url** | **str** |  | [optional] 
**github_source_url** | **str** |  | [optional] 
**is_certified** | **bool** |  | [optional] 
**is_cloud_ide_compatible** | **bool** |  | [optional] 
**is_display_name_manual** | **bool** |  | [optional] 
**is_featured** | **bool** |  | [optional] 
**is_global** | **bool** |  | [optional] 
**is_logo_manual** | **bool** |  | [optional] 
**is_private** | **bool** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**logo** | **str** |  | [optional] 
**related_modules** | [**List[RelatedModuleRequest]**](RelatedModuleRequest.md) |  | [optional] 
**repository_name** | **str** |  | [optional] 
**repository_owner** | **str** |  | [optional] 
**social_stats** | [**SocialStats**](SocialStats.md) |  | [optional] 
**task_dependency_tree** | [**List[TaskDependencyTree]**](TaskDependencyTree.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from astronomerregistry.models.update_dag_request import UpdateDagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDagRequest from a JSON string
update_dag_request_instance = UpdateDagRequest.from_json(json)
# print the JSON string representation of the object
print UpdateDagRequest.to_json()

# convert the object into a dict
update_dag_request_dict = update_dag_request_instance.to_dict()
# create an instance of UpdateDagRequest from a dict
update_dag_request_form_dict = update_dag_request.from_dict(update_dag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


