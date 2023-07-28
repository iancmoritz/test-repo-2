# RangeMetricPerComponentAndQueueAndStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | 
**deployment_id** | **str** |  | 
**end** | **int** |  | 
**queue** | **str** |  | [optional] 
**release_name** | **str** |  | 
**start** | **int** |  | 
**status** | **str** |  | 
**step** | **int** |  | 
**values** | [**List[MetricValue]**](MetricValue.md) |  | 
**workspace_id** | **str** |  | 

## Example

```python
from astronomercoreapi.models.range_metric_per_component_and_queue_and_status import RangeMetricPerComponentAndQueueAndStatus

# TODO update the JSON string below
json = "{}"
# create an instance of RangeMetricPerComponentAndQueueAndStatus from a JSON string
range_metric_per_component_and_queue_and_status_instance = RangeMetricPerComponentAndQueueAndStatus.from_json(json)
# print the JSON string representation of the object
print RangeMetricPerComponentAndQueueAndStatus.to_json()

# convert the object into a dict
range_metric_per_component_and_queue_and_status_dict = range_metric_per_component_and_queue_and_status_instance.to_dict()
# create an instance of RangeMetricPerComponentAndQueueAndStatus from a dict
range_metric_per_component_and_queue_and_status_form_dict = range_metric_per_component_and_queue_and_status.from_dict(range_metric_per_component_and_queue_and_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


