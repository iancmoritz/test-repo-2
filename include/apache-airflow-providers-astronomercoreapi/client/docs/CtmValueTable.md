# CtmValueTable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conn_id** | **str** |  | 
**database** | **str** |  | [optional] 
**name** | **str** |  | 
**var_schema** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.ctm_value_table import CtmValueTable

# TODO update the JSON string below
json = "{}"
# create an instance of CtmValueTable from a JSON string
ctm_value_table_instance = CtmValueTable.from_json(json)
# print the JSON string representation of the object
print CtmValueTable.to_json()

# convert the object into a dict
ctm_value_table_dict = ctm_value_table_instance.to_dict()
# create an instance of CtmValueTable from a dict
ctm_value_table_form_dict = ctm_value_table.from_dict(ctm_value_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


