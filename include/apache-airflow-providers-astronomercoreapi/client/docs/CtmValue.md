# CtmValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boolean** | **bool** |  | [optional] 
**duration** | [**CtmValueDuration**](CtmValueDuration.md) |  | [optional] 
**file** | [**CtmValueFile**](CtmValueFile.md) |  | [optional] 
**float** | **float** |  | [optional] 
**integer** | **int** |  | [optional] 
**string** | **str** |  | [optional] 
**string_list** | **List[str]** |  | [optional] 
**string_list_map** | **Dict[str, List[str]]** |  | [optional] 
**string_map** | **Dict[str, str]** |  | [optional] 
**string_map_list** | **List[Dict[str, str]]** |  | [optional] 
**string_set** | **Dict[str, bool]** |  | [optional] 
**table** | [**CtmValueTable**](CtmValueTable.md) |  | [optional] 

## Example

```python
from astronomercoreapi.models.ctm_value import CtmValue

# TODO update the JSON string below
json = "{}"
# create an instance of CtmValue from a JSON string
ctm_value_instance = CtmValue.from_json(json)
# print the JSON string representation of the object
print CtmValue.to_json()

# convert the object into a dict
ctm_value_dict = ctm_value_instance.to_dict()
# create an instance of CtmValue from a dict
ctm_value_form_dict = ctm_value.from_dict(ctm_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


