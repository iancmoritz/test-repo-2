# DagRunsPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_runs** | [**List[DagRun]**](DagRun.md) |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**total_count** | **int** |  | 

## Example

```python
from astronomercoreapi.models.dag_runs_paginated import DagRunsPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of DagRunsPaginated from a JSON string
dag_runs_paginated_instance = DagRunsPaginated.from_json(json)
# print the JSON string representation of the object
print DagRunsPaginated.to_json()

# convert the object into a dict
dag_runs_paginated_dict = dag_runs_paginated_instance.to_dict()
# create an instance of DagRunsPaginated from a dict
dag_runs_paginated_form_dict = dag_runs_paginated.from_dict(dag_runs_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


