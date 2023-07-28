# CtmGenerationInvoke


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_task_id_arg** | **bool** |  | [optional] 
**function_name** | **str** |  | 
**imports** | **List[str]** |  | [optional] 

## Example

```python
from astronomercoreapi.models.ctm_generation_invoke import CtmGenerationInvoke

# TODO update the JSON string below
json = "{}"
# create an instance of CtmGenerationInvoke from a JSON string
ctm_generation_invoke_instance = CtmGenerationInvoke.from_json(json)
# print the JSON string representation of the object
print CtmGenerationInvoke.to_json()

# convert the object into a dict
ctm_generation_invoke_dict = ctm_generation_invoke_instance.to_dict()
# create an instance of CtmGenerationInvoke from a dict
ctm_generation_invoke_form_dict = ctm_generation_invoke.from_dict(ctm_generation_invoke_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


