# PostDagRun


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conf** | **object** |  | [optional] 
**dag_id** | **str** |  | [optional] 
**dag_run_id** | **str** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**external_trigger** | **bool** |  | [optional] 
**logical_date** | **datetime** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.post_dag_run import PostDagRun

# TODO update the JSON string below
json = "{}"
# create an instance of PostDagRun from a JSON string
post_dag_run_instance = PostDagRun.from_json(json)
# print the JSON string representation of the object
print PostDagRun.to_json()

# convert the object into a dict
post_dag_run_dict = post_dag_run_instance.to_dict()
# create an instance of PostDagRun from a dict
post_dag_run_form_dict = post_dag_run.from_dict(post_dag_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


