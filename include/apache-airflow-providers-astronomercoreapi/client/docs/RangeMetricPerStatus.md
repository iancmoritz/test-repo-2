# RangeMetricPerStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **str** |  | 
**end** | **int** |  | 
**release_name** | **str** |  | 
**start** | **int** |  | 
**status** | **str** |  | 
**step** | **int** |  | 
**values** | [**List[MetricValue]**](MetricValue.md) |  | 
**workspace_id** | **str** |  | 

## Example

```python
from astronomercoreapi.models.range_metric_per_status import RangeMetricPerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of RangeMetricPerStatus from a JSON string
range_metric_per_status_instance = RangeMetricPerStatus.from_json(json)
# print the JSON string representation of the object
print RangeMetricPerStatus.to_json()

# convert the object into a dict
range_metric_per_status_dict = range_metric_per_status_instance.to_dict()
# create an instance of RangeMetricPerStatus from a dict
range_metric_per_status_form_dict = range_metric_per_status.from_dict(range_metric_per_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


