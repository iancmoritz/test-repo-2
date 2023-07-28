# CreateGcpClusterRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_instance_type** | **str** |  | 
**is_dry_run** | **bool** |  | [optional] 
**k8s_tags** | [**List[ClusterTag]**](ClusterTag.md) |  | [optional] 
**name** | **str** |  | 
**node_pools** | [**List[CreateNodePoolRequest]**](CreateNodePoolRequest.md) |  | [optional] 
**pod_subnet_range** | **str** |  | 
**provider_account** | **str** |  | [optional] 
**region** | **str** |  | 
**service_peering_range** | **str** |  | 
**service_subnet_range** | **str** |  | 
**template_version** | **str** |  | 
**type** | **str** |  | 
**vpc_subnet_range** | **str** |  | 

## Example

```python
from astronomercoreapi.models.create_gcp_cluster_request import CreateGcpClusterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGcpClusterRequest from a JSON string
create_gcp_cluster_request_instance = CreateGcpClusterRequest.from_json(json)
# print the JSON string representation of the object
print CreateGcpClusterRequest.to_json()

# convert the object into a dict
create_gcp_cluster_request_dict = create_gcp_cluster_request_instance.to_dict()
# create an instance of CreateGcpClusterRequest from a dict
create_gcp_cluster_request_form_dict = create_gcp_cluster_request.from_dict(create_gcp_cluster_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


