# UpdateGcpClusterRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_instance_type** | **str** |  | 
**k8s_tags** | [**List[ClusterTag]**](ClusterTag.md) |  | 
**name** | **str** |  | 
**node_pools** | [**List[UpdateNodePoolRequest]**](UpdateNodePoolRequest.md) |  | 
**template_version** | **str** |  | 

## Example

```python
from astronomercoreapi.models.update_gcp_cluster_request import UpdateGcpClusterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGcpClusterRequest from a JSON string
update_gcp_cluster_request_instance = UpdateGcpClusterRequest.from_json(json)
# print the JSON string representation of the object
print UpdateGcpClusterRequest.to_json()

# convert the object into a dict
update_gcp_cluster_request_dict = update_gcp_cluster_request_instance.to_dict()
# create an instance of UpdateGcpClusterRequest from a dict
update_gcp_cluster_request_form_dict = update_gcp_cluster_request.from_dict(update_gcp_cluster_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


