# InternalScheduleIntervalRelativeDelta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **int** |  | [optional] 
**days** | **int** |  | [optional] 
**hour** | **int** |  | [optional] 
**hours** | **int** |  | [optional] 
**leapdays** | **int** |  | [optional] 
**microsecond** | **int** |  | [optional] 
**microseconds** | **int** |  | [optional] 
**minute** | **int** |  | [optional] 
**minutes** | **int** |  | [optional] 
**month** | **int** |  | [optional] 
**months** | **int** |  | [optional] 
**second** | **int** |  | [optional] 
**seconds** | **int** |  | [optional] 
**week** | **int** |  | [optional] 
**weeks** | **int** |  | [optional] 
**year** | **int** |  | [optional] 
**years** | **int** |  | [optional] 

## Example

```python
from astronomercoreapi.models.internal_schedule_interval_relative_delta import InternalScheduleIntervalRelativeDelta

# TODO update the JSON string below
json = "{}"
# create an instance of InternalScheduleIntervalRelativeDelta from a JSON string
internal_schedule_interval_relative_delta_instance = InternalScheduleIntervalRelativeDelta.from_json(json)
# print the JSON string representation of the object
print InternalScheduleIntervalRelativeDelta.to_json()

# convert the object into a dict
internal_schedule_interval_relative_delta_dict = internal_schedule_interval_relative_delta_instance.to_dict()
# create an instance of InternalScheduleIntervalRelativeDelta from a dict
internal_schedule_interval_relative_delta_form_dict = internal_schedule_interval_relative_delta.from_dict(internal_schedule_interval_relative_delta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


