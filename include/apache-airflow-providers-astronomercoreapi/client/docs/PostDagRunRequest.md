# PostDagRunRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logical_date** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.post_dag_run_request import PostDagRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDagRunRequest from a JSON string
post_dag_run_request_instance = PostDagRunRequest.from_json(json)
# print the JSON string representation of the object
print PostDagRunRequest.to_json()

# convert the object into a dict
post_dag_run_request_dict = post_dag_run_request_instance.to_dict()
# create an instance of PostDagRunRequest from a dict
post_dag_run_request_form_dict = post_dag_run_request.from_dict(post_dag_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


