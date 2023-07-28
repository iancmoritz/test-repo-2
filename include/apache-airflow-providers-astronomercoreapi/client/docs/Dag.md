# Dag


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_dag_run_duration** | **float** |  | 
**dag_id** | **str** |  | 
**dag_run_duration_history** | **List[float]** |  | 
**dag_run_start_history** | **List[float]** |  | 
**dag_run_status_history** | **List[str]** |  | 
**dag_url** | **str** |  | 
**deployment_id** | **str** |  | 
**deployment_name** | **str** |  | 
**latest_dag_run_duration** | **float** |  | 
**latest_dag_run_end** | **float** |  | 
**latest_dag_run_status** | **str** |  | 
**next_dag_run** | **float** |  | 
**release_name** | **str** |  | 

## Example

```python
from astronomercoreapi.models.dag import Dag

# TODO update the JSON string below
json = "{}"
# create an instance of Dag from a JSON string
dag_instance = Dag.from_json(json)
# print the JSON string representation of the object
print Dag.to_json()

# convert the object into a dict
dag_dict = dag_instance.to_dict()
# create an instance of Dag from a dict
dag_form_dict = dag.from_dict(dag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


