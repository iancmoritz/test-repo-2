# DeploymentLogEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw** | **str** |  | 
**source** | **str** |  | 
**timestamp** | **float** |  | 

## Example

```python
from astronomercoreapi.models.deployment_log_entry import DeploymentLogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentLogEntry from a JSON string
deployment_log_entry_instance = DeploymentLogEntry.from_json(json)
# print the JSON string representation of the object
print DeploymentLogEntry.to_json()

# convert the object into a dict
deployment_log_entry_dict = deployment_log_entry_instance.to_dict()
# create an instance of DeploymentLogEntry from a dict
deployment_log_entry_form_dict = deployment_log_entry.from_dict(deployment_log_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


