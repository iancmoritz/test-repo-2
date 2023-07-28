# EventClient


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.event_client import EventClient

# TODO update the JSON string below
json = "{}"
# create an instance of EventClient from a JSON string
event_client_instance = EventClient.from_json(json)
# print the JSON string representation of the object
print EventClient.to_json()

# convert the object into a dict
event_client_dict = event_client_instance.to_dict()
# create an instance of EventClient from a dict
event_client_form_dict = event_client.from_dict(event_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


