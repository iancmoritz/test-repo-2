# InstantMetricPerComponentStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | 
**deployment_id** | **str** |  | 
**release_name** | **str** |  | 
**status** | **str** |  | 
**value** | **float** |  | 
**workspace_id** | **str** |  | 

## Example

```python
from astronomercoreapi.models.instant_metric_per_component_status import InstantMetricPerComponentStatus

# TODO update the JSON string below
json = "{}"
# create an instance of InstantMetricPerComponentStatus from a JSON string
instant_metric_per_component_status_instance = InstantMetricPerComponentStatus.from_json(json)
# print the JSON string representation of the object
print InstantMetricPerComponentStatus.to_json()

# convert the object into a dict
instant_metric_per_component_status_dict = instant_metric_per_component_status_instance.to_dict()
# create an instance of InstantMetricPerComponentStatus from a dict
instant_metric_per_component_status_form_dict = instant_metric_per_component_status.from_dict(instant_metric_per_component_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


