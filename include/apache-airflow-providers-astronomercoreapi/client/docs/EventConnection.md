# EventConnection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**name** | **str** |  | [optional] 
**strategy** | **str** |  | 

## Example

```python
from astronomercoreapi.models.event_connection import EventConnection

# TODO update the JSON string below
json = "{}"
# create an instance of EventConnection from a JSON string
event_connection_instance = EventConnection.from_json(json)
# print the JSON string representation of the object
print EventConnection.to_json()

# convert the object into a dict
event_connection_dict = event_connection_instance.to_dict()
# create an instance of EventConnection from a dict
event_connection_form_dict = event_connection.from_dict(event_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


