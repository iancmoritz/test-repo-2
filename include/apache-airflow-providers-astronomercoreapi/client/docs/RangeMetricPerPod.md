# RangeMetricPerPod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | 
**deployment_id** | **str** |  | 
**end** | **int** |  | 
**pod** | **str** |  | 
**release_name** | **str** |  | 
**start** | **int** |  | 
**step** | **int** |  | 
**values** | [**List[MetricValue]**](MetricValue.md) |  | 
**workspace_id** | **str** |  | 

## Example

```python
from astronomercoreapi.models.range_metric_per_pod import RangeMetricPerPod

# TODO update the JSON string below
json = "{}"
# create an instance of RangeMetricPerPod from a JSON string
range_metric_per_pod_instance = RangeMetricPerPod.from_json(json)
# print the JSON string representation of the object
print RangeMetricPerPod.to_json()

# convert the object into a dict
range_metric_per_pod_dict = range_metric_per_pod_instance.to_dict()
# create an instance of RangeMetricPerPod from a dict
range_metric_per_pod_form_dict = range_metric_per_pod.from_dict(range_metric_per_pod_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


