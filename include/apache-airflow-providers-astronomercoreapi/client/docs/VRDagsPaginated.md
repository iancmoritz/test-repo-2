# VRDagsPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dags** | [**List[VirtualRuntimeDag]**](VirtualRuntimeDag.md) |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**total_count** | **int** |  | 

## Example

```python
from astronomercoreapi.models.vr_dags_paginated import VRDagsPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of VRDagsPaginated from a JSON string
vr_dags_paginated_instance = VRDagsPaginated.from_json(json)
# print the JSON string representation of the object
print VRDagsPaginated.to_json()

# convert the object into a dict
vr_dags_paginated_dict = vr_dags_paginated_instance.to_dict()
# create an instance of VRDagsPaginated from a dict
vr_dags_paginated_form_dict = vr_dags_paginated.from_dict(vr_dags_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


