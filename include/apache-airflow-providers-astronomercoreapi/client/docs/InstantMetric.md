# InstantMetric


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **str** |  | 
**deployment_name** | **str** |  | 
**release_name** | **str** |  | 
**value** | **float** |  | 
**workspace_id** | **str** |  | 

## Example

```python
from astronomercoreapi.models.instant_metric import InstantMetric

# TODO update the JSON string below
json = "{}"
# create an instance of InstantMetric from a JSON string
instant_metric_instance = InstantMetric.from_json(json)
# print the JSON string representation of the object
print InstantMetric.to_json()

# convert the object into a dict
instant_metric_dict = instant_metric_instance.to_dict()
# create an instance of InstantMetric from a dict
instant_metric_form_dict = instant_metric.from_dict(instant_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


