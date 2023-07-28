# InternalScheduleIntervalTimeDelta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **int** |  | [optional] 
**microseconds** | **int** |  | [optional] 
**seconds** | **int** |  | [optional] 

## Example

```python
from astronomercoreapi.models.internal_schedule_interval_time_delta import InternalScheduleIntervalTimeDelta

# TODO update the JSON string below
json = "{}"
# create an instance of InternalScheduleIntervalTimeDelta from a JSON string
internal_schedule_interval_time_delta_instance = InternalScheduleIntervalTimeDelta.from_json(json)
# print the JSON string representation of the object
print InternalScheduleIntervalTimeDelta.to_json()

# convert the object into a dict
internal_schedule_interval_time_delta_dict = internal_schedule_interval_time_delta_instance.to_dict()
# create an instance of InternalScheduleIntervalTimeDelta from a dict
internal_schedule_interval_time_delta_form_dict = internal_schedule_interval_time_delta.from_dict(internal_schedule_interval_time_delta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


