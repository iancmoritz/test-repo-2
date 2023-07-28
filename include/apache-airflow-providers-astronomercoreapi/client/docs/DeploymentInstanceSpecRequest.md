# DeploymentInstanceSpecRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**au** | **int** |  | [optional] 
**cpu** | **str** |  | [optional] 
**memory** | **str** |  | [optional] 
**replicas** | **int** |  | [optional] 

## Example

```python
from astronomercoreapi.models.deployment_instance_spec_request import DeploymentInstanceSpecRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentInstanceSpecRequest from a JSON string
deployment_instance_spec_request_instance = DeploymentInstanceSpecRequest.from_json(json)
# print the JSON string representation of the object
print DeploymentInstanceSpecRequest.to_json()

# convert the object into a dict
deployment_instance_spec_request_dict = deployment_instance_spec_request_instance.to_dict()
# create an instance of DeploymentInstanceSpecRequest from a dict
deployment_instance_spec_request_form_dict = deployment_instance_spec_request.from_dict(deployment_instance_spec_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


