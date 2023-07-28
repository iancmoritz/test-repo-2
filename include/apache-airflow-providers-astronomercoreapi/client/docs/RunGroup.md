# RunGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[RunGroup]**](RunGroup.md) |  | [optional] 
**extra_links** | **List[str]** |  | [optional] 
**has_outlet_datasets** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**is_mapped** | **bool** |  | [optional] 
**label** | **str** |  | [optional] 
**operator** | **str** |  | [optional] 
**task_instances** | [**List[TaskInstance]**](TaskInstance.md) |  | [optional] 

## Example

```python
from astronomercoreapi.models.run_group import RunGroup

# TODO update the JSON string below
json = "{}"
# create an instance of RunGroup from a JSON string
run_group_instance = RunGroup.from_json(json)
# print the JSON string representation of the object
print RunGroup.to_json()

# convert the object into a dict
run_group_dict = run_group_instance.to_dict()
# create an instance of RunGroup from a dict
run_group_form_dict = run_group.from_dict(run_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


