# ResourceQuotaOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_pod_size** | [**ResourceOption**](ResourceOption.md) |  | 
**resource_quota** | [**ResourceOption**](ResourceOption.md) |  | 

## Example

```python
from astronomercoreapi.models.resource_quota_options import ResourceQuotaOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceQuotaOptions from a JSON string
resource_quota_options_instance = ResourceQuotaOptions.from_json(json)
# print the JSON string representation of the object
print ResourceQuotaOptions.to_json()

# convert the object into a dict
resource_quota_options_dict = resource_quota_options_instance.to_dict()
# create an instance of ResourceQuotaOptions from a dict
resource_quota_options_form_dict = resource_quota_options.from_dict(resource_quota_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


