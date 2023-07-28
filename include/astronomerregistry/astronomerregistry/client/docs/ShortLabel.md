# ShortLabel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from astronomerregistry.models.short_label import ShortLabel

# TODO update the JSON string below
json = "{}"
# create an instance of ShortLabel from a JSON string
short_label_instance = ShortLabel.from_json(json)
# print the JSON string representation of the object
print ShortLabel.to_json()

# convert the object into a dict
short_label_dict = short_label_instance.to_dict()
# create an instance of ShortLabel from a dict
short_label_form_dict = short_label.from_dict(short_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


