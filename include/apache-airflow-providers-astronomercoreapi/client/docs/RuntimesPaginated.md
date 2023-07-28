# RuntimesPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | 
**offset** | **int** |  | 
**runtimes** | [**List[Runtime]**](Runtime.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from astronomercoreapi.models.runtimes_paginated import RuntimesPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimesPaginated from a JSON string
runtimes_paginated_instance = RuntimesPaginated.from_json(json)
# print the JSON string representation of the object
print RuntimesPaginated.to_json()

# convert the object into a dict
runtimes_paginated_dict = runtimes_paginated_instance.to_dict()
# create an instance of RuntimesPaginated from a dict
runtimes_paginated_form_dict = runtimes_paginated.from_dict(runtimes_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


