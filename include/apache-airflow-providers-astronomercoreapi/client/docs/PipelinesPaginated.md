# PipelinesPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | 
**offset** | **int** |  | 
**pipelines** | [**List[Pipeline]**](Pipeline.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from astronomercoreapi.models.pipelines_paginated import PipelinesPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of PipelinesPaginated from a JSON string
pipelines_paginated_instance = PipelinesPaginated.from_json(json)
# print the JSON string representation of the object
print PipelinesPaginated.to_json()

# convert the object into a dict
pipelines_paginated_dict = pipelines_paginated_instance.to_dict()
# create an instance of PipelinesPaginated from a dict
pipelines_paginated_form_dict = pipelines_paginated.from_dict(pipelines_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


