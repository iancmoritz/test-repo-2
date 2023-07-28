# CreateNodePoolRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_default** | **bool** |  | 
**max_node_count** | **int** |  | 
**name** | **str** |  | 
**node_instance_type** | **str** |  | 

## Example

```python
from astronomercoreapi.models.create_node_pool_request import CreateNodePoolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNodePoolRequest from a JSON string
create_node_pool_request_instance = CreateNodePoolRequest.from_json(json)
# print the JSON string representation of the object
print CreateNodePoolRequest.to_json()

# convert the object into a dict
create_node_pool_request_dict = create_node_pool_request_instance.to_dict()
# create an instance of CreateNodePoolRequest from a dict
create_node_pool_request_form_dict = create_node_pool_request.from_dict(create_node_pool_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


