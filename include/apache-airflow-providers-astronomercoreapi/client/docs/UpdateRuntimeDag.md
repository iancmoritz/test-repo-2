# UpdateRuntimeDag


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** |  | 
**is_dag_paused** | **bool** |  | 

## Example

```python
from astronomercoreapi.models.update_runtime_dag import UpdateRuntimeDag

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRuntimeDag from a JSON string
update_runtime_dag_instance = UpdateRuntimeDag.from_json(json)
# print the JSON string representation of the object
print UpdateRuntimeDag.to_json()

# convert the object into a dict
update_runtime_dag_dict = update_runtime_dag_instance.to_dict()
# create an instance of UpdateRuntimeDag from a dict
update_runtime_dag_form_dict = update_runtime_dag.from_dict(update_runtime_dag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


