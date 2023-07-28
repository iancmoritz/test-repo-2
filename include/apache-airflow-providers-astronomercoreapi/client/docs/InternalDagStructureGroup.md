# InternalDagStructureGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[InternalTaskGroupChildrenInner]**](InternalTaskGroupChildrenInner.md) |  | [optional] 
**id** | **str** |  | [optional] 
**is_mapped** | **bool** |  | [optional] 
**label** | **str** |  | [optional] 
**tooltip** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.internal_dag_structure_group import InternalDagStructureGroup

# TODO update the JSON string below
json = "{}"
# create an instance of InternalDagStructureGroup from a JSON string
internal_dag_structure_group_instance = InternalDagStructureGroup.from_json(json)
# print the JSON string representation of the object
print InternalDagStructureGroup.to_json()

# convert the object into a dict
internal_dag_structure_group_dict = internal_dag_structure_group_instance.to_dict()
# create an instance of InternalDagStructureGroup from a dict
internal_dag_structure_group_form_dict = internal_dag_structure_group.from_dict(internal_dag_structure_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


