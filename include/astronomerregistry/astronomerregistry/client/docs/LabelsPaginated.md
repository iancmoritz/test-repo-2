# LabelsPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | [**List[Label]**](Label.md) |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**total_count** | **int** |  | 

## Example

```python
from astronomerregistry.models.labels_paginated import LabelsPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of LabelsPaginated from a JSON string
labels_paginated_instance = LabelsPaginated.from_json(json)
# print the JSON string representation of the object
print LabelsPaginated.to_json()

# convert the object into a dict
labels_paginated_dict = labels_paginated_instance.to_dict()
# create an instance of LabelsPaginated from a dict
labels_paginated_form_dict = labels_paginated.from_dict(labels_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


