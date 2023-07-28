# Entitlement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**required_tier** | **str** |  | 

## Example

```python
from astronomercoreapi.models.entitlement import Entitlement

# TODO update the JSON string below
json = "{}"
# create an instance of Entitlement from a JSON string
entitlement_instance = Entitlement.from_json(json)
# print the JSON string representation of the object
print Entitlement.to_json()

# convert the object into a dict
entitlement_dict = entitlement_instance.to_dict()
# create an instance of Entitlement from a dict
entitlement_form_dict = entitlement.from_dict(entitlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


