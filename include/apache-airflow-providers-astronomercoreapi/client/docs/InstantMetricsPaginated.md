# InstantMetricsPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | 
**metrics** | [**List[InstantMetric]**](InstantMetric.md) |  | 
**offset** | **int** |  | 
**total_deployments** | **int** |  | 

## Example

```python
from astronomercoreapi.models.instant_metrics_paginated import InstantMetricsPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of InstantMetricsPaginated from a JSON string
instant_metrics_paginated_instance = InstantMetricsPaginated.from_json(json)
# print the JSON string representation of the object
print InstantMetricsPaginated.to_json()

# convert the object into a dict
instant_metrics_paginated_dict = instant_metrics_paginated_instance.to_dict()
# create an instance of InstantMetricsPaginated from a dict
instant_metrics_paginated_form_dict = instant_metrics_paginated.from_dict(instant_metrics_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


