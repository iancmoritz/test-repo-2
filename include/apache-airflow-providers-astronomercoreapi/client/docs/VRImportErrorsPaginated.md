# VRImportErrorsPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_errors** | [**List[VirtualRuntimeImportError]**](VirtualRuntimeImportError.md) |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**total_count** | **int** |  | 

## Example

```python
from astronomercoreapi.models.vr_import_errors_paginated import VRImportErrorsPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of VRImportErrorsPaginated from a JSON string
vr_import_errors_paginated_instance = VRImportErrorsPaginated.from_json(json)
# print the JSON string representation of the object
print VRImportErrorsPaginated.to_json()

# convert the object into a dict
vr_import_errors_paginated_dict = vr_import_errors_paginated_instance.to_dict()
# create an instance of VRImportErrorsPaginated from a dict
vr_import_errors_paginated_form_dict = vr_import_errors_paginated.from_dict(vr_import_errors_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


