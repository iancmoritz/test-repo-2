# InternalDagStructure


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edges** | [**List[InternalEdge]**](InternalEdge.md) |  | [optional] 
**group** | [**InternalDagStructureGroup**](InternalDagStructureGroup.md) |  | [optional] 
**ordering** | **List[str]** |  | [optional] 

## Example

```python
from astronomercoreapi.models.internal_dag_structure import InternalDagStructure

# TODO update the JSON string below
json = "{}"
# create an instance of InternalDagStructure from a JSON string
internal_dag_structure_instance = InternalDagStructure.from_json(json)
# print the JSON string representation of the object
print InternalDagStructure.to_json()

# convert the object into a dict
internal_dag_structure_dict = internal_dag_structure_instance.to_dict()
# create an instance of InternalDagStructure from a dict
internal_dag_structure_form_dict = internal_dag_structure.from_dict(internal_dag_structure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


