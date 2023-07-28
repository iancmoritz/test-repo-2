# SchedulerMachine


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this machine. | 
**spec** | [**MachineSpec**](MachineSpec.md) |  | 

## Example

```python
from astronomercoreapi.models.scheduler_machine import SchedulerMachine

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulerMachine from a JSON string
scheduler_machine_instance = SchedulerMachine.from_json(json)
# print the JSON string representation of the object
print SchedulerMachine.to_json()

# convert the object into a dict
scheduler_machine_dict = scheduler_machine_instance.to_dict()
# create an instance of SchedulerMachine from a dict
scheduler_machine_form_dict = scheduler_machine.from_dict(scheduler_machine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


