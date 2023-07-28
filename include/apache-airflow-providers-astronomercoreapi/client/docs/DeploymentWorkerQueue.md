# DeploymentWorkerQueue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**is_default** | **bool** |  | 
**max_worker_count** | **int** |  | 
**min_worker_count** | **int** |  | 
**name** | **str** |  | 
**node_pool_id** | **str** |  | 
**pod_cpu** | **str** |  | 
**pod_ram** | **str** |  | 
**pod_size** | **str** |  | 
**worker_concurrency** | **int** |  | 

## Example

```python
from astronomercoreapi.models.deployment_worker_queue import DeploymentWorkerQueue

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentWorkerQueue from a JSON string
deployment_worker_queue_instance = DeploymentWorkerQueue.from_json(json)
# print the JSON string representation of the object
print DeploymentWorkerQueue.to_json()

# convert the object into a dict
deployment_worker_queue_dict = deployment_worker_queue_instance.to_dict()
# create an instance of DeploymentWorkerQueue from a dict
deployment_worker_queue_form_dict = deployment_worker_queue.from_dict(deployment_worker_queue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


