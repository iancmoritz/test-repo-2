# ModulesPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**ModuleFilters**](ModuleFilters.md) |  | 
**limit** | **int** |  | 
**modules** | [**List[Module]**](Module.md) |  | 
**offset** | **int** |  | 
**total_count** | **int** |  | 

## Example

```python
from astronomerregistry.models.modules_paginated import ModulesPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of ModulesPaginated from a JSON string
modules_paginated_instance = ModulesPaginated.from_json(json)
# print the JSON string representation of the object
print ModulesPaginated.to_json()

# convert the object into a dict
modules_paginated_dict = modules_paginated_instance.to_dict()
# create an instance of ModulesPaginated from a dict
modules_paginated_form_dict = modules_paginated.from_dict(modules_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


