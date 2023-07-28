# EventOrganization


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.event_organization import EventOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of EventOrganization from a JSON string
event_organization_instance = EventOrganization.from_json(json)
# print the JSON string representation of the object
print EventOrganization.to_json()

# convert the object into a dict
event_organization_dict = event_organization_instance.to_dict()
# create an instance of EventOrganization from a dict
event_organization_form_dict = event_organization.from_dict(event_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


