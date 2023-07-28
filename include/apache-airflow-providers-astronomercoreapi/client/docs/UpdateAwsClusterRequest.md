# UpdateAwsClusterRequest


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
from astronomercoreapi.models.update_aws_cluster_request import UpdateAwsClusterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAwsClusterRequest from a JSON string
update_aws_cluster_request_instance = UpdateAwsClusterRequest.from_json(json)
# print the JSON string representation of the object
print UpdateAwsClusterRequest.to_json()

# convert the object into a dict
update_aws_cluster_request_dict = update_aws_cluster_request_instance.to_dict()
# create an instance of UpdateAwsClusterRequest from a dict
update_aws_cluster_request_form_dict = update_aws_cluster_request.from_dict(update_aws_cluster_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


