# DagSchedule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron_expression** | [**InternalScheduleIntervalCronExpression**](InternalScheduleIntervalCronExpression.md) |  | [optional] 
**relative_delta** | [**InternalScheduleIntervalRelativeDelta**](InternalScheduleIntervalRelativeDelta.md) |  | [optional] 
**time_delta** | [**InternalScheduleIntervalTimeDelta**](InternalScheduleIntervalTimeDelta.md) |  | [optional] 

## Example

```python
from astronomercoreapi.models.dag_schedule import DagSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of DagSchedule from a JSON string
dag_schedule_instance = DagSchedule.from_json(json)
# print the JSON string representation of the object
print DagSchedule.to_json()

# convert the object into a dict
dag_schedule_dict = dag_schedule_instance.to_dict()
# create an instance of DagSchedule from a dict
dag_schedule_form_dict = dag_schedule.from_dict(dag_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


