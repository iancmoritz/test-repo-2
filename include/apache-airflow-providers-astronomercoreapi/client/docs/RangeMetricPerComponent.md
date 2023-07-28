# RangeMetricPerComponent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | 
**deployment_id** | **str** |  | 
**end** | **int** |  | 
**release_name** | **str** |  | 
**start** | **int** |  | 
**step** | **int** |  | 
**values** | [**List[MetricValue]**](MetricValue.md) |  | 
**workspace_id** | **str** |  | 

## Example

```python
from astronomercoreapi.models.range_metric_per_component import RangeMetricPerComponent

# TODO update the JSON string below
json = "{}"
# create an instance of RangeMetricPerComponent from a JSON string
range_metric_per_component_instance = RangeMetricPerComponent.from_json(json)
# print the JSON string representation of the object
print RangeMetricPerComponent.to_json()

# convert the object into a dict
range_metric_per_component_dict = range_metric_per_component_instance.to_dict()
# create an instance of RangeMetricPerComponent from a dict
range_metric_per_component_form_dict = range_metric_per_component.from_dict(range_metric_per_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


