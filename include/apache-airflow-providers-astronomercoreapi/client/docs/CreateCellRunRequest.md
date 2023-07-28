# CreateCellRunRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pipeline_session_id** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.create_cell_run_request import CreateCellRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCellRunRequest from a JSON string
create_cell_run_request_instance = CreateCellRunRequest.from_json(json)
# print the JSON string representation of the object
print CreateCellRunRequest.to_json()

# convert the object into a dict
create_cell_run_request_dict = create_cell_run_request_instance.to_dict()
# create an instance of CreateCellRunRequest from a dict
create_cell_run_request_form_dict = create_cell_run_request.from_dict(create_cell_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


