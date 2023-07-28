# DagsPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dags** | [**List[Dag]**](Dag.md) |  | 
**filters** | [**DagFilters**](DagFilters.md) |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**total_count** | **int** |  | 

## Example

```python
from astronomerregistry.models.dags_paginated import DagsPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of DagsPaginated from a JSON string
dags_paginated_instance = DagsPaginated.from_json(json)
# print the JSON string representation of the object
print DagsPaginated.to_json()

# convert the object into a dict
dags_paginated_dict = dags_paginated_instance.to_dict()
# create an instance of DagsPaginated from a dict
dags_paginated_form_dict = dags_paginated.from_dict(dags_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


