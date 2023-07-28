# DeploymentOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executors** | **List[str]** |  | 
**resource_quotas** | [**ResourceQuotaOptions**](ResourceQuotaOptions.md) |  | 
**runtime_releases** | [**List[RuntimeRelease]**](RuntimeRelease.md) |  | 
**scheduler_machines** | [**List[SchedulerMachine]**](SchedulerMachine.md) |  | 
**worker_machines** | [**List[WorkerMachine]**](WorkerMachine.md) |  | 
**worker_queues** | [**WorkerQueueOptions**](WorkerQueueOptions.md) |  | 

## Example

```python
from astronomercoreapi.models.deployment_options import DeploymentOptions

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentOptions from a JSON string
deployment_options_instance = DeploymentOptions.from_json(json)
# print the JSON string representation of the object
print DeploymentOptions.to_json()

# convert the object into a dict
deployment_options_dict = deployment_options_instance.to_dict()
# create an instance of DeploymentOptions from a dict
deployment_options_form_dict = deployment_options.from_dict(deployment_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


