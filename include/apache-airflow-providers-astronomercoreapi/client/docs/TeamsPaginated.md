# TeamsPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | 
**offset** | **int** |  | 
**teams** | [**List[Team]**](Team.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from astronomercoreapi.models.teams_paginated import TeamsPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of TeamsPaginated from a JSON string
teams_paginated_instance = TeamsPaginated.from_json(json)
# print the JSON string representation of the object
print TeamsPaginated.to_json()

# convert the object into a dict
teams_paginated_dict = teams_paginated_instance.to_dict()
# create an instance of TeamsPaginated from a dict
teams_paginated_form_dict = teams_paginated.from_dict(teams_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


