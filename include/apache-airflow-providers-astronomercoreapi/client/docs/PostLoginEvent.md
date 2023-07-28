# PostLoginEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client** | [**EventClient**](EventClient.md) |  | [optional] 
**connection** | [**EventConnection**](EventConnection.md) |  | 
**organization** | [**EventOrganization**](EventOrganization.md) |  | [optional] 
**request** | [**EventRequest**](EventRequest.md) |  | [optional] 
**transaction** | **Dict[str, object]** |  | [optional] 
**user** | [**EventUser**](EventUser.md) |  | 

## Example

```python
from astronomercoreapi.models.post_login_event import PostLoginEvent

# TODO update the JSON string below
json = "{}"
# create an instance of PostLoginEvent from a JSON string
post_login_event_instance = PostLoginEvent.from_json(json)
# print the JSON string representation of the object
print PostLoginEvent.to_json()

# convert the object into a dict
post_login_event_dict = post_login_event_instance.to_dict()
# create an instance of PostLoginEvent from a dict
post_login_event_form_dict = post_login_event.from_dict(post_login_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


