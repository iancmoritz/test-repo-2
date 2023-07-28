# Cluster


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied_template_version** | **str** |  | 
**cloud_provider** | **str** |  | 
**created_at** | **datetime** |  | 
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
**organization_id** | **str** |  | 
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
**vpc_subnet_range** | **str** |  | 
**workspaces** | **List[str]** |  | 

## Example

```python
from astronomercoreapi.models.cluster import Cluster

# TODO update the JSON string below
json = "{}"
# create an instance of Cluster from a JSON string
cluster_instance = Cluster.from_json(json)
# print the JSON string representation of the object
print Cluster.to_json()

# convert the object into a dict
cluster_dict = cluster_instance.to_dict()
# create an instance of Cluster from a dict
cluster_form_dict = cluster.from_dict(cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


