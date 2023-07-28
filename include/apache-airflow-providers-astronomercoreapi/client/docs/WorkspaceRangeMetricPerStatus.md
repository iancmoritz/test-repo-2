# WorkspaceRangeMetricPerStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **int** |  | 
**start** | **int** |  | 
**status** | **str** |  | 
**step** | **int** |  | 
**values** | [**List[MetricValue]**](MetricValue.md) |  | 
**workspace_id** | **str** |  | 

## Example

```python
from astronomercoreapi.models.workspace_range_metric_per_status import WorkspaceRangeMetricPerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceRangeMetricPerStatus from a JSON string
workspace_range_metric_per_status_instance = WorkspaceRangeMetricPerStatus.from_json(json)
# print the JSON string representation of the object
print WorkspaceRangeMetricPerStatus.to_json()

# convert the object into a dict
workspace_range_metric_per_status_dict = workspace_range_metric_per_status_instance.to_dict()
# create an instance of WorkspaceRangeMetricPerStatus from a dict
workspace_range_metric_per_status_form_dict = workspace_range_metric_per_status.from_dict(workspace_range_metric_per_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


