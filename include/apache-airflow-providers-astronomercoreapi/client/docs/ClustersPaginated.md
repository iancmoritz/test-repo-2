# ClustersPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**List[Cluster]**](Cluster.md) |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**total_count** | **int** |  | 

## Example

```python
from astronomercoreapi.models.clusters_paginated import ClustersPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of ClustersPaginated from a JSON string
clusters_paginated_instance = ClustersPaginated.from_json(json)
# print the JSON string representation of the object
print ClustersPaginated.to_json()

# convert the object into a dict
clusters_paginated_dict = clusters_paginated_instance.to_dict()
# create an instance of ClustersPaginated from a dict
clusters_paginated_form_dict = clusters_paginated.from_dict(clusters_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


