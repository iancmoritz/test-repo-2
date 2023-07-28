# CreateAwsClusterRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_instance_type** | **str** |  | 
**is_dry_run** | **bool** |  | [optional] 
**k8s_tags** | [**List[ClusterTag]**](ClusterTag.md) |  | [optional] 
**name** | **str** |  | 
**node_pools** | [**List[CreateNodePoolRequest]**](CreateNodePoolRequest.md) |  | [optional] 
**provider_account** | **str** |  | [optional] 
**region** | **str** |  | 
**template_version** | **str** |  | 
**type** | **str** |  | 
**vpc_subnet_range** | **str** |  | 

## Example

```python
from astronomercoreapi.models.create_aws_cluster_request import CreateAwsClusterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAwsClusterRequest from a JSON string
create_aws_cluster_request_instance = CreateAwsClusterRequest.from_json(json)
# print the JSON string representation of the object
print CreateAwsClusterRequest.to_json()

# convert the object into a dict
create_aws_cluster_request_dict = create_aws_cluster_request_instance.to_dict()
# create an instance of CreateAwsClusterRequest from a dict
create_aws_cluster_request_form_dict = create_aws_cluster_request.from_dict(create_aws_cluster_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


