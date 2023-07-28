# WorkerMachine


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concurrency** | [**ResourceRange**](ResourceRange.md) |  | 
**name** | **str** | The name of this machine. | 
**spec** | [**MachineSpec**](MachineSpec.md) |  | 

## Example

```python
from astronomercoreapi.models.worker_machine import WorkerMachine

# TODO update the JSON string below
json = "{}"
# create an instance of WorkerMachine from a JSON string
worker_machine_instance = WorkerMachine.from_json(json)
# print the JSON string representation of the object
print WorkerMachine.to_json()

# convert the object into a dict
worker_machine_dict = worker_machine_instance.to_dict()
# create an instance of WorkerMachine from a dict
worker_machine_form_dict = worker_machine.from_dict(worker_machine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


