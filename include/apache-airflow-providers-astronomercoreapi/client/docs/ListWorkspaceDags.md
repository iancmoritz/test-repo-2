# ListWorkspaceDags


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[WorkspaceDag]**](WorkspaceDag.md) |  | 
**next_cursor** | **str** |  | [optional] 
**previous_cursor** | **str** |  | [optional] 
**total_count** | **int** |  | [optional] 
**warnings** | **List[str]** |  | [optional] 

## Example

```python
from astronomercoreapi.models.list_workspace_dags import ListWorkspaceDags

# TODO update the JSON string below
json = "{}"
# create an instance of ListWorkspaceDags from a JSON string
list_workspace_dags_instance = ListWorkspaceDags.from_json(json)
# print the JSON string representation of the object
print ListWorkspaceDags.to_json()

# convert the object into a dict
list_workspace_dags_dict = list_workspace_dags_instance.to_dict()
# create an instance of ListWorkspaceDags from a dict
list_workspace_dags_form_dict = list_workspace_dags.from_dict(list_workspace_dags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


