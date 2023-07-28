# ModelSelf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_url** | **str** |  | 
**color_mode_preference** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**feature_flags** | [**List[FeatureFlag]**](FeatureFlag.md) |  | [optional] 
**full_name** | **str** |  | 
**id** | **str** |  | 
**intercom_user_hash** | **str** |  | [optional] 
**invites** | [**List[Invite]**](Invite.md) |  | [optional] 
**organization_id** | **str** |  | [optional] 
**roles** | [**List[UserRole]**](UserRole.md) |  | [optional] 
**status** | **str** |  | 
**system_role** | **str** |  | [optional] 
**updated_at** | **datetime** |  | 
**username** | **str** |  | 

## Example

```python
from astronomercoreapi.models.model_self import ModelSelf

# TODO update the JSON string below
json = "{}"
# create an instance of ModelSelf from a JSON string
model_self_instance = ModelSelf.from_json(json)
# print the JSON string representation of the object
print ModelSelf.to_json()

# convert the object into a dict
model_self_dict = model_self_instance.to_dict()
# create an instance of ModelSelf from a dict
model_self_form_dict = model_self.from_dict(model_self_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


