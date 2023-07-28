# RangeMetricsPerStatusPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **int** |  | 
**limit** | **int** |  | 
**metrics** | [**List[RangeMetricPerStatus]**](RangeMetricPerStatus.md) |  | 
**offset** | **int** |  | 
**start** | **int** |  | 
**step** | **int** |  | 
**total_deployments** | **int** |  | 

## Example

```python
from astronomercoreapi.models.range_metrics_per_status_paginated import RangeMetricsPerStatusPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of RangeMetricsPerStatusPaginated from a JSON string
range_metrics_per_status_paginated_instance = RangeMetricsPerStatusPaginated.from_json(json)
# print the JSON string representation of the object
print RangeMetricsPerStatusPaginated.to_json()

# convert the object into a dict
range_metrics_per_status_paginated_dict = range_metrics_per_status_paginated_instance.to_dict()
# create an instance of RangeMetricsPerStatusPaginated from a dict
range_metrics_per_status_paginated_form_dict = range_metrics_per_status_paginated.from_dict(range_metrics_per_status_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


