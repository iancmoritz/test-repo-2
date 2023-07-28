# RuntimeImportErrorsPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_errors** | [**List[RuntimeImportError]**](RuntimeImportError.md) |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**total_count** | **int** |  | 

## Example

```python
from astronomercoreapi.models.runtime_import_errors_paginated import RuntimeImportErrorsPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeImportErrorsPaginated from a JSON string
runtime_import_errors_paginated_instance = RuntimeImportErrorsPaginated.from_json(json)
# print the JSON string representation of the object
print RuntimeImportErrorsPaginated.to_json()

# convert the object into a dict
runtime_import_errors_paginated_dict = runtime_import_errors_paginated_instance.to_dict()
# create an instance of RuntimeImportErrorsPaginated from a dict
runtime_import_errors_paginated_form_dict = runtime_import_errors_paginated.from_dict(runtime_import_errors_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


