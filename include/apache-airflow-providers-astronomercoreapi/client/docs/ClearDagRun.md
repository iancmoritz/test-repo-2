# ClearDagRun


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_run** | [**DagRun**](DagRun.md) |  | [optional] 
**task_instances** | [**List[TaskInstance]**](TaskInstance.md) |  | [optional] 

## Example

```python
from astronomercoreapi.models.clear_dag_run import ClearDagRun

# TODO update the JSON string below
json = "{}"
# create an instance of ClearDagRun from a JSON string
clear_dag_run_instance = ClearDagRun.from_json(json)
# print the JSON string representation of the object
print ClearDagRun.to_json()

# convert the object into a dict
clear_dag_run_dict = clear_dag_run_instance.to_dict()
# create an instance of ClearDagRun from a dict
clear_dag_run_form_dict = clear_dag_run.from_dict(clear_dag_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


