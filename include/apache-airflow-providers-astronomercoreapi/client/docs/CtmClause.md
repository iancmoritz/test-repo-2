# CtmClause


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**operator** | **str** |  | 
**value** | [**CtmValue**](CtmValue.md) |  | 

## Example

```python
from astronomercoreapi.models.ctm_clause import CtmClause

# TODO update the JSON string below
json = "{}"
# create an instance of CtmClause from a JSON string
ctm_clause_instance = CtmClause.from_json(json)
# print the JSON string representation of the object
print CtmClause.to_json()

# convert the object into a dict
ctm_clause_dict = ctm_clause_instance.to_dict()
# create an instance of CtmClause from a dict
ctm_clause_form_dict = ctm_clause.from_dict(ctm_clause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


