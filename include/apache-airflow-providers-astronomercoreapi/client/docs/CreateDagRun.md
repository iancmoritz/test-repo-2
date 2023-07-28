# CreateDagRun


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conf** | **object** |  | [optional] 
**dag_id** | **str** |  | 
**dag_run_id** | **str** |  | 
**end_date** | **datetime** |  | [optional] 
**external_trigger** | **bool** |  | 
**logical_date** | **datetime** |  | 
**start_date** | **datetime** |  | [optional] 
**state** | **str** |  | 

## Example

```python
from astronomercoreapi.models.create_dag_run import CreateDagRun

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDagRun from a JSON string
create_dag_run_instance = CreateDagRun.from_json(json)
# print the JSON string representation of the object
print CreateDagRun.to_json()

# convert the object into a dict
create_dag_run_dict = create_dag_run_instance.to_dict()
# create an instance of CreateDagRun from a dict
create_dag_run_form_dict = create_dag_run.from_dict(create_dag_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


