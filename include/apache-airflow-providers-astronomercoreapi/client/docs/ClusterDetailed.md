# ClusterDetailed


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied_template_version** | **str** |  | 
**cloud_provider** | **str** |  | 
**created_at** | **datetime** |  | 
**created_by** | [**BasicSubjectProfile**](BasicSubjectProfile.md) |  | 
**db_instance_type** | **str** |  | 
**deleted_at** | **str** |  | [optional] 
**id** | **str** |  | 
**is_cordoned** | **bool** |  | [optional] 
**is_dry_run** | **bool** |  | 
**is_limited** | **bool** |  | 
**k8s_tags** | [**List[ClusterTag]**](ClusterTag.md) |  | 
**metadata** | [**ClusterMetadata**](ClusterMetadata.md) |  | 
**name** | **str** |  | 
**node_pools** | [**List[NodePool]**](NodePool.md) |  | 
**org_short_name** | **str** | Deprecated: orgShortName has been replaced with organizationShortName | [optional] 
**organization_id** | **str** |  | 
**organization_name** | **str** |  | 
**organization_short_name** | **str** |  | 
**organization_support_plan** | **str** |  | 
**organization_trial_expires_at** | **str** |  | [optional] 
**pod_subnet_range** | **str** |  | 
**provider_account** | **str** |  | 
**region** | **str** |  | 
**service_peering_range** | **str** |  | 
**service_subnet_range** | **str** |  | 
**status** | **str** |  | 
**template_url** | **str** |  | 
**template_version** | **str** |  | 
**temporal_run_id** | **str** |  | 
**tenant_id** | **str** |  | 
**type** | **str** |  | 
**updated_at** | **datetime** |  | 
**updated_by** | [**BasicSubjectProfile**](BasicSubjectProfile.md) |  | 
**vpc_subnet_range** | **str** |  | 
**workspaces** | **List[str]** |  | 

## Example

```python
from astronomercoreapi.models.cluster_detailed import ClusterDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDetailed from a JSON string
cluster_detailed_instance = ClusterDetailed.from_json(json)
# print the JSON string representation of the object
print ClusterDetailed.to_json()

# convert the object into a dict
cluster_detailed_dict = cluster_detailed_instance.to_dict()
# create an instance of ClusterDetailed from a dict
cluster_detailed_form_dict = cluster_detailed.from_dict(cluster_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


