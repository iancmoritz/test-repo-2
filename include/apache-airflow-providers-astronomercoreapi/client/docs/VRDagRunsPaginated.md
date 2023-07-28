# VRDagRunsPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_runs** | [**List[VirtualRuntimeDagRun]**](VirtualRuntimeDagRun.md) |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**total_count** | **int** |  | 

## Example

```python
from astronomercoreapi.models.vr_dag_runs_paginated import VRDagRunsPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of VRDagRunsPaginated from a JSON string
vr_dag_runs_paginated_instance = VRDagRunsPaginated.from_json(json)
# print the JSON string representation of the object
print VRDagRunsPaginated.to_json()

# convert the object into a dict
vr_dag_runs_paginated_dict = vr_dag_runs_paginated_instance.to_dict()
# create an instance of VRDagRunsPaginated from a dict
vr_dag_runs_paginated_form_dict = vr_dag_runs_paginated.from_dict(vr_dag_runs_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


