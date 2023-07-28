# CreateDagRunRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logical_date** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.create_dag_run_request import CreateDagRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDagRunRequest from a JSON string
create_dag_run_request_instance = CreateDagRunRequest.from_json(json)
# print the JSON string representation of the object
print CreateDagRunRequest.to_json()

# convert the object into a dict
create_dag_run_request_dict = create_dag_run_request_instance.to_dict()
# create an instance of CreateDagRunRequest from a dict
create_dag_run_request_form_dict = create_dag_run_request.from_dict(create_dag_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


