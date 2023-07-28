# RuntimeApiCapabilities


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_clear_dag_run** | **bool** |  | 
**can_update_task_instance** | **bool** |  | 

## Example

```python
from astronomercoreapi.models.runtime_api_capabilities import RuntimeApiCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeApiCapabilities from a JSON string
runtime_api_capabilities_instance = RuntimeApiCapabilities.from_json(json)
# print the JSON string representation of the object
print RuntimeApiCapabilities.to_json()

# convert the object into a dict
runtime_api_capabilities_dict = runtime_api_capabilities_instance.to_dict()
# create an instance of RuntimeApiCapabilities from a dict
runtime_api_capabilities_form_dict = runtime_api_capabilities.from_dict(runtime_api_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


