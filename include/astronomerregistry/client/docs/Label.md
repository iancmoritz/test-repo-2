# Label


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | 
**created_by** | **str** |  | 
**description** | **str** |  | [optional] 
**graphics** | [**LabelGraphics**](LabelGraphics.md) |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | 
**organization_id** | **str** |  | [optional] 
**updated_at** | **str** |  | 
**updated_by** | **str** |  | 

## Example

```python
from astronomerregistry.models.label import Label

# TODO update the JSON string below
json = "{}"
# create an instance of Label from a JSON string
label_instance = Label.from_json(json)
# print the JSON string representation of the object
print Label.to_json()

# convert the object into a dict
label_dict = label_instance.to_dict()
# create an instance of Label from a dict
label_form_dict = label.from_dict(label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


