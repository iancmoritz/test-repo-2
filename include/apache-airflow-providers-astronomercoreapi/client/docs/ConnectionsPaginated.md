# ConnectionsPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connections** | [**List[Connection]**](Connection.md) |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**total_count** | **int** |  | 

## Example

```python
from astronomercoreapi.models.connections_paginated import ConnectionsPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionsPaginated from a JSON string
connections_paginated_instance = ConnectionsPaginated.from_json(json)
# print the JSON string representation of the object
print ConnectionsPaginated.to_json()

# convert the object into a dict
connections_paginated_dict = connections_paginated_instance.to_dict()
# create an instance of ConnectionsPaginated from a dict
connections_paginated_form_dict = connections_paginated.from_dict(connections_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


