# UpdateDag


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** |  | [optional] 
**is_dag_paused** | **bool** |  | [optional] 

## Example

```python
from astronomercoreapi.models.update_dag import UpdateDag

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDag from a JSON string
update_dag_instance = UpdateDag.from_json(json)
# print the JSON string representation of the object
print UpdateDag.to_json()

# convert the object into a dict
update_dag_dict = update_dag_instance.to_dict()
# create an instance of UpdateDag from a dict
update_dag_form_dict = update_dag.from_dict(update_dag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


