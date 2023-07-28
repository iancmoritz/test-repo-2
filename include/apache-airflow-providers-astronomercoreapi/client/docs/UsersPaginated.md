# UsersPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | 
**offset** | **int** |  | 
**total_count** | **int** |  | 
**users** | [**List[User]**](User.md) |  | 

## Example

```python
from astronomercoreapi.models.users_paginated import UsersPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of UsersPaginated from a JSON string
users_paginated_instance = UsersPaginated.from_json(json)
# print the JSON string representation of the object
print UsersPaginated.to_json()

# convert the object into a dict
users_paginated_dict = users_paginated_instance.to_dict()
# create an instance of UsersPaginated from a dict
users_paginated_form_dict = users_paginated.from_dict(users_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


