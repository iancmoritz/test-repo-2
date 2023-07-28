# EventRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **Dict[str, object]** |  | [optional] 
**geoip** | **object** |  | [optional] 
**hostname** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**query** | **Dict[str, object]** |  | [optional] 
**user_agent** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.event_request import EventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EventRequest from a JSON string
event_request_instance = EventRequest.from_json(json)
# print the JSON string representation of the object
print EventRequest.to_json()

# convert the object into a dict
event_request_dict = event_request_instance.to_dict()
# create an instance of EventRequest from a dict
event_request_form_dict = event_request.from_dict(event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


