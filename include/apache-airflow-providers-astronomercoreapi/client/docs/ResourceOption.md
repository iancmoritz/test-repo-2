# ResourceOption


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**ResourceRange**](ResourceRange.md) |  | 
**memory** | [**ResourceRange**](ResourceRange.md) |  | 

## Example

```python
from astronomercoreapi.models.resource_option import ResourceOption

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceOption from a JSON string
resource_option_instance = ResourceOption.from_json(json)
# print the JSON string representation of the object
print ResourceOption.to_json()

# convert the object into a dict
resource_option_dict = resource_option_instance.to_dict()
# create an instance of ResourceOption from a dict
resource_option_form_dict = resource_option.from_dict(resource_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


