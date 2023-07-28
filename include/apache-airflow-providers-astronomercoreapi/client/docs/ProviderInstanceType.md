# ProviderInstanceType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **int** |  | 
**name** | **str** |  | 
**ram** | **str** |  | 

## Example

```python
from astronomercoreapi.models.provider_instance_type import ProviderInstanceType

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderInstanceType from a JSON string
provider_instance_type_instance = ProviderInstanceType.from_json(json)
# print the JSON string representation of the object
print ProviderInstanceType.to_json()

# convert the object into a dict
provider_instance_type_dict = provider_instance_type_instance.to_dict()
# create an instance of ProviderInstanceType from a dict
provider_instance_type_form_dict = provider_instance_type.from_dict(provider_instance_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


