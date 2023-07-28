# DeploymentEnvVar


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_secret** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.deployment_env_var import DeploymentEnvVar

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentEnvVar from a JSON string
deployment_env_var_instance = DeploymentEnvVar.from_json(json)
# print the JSON string representation of the object
print DeploymentEnvVar.to_json()

# convert the object into a dict
deployment_env_var_dict = deployment_env_var_instance.to_dict()
# create an instance of DeploymentEnvVar from a dict
deployment_env_var_form_dict = deployment_env_var.from_dict(deployment_env_var_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


