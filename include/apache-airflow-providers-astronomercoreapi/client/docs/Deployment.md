# Deployment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_emails** | **List[str]** |  | [optional] 
**api_key_only_deployments** | **bool** |  | 
**cluster_id** | **str** |  | 
**created_at** | **datetime** |  | 
**current_dag_tarball_version** | **str** |  | [optional] 
**current_image_version** | **str** |  | [optional] 
**dag_deploy_enabled** | **bool** |  | 
**description** | **str** |  | [optional] 
**desired_dag_tarball_version** | **str** |  | [optional] 
**environment_variables** | [**List[DeploymentEnvVar]**](DeploymentEnvVar.md) |  | [optional] 
**executor** | **str** |  | [optional] 
**external_ips** | **List[str]** |  | [optional] 
**id** | **str** |  | 
**image_id** | **str** |  | 
**image_repository** | **str** |  | 
**image_tag** | **str** |  | 
**is_high_availability** | **bool** |  | 
**name** | **str** |  | 
**org_short_name** | **str** | Deprecated: orgShortName has been replaced with organizationShortName | [optional] 
**organization_id** | **str** |  | 
**organization_name** | **str** |  | 
**organization_short_name** | **str** |  | 
**release_name** | **str** |  | 
**runtime_version** | **str** |  | 
**scheduler_au** | **int** |  | 
**scheduler_cpu** | **str** |  | 
**scheduler_memory** | **str** |  | 
**scheduler_replicas** | **int** |  | 
**scheduler_size** | **str** |  | [optional] 
**spec_created_at** | **datetime** |  | 
**spec_updated_at** | **datetime** |  | 
**status** | **str** |  | 
**status_reason** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | **datetime** |  | 
**web_server_cpu** | **str** |  | 
**web_server_ingress_hostname** | **str** |  | 
**web_server_memory** | **str** |  | 
**web_server_replicas** | **int** |  | [optional] 
**web_server_url** | **str** |  | 
**worker_cpu** | **str** |  | 
**worker_memory** | **str** |  | 
**worker_queues** | [**List[DeploymentWorkerQueue]**](DeploymentWorkerQueue.md) |  | [optional] 
**workers_au** | **int** |  | 
**workers_replicas** | **int** |  | [optional] 
**workload_identity** | **str** |  | [optional] 
**workspace_id** | **str** |  | 

## Example

```python
from astronomercoreapi.models.deployment import Deployment

# TODO update the JSON string below
json = "{}"
# create an instance of Deployment from a JSON string
deployment_instance = Deployment.from_json(json)
# print the JSON string representation of the object
print Deployment.to_json()

# convert the object into a dict
deployment_dict = deployment_instance.to_dict()
# create an instance of Deployment from a dict
deployment_form_dict = deployment.from_dict(deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


