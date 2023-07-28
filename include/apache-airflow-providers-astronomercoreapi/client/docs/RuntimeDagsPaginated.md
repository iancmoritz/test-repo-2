# RuntimeDagsPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dags** | [**List[RuntimeDag]**](RuntimeDag.md) |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**total_count** | **int** |  | 

## Example

```python
from astronomercoreapi.models.runtime_dags_paginated import RuntimeDagsPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeDagsPaginated from a JSON string
runtime_dags_paginated_instance = RuntimeDagsPaginated.from_json(json)
# print the JSON string representation of the object
print RuntimeDagsPaginated.to_json()

# convert the object into a dict
runtime_dags_paginated_dict = runtime_dags_paginated_instance.to_dict()
# create an instance of RuntimeDagsPaginated from a dict
runtime_dags_paginated_form_dict = runtime_dags_paginated.from_dict(runtime_dags_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


