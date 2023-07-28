# SharedCluster


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_provider** | **str** |  | 
**created_at** | **datetime** |  | 
**db_instance_type** | **str** |  | 
**id** | **str** |  | 
**is_cordoned** | **bool** |  | [optional] 
**is_dry_run** | **bool** |  | 
**metadata** | [**ClusterMetadata**](ClusterMetadata.md) |  | 
**name** | **str** |  | 
**pod_subnet_range** | **str** |  | 
**region** | **str** |  | 
**service_peering_range** | **str** |  | 
**service_subnet_range** | **str** |  | 
**status** | **str** |  | 
**template_version** | **str** |  | 
**updated_at** | **datetime** |  | 
**vpc_subnet_range** | **str** |  | 

## Example

```python
from astronomercoreapi.models.shared_cluster import SharedCluster

# TODO update the JSON string below
json = "{}"
# create an instance of SharedCluster from a JSON string
shared_cluster_instance = SharedCluster.from_json(json)
# print the JSON string representation of the object
print SharedCluster.to_json()

# convert the object into a dict
shared_cluster_dict = shared_cluster_instance.to_dict()
# create an instance of SharedCluster from a dict
shared_cluster_form_dict = shared_cluster.from_dict(shared_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


