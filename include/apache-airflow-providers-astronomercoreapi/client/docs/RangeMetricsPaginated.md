# RangeMetricsPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **int** |  | 
**limit** | **int** |  | 
**metrics** | [**List[RangeMetric]**](RangeMetric.md) |  | 
**offset** | **int** |  | 
**start** | **int** |  | 
**step** | **int** |  | 
**total_deployments** | **int** |  | 

## Example

```python
from astronomercoreapi.models.range_metrics_paginated import RangeMetricsPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of RangeMetricsPaginated from a JSON string
range_metrics_paginated_instance = RangeMetricsPaginated.from_json(json)
# print the JSON string representation of the object
print RangeMetricsPaginated.to_json()

# convert the object into a dict
range_metrics_paginated_dict = range_metrics_paginated_instance.to_dict()
# create an instance of RangeMetricsPaginated from a dict
range_metrics_paginated_form_dict = range_metrics_paginated.from_dict(range_metrics_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


