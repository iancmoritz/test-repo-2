# ProvidersPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**ProviderFilters**](ProviderFilters.md) |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**providers** | [**List[Provider]**](Provider.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from astronomerregistry.models.providers_paginated import ProvidersPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of ProvidersPaginated from a JSON string
providers_paginated_instance = ProvidersPaginated.from_json(json)
# print the JSON string representation of the object
print ProvidersPaginated.to_json()

# convert the object into a dict
providers_paginated_dict = providers_paginated_instance.to_dict()
# create an instance of ProvidersPaginated from a dict
providers_paginated_form_dict = providers_paginated.from_dict(providers_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


