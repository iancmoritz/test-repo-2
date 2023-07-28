# DeploymentLog


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | 
**max_num_results** | **int** |  | 
**offset** | **int** |  | 
**result_count** | **int** |  | 
**results** | [**List[DeploymentLogEntry]**](DeploymentLogEntry.md) |  | 
**search_id** | **str** |  | 

## Example

```python
from astronomercoreapi.models.deployment_log import DeploymentLog

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentLog from a JSON string
deployment_log_instance = DeploymentLog.from_json(json)
# print the JSON string representation of the object
print DeploymentLog.to_json()

# convert the object into a dict
deployment_log_dict = deployment_log_instance.to_dict()
# create an instance of DeploymentLog from a dict
deployment_log_form_dict = deployment_log.from_dict(deployment_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


