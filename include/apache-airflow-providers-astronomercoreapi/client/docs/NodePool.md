# NodePool


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_provider** | **str** |  | 
**cluster_id** | **str** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**is_default** | **bool** |  | 
**max_node_count** | **int** |  | 
**name** | **str** |  | 
**node_instance_type** | **str** |  | 
**supported_astro_machines** | **List[str]** |  | [optional] 
**updated_at** | **datetime** |  | 

## Example

```python
from astronomercoreapi.models.node_pool import NodePool

# TODO update the JSON string below
json = "{}"
# create an instance of NodePool from a JSON string
node_pool_instance = NodePool.from_json(json)
# print the JSON string representation of the object
print NodePool.to_json()

# convert the object into a dict
node_pool_dict = node_pool_instance.to_dict()
# create an instance of NodePool from a dict
node_pool_form_dict = node_pool.from_dict(node_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


