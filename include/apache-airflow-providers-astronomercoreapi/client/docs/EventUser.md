# EventUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_metadata** | **Dict[str, object]** |  | [optional] 
**created_at** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**email_verified** | **bool** |  | [optional] 
**family_name** | **str** |  | [optional] 
**given_name** | **str** |  | [optional] 
**identities** | **List[object]** |  | [optional] 
**last_password_reset** | **str** |  | [optional] 
**multifactor** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**nickname** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**phone_verified** | **bool** |  | [optional] 
**picture** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**user_metadata** | **Dict[str, object]** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.event_user import EventUser

# TODO update the JSON string below
json = "{}"
# create an instance of EventUser from a JSON string
event_user_instance = EventUser.from_json(json)
# print the JSON string representation of the object
print EventUser.to_json()

# convert the object into a dict
event_user_dict = event_user_instance.to_dict()
# create an instance of EventUser from a dict
event_user_form_dict = event_user.from_dict(event_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


