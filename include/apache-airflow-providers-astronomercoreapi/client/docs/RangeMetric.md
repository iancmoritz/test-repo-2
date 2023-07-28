# RangeMetric


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **str** |  | 
**deployment_name** | **str** |  | 
**end** | **int** |  | 
**release_name** | **str** |  | 
**start** | **int** |  | 
**step** | **int** |  | 
**values** | [**List[MetricValue]**](MetricValue.md) |  | 
**workspace_id** | **str** |  | 

## Example

```python
from astronomercoreapi.models.range_metric import RangeMetric

# TODO update the JSON string below
json = "{}"
# create an instance of RangeMetric from a JSON string
range_metric_instance = RangeMetric.from_json(json)
# print the JSON string representation of the object
print RangeMetric.to_json()

# convert the object into a dict
range_metric_dict = range_metric_instance.to_dict()
# create an instance of RangeMetric from a dict
range_metric_form_dict = range_metric.from_dict(range_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


