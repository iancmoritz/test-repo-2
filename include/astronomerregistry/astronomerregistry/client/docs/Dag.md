# Dag


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badges** | [**List[ShortLabel]**](ShortLabel.md) |  | 
**categories** | [**List[ShortLabel]**](ShortLabel.md) |  | 
**created_at** | **str** |  | 
**created_by** | **str** |  | 
**description** | **str** |  | 
**display_name** | **str** |  | 
**documentation** | **str** |  | 
**file_path** | **str** |  | 
**github_raw_dockerfile_url** | **str** |  | 
**github_raw_requirements_url** | **str** |  | 
**github_raw_source_url** | **str** |  | 
**github_repository_url** | **str** |  | 
**github_source_url** | **str** |  | 
**is_certified** | **bool** |  | 
**is_cloud_ide_compatible** | **bool** |  | 
**is_display_name_manual** | **bool** |  | 
**is_featured** | **bool** |  | 
**is_global** | **bool** |  | 
**is_latest_version** | **bool** |  | 
**is_logo_manual** | **bool** |  | 
**is_private** | **bool** |  | 
**logo** | **str** |  | 
**modules** | [**List[ShortModule]**](ShortModule.md) |  | 
**name** | **str** |  | 
**organization_id** | **str** |  | 
**other_versions** | **List[str]** |  | 
**providers** | [**List[ShortProvider]**](ShortProvider.md) |  | 
**repository_name** | **str** |  | 
**repository_owner** | **str** |  | 
**search_id** | **str** |  | 
**search_rank** | **int** |  | [optional] 
**short_name_id** | **str** |  | 
**social_stats** | [**SocialStats**](SocialStats.md) |  | 
**task_dependency_tree** | [**List[TaskDependencyTree]**](TaskDependencyTree.md) |  | 
**tiers** | [**List[ShortLabel]**](ShortLabel.md) |  | 
**type** | **str** |  | 
**updated_at** | **str** |  | 
**updated_by** | **str** |  | 
**version** | **str** |  | 

## Example

```python
from astronomerregistry.models.dag import Dag

# TODO update the JSON string below
json = "{}"
# create an instance of Dag from a JSON string
dag_instance = Dag.from_json(json)
# print the JSON string representation of the object
print Dag.to_json()

# convert the object into a dict
dag_dict = dag_instance.to_dict()
# create an instance of Dag from a dict
dag_form_dict = dag.from_dict(dag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


