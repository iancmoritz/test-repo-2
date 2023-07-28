# ClearDagRunRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_dry_run** | **bool** |  | [optional] 

## Example

```python
from astronomercoreapi.models.clear_dag_run_request import ClearDagRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClearDagRunRequest from a JSON string
clear_dag_run_request_instance = ClearDagRunRequest.from_json(json)
# print the JSON string representation of the object
print ClearDagRunRequest.to_json()

# convert the object into a dict
clear_dag_run_request_dict = clear_dag_run_request_instance.to_dict()
# create an instance of ClearDagRunRequest from a dict
clear_dag_run_request_form_dict = clear_dag_run_request.from_dict(clear_dag_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


