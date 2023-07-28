# UpdateNodePoolRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**is_default** | **bool** |  | 
**max_node_count** | **int** |  | 
**name** | **str** |  | 
**node_instance_type** | **str** |  | 

## Example

```python
from astronomercoreapi.models.update_node_pool_request import UpdateNodePoolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNodePoolRequest from a JSON string
update_node_pool_request_instance = UpdateNodePoolRequest.from_json(json)
# print the JSON string representation of the object
print UpdateNodePoolRequest.to_json()

# convert the object into a dict
update_node_pool_request_dict = update_node_pool_request_instance.to_dict()
# create an instance of UpdateNodePoolRequest from a dict
update_node_pool_request_form_dict = update_node_pool_request.from_dict(update_node_pool_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


