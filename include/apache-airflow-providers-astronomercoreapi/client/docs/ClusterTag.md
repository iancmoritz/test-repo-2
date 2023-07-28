# ClusterTag


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.cluster_tag import ClusterTag

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterTag from a JSON string
cluster_tag_instance = ClusterTag.from_json(json)
# print the JSON string representation of the object
print ClusterTag.to_json()

# convert the object into a dict
cluster_tag_dict = cluster_tag_instance.to_dict()
# create an instance of ClusterTag from a dict
cluster_tag_form_dict = cluster_tag.from_dict(cluster_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


