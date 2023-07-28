# RelatedModuleRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module_name** | **str** |  | 
**provider_name** | **str** |  | 
**version** | **str** |  | 

## Example

```python
from astronomerregistry.models.related_module_request import RelatedModuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedModuleRequest from a JSON string
related_module_request_instance = RelatedModuleRequest.from_json(json)
# print the JSON string representation of the object
print RelatedModuleRequest.to_json()

# convert the object into a dict
related_module_request_dict = related_module_request_instance.to_dict()
# create an instance of RelatedModuleRequest from a dict
related_module_request_form_dict = related_module_request.from_dict(related_module_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


