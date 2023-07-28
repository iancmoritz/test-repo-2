# CtmGenerationDecorator


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decorator_arg_configs** | **List[str]** | The cell type configs that will be passed as keyword arguments to the decorator | [optional] 
**decorator_function_params** | **List[str]** | Positional function parameters that are added by the decorator | [optional] 
**decorator_name** | **str** | The name of the decorator | 
**function_arg_configs** | **List[str]** | The cell type configs that will be passed as keyword arguments to the function | [optional] 
**function_code_config** | **str** | The cell type config that will contain the function code | 
**imports** | **List[str]** | Import statements for the decorator cell type | [optional] 
**include_implicit_deps** | **bool** | Whether to pass implicit dependencies as positional arguments to the function | [optional] 
**include_task_id_as_decorator_arg** | **bool** | Whether to pass the task id as a keyword argument to the decorator | [optional] 
**include_task_id_as_function_arg** | **bool** | Whether to pass the task id as a keyword argument to the function | [optional] 

## Example

```python
from astronomercoreapi.models.ctm_generation_decorator import CtmGenerationDecorator

# TODO update the JSON string below
json = "{}"
# create an instance of CtmGenerationDecorator from a JSON string
ctm_generation_decorator_instance = CtmGenerationDecorator.from_json(json)
# print the JSON string representation of the object
print CtmGenerationDecorator.to_json()

# convert the object into a dict
ctm_generation_decorator_dict = ctm_generation_decorator_instance.to_dict()
# create an instance of CtmGenerationDecorator from a dict
ctm_generation_decorator_form_dict = ctm_generation_decorator.from_dict(ctm_generation_decorator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


