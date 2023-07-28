# WorkerQueueOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_workers** | [**ResourceRange**](ResourceRange.md) |  | [optional] 
**min_workers** | [**ResourceRange**](ResourceRange.md) |  | [optional] 

## Example

```python
from astronomercoreapi.models.worker_queue_options import WorkerQueueOptions

# TODO update the JSON string below
json = "{}"
# create an instance of WorkerQueueOptions from a JSON string
worker_queue_options_instance = WorkerQueueOptions.from_json(json)
# print the JSON string representation of the object
print WorkerQueueOptions.to_json()

# convert the object into a dict
worker_queue_options_dict = worker_queue_options_instance.to_dict()
# create an instance of WorkerQueueOptions from a dict
worker_queue_options_form_dict = worker_queue_options.from_dict(worker_queue_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


