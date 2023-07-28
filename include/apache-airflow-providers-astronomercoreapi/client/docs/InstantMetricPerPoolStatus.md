# InstantMetricPerPoolStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **str** |  | 
**pool** | **str** |  | 
**release_name** | **str** |  | 
**status** | **str** |  | 
**value** | **float** |  | 
**workspace_id** | **str** |  | 

## Example

```python
from astronomercoreapi.models.instant_metric_per_pool_status import InstantMetricPerPoolStatus

# TODO update the JSON string below
json = "{}"
# create an instance of InstantMetricPerPoolStatus from a JSON string
instant_metric_per_pool_status_instance = InstantMetricPerPoolStatus.from_json(json)
# print the JSON string representation of the object
print InstantMetricPerPoolStatus.to_json()

# convert the object into a dict
instant_metric_per_pool_status_dict = instant_metric_per_pool_status_instance.to_dict()
# create an instance of InstantMetricPerPoolStatus from a dict
instant_metric_per_pool_status_form_dict = instant_metric_per_pool_status.from_dict(instant_metric_per_pool_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


