# ListApiTokensPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_tokens** | [**List[ApiToken]**](ApiToken.md) |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**total_count** | **int** |  | 

## Example

```python
from astronomercoreapi.models.list_api_tokens_paginated import ListApiTokensPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of ListApiTokensPaginated from a JSON string
list_api_tokens_paginated_instance = ListApiTokensPaginated.from_json(json)
# print the JSON string representation of the object
print ListApiTokensPaginated.to_json()

# convert the object into a dict
list_api_tokens_paginated_dict = list_api_tokens_paginated_instance.to_dict()
# create an instance of ListApiTokensPaginated from a dict
list_api_tokens_paginated_form_dict = list_api_tokens_paginated.from_dict(list_api_tokens_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


