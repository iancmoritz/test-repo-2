# VirtualRuntimesPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | 
**offset** | **int** |  | 
**total_count** | **int** |  | 
**virtual_runtimes** | [**List[VirtualRuntime]**](VirtualRuntime.md) |  | 

## Example

```python
from astronomercoreapi.models.virtual_runtimes_paginated import VirtualRuntimesPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualRuntimesPaginated from a JSON string
virtual_runtimes_paginated_instance = VirtualRuntimesPaginated.from_json(json)
# print the JSON string representation of the object
print VirtualRuntimesPaginated.to_json()

# convert the object into a dict
virtual_runtimes_paginated_dict = virtual_runtimes_paginated_instance.to_dict()
# create an instance of VirtualRuntimesPaginated from a dict
virtual_runtimes_paginated_form_dict = virtual_runtimes_paginated.from_dict(virtual_runtimes_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


