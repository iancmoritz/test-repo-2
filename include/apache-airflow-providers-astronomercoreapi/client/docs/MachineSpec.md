# MachineSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **int** | A slice of CPU expressed in Millicpu (m). | 
**ephemeral_storage** | **int** | A slice of Ephemeral Storage expressed in Mebibytes (MiB). | [optional] 
**memory** | **int** | A slice of Memory expressed in Mebibytes (MiB). | 

## Example

```python
from astronomercoreapi.models.machine_spec import MachineSpec

# TODO update the JSON string below
json = "{}"
# create an instance of MachineSpec from a JSON string
machine_spec_instance = MachineSpec.from_json(json)
# print the JSON string representation of the object
print MachineSpec.to_json()

# convert the object into a dict
machine_spec_dict = machine_spec_instance.to_dict()
# create an instance of MachineSpec from a dict
machine_spec_form_dict = machine_spec.from_dict(machine_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


