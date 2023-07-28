# InternalOutlet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra** | **Dict[str, str]** |  | [optional] 
**type** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.internal_outlet import InternalOutlet

# TODO update the JSON string below
json = "{}"
# create an instance of InternalOutlet from a JSON string
internal_outlet_instance = InternalOutlet.from_json(json)
# print the JSON string representation of the object
print InternalOutlet.to_json()

# convert the object into a dict
internal_outlet_dict = internal_outlet_instance.to_dict()
# create an instance of InternalOutlet from a dict
internal_outlet_form_dict = internal_outlet.from_dict(internal_outlet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


