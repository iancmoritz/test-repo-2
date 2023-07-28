# RunsWithGroups


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_runs** | [**List[DagRun]**](DagRun.md) |  | [optional] 
**groups** | [**RunGroup**](RunGroup.md) |  | 
**ordering** | **List[str]** |  | 

## Example

```python
from astronomercoreapi.models.runs_with_groups import RunsWithGroups

# TODO update the JSON string below
json = "{}"
# create an instance of RunsWithGroups from a JSON string
runs_with_groups_instance = RunsWithGroups.from_json(json)
# print the JSON string representation of the object
print RunsWithGroups.to_json()

# convert the object into a dict
runs_with_groups_dict = runs_with_groups_instance.to_dict()
# create an instance of RunsWithGroups from a dict
runs_with_groups_form_dict = runs_with_groups.from_dict(runs_with_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


