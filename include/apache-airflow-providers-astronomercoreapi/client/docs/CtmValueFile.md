# CtmValueFile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conn_id** | **str** |  | 
**file_type** | **str** |  | [optional] 
**path** | **str** |  | 

## Example

```python
from astronomercoreapi.models.ctm_value_file import CtmValueFile

# TODO update the JSON string below
json = "{}"
# create an instance of CtmValueFile from a JSON string
ctm_value_file_instance = CtmValueFile.from_json(json)
# print the JSON string representation of the object
print CtmValueFile.to_json()

# convert the object into a dict
ctm_value_file_dict = ctm_value_file_instance.to_dict()
# create an instance of CtmValueFile from a dict
ctm_value_file_form_dict = ctm_value_file.from_dict(ctm_value_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


