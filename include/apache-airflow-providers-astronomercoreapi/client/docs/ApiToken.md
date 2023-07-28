# ApiToken


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**created_by** | [**BasicSubjectProfile**](BasicSubjectProfile.md) |  | [optional] 
**created_by_id** | **str** |  | 
**deleted_at** | **datetime** |  | [optional] 
**description** | **str** |  | 
**end_at** | **datetime** |  | [optional] 
**expiry_period_in_days** | **int** |  | 
**id** | **str** |  | 
**last_used_at** | **datetime** |  | [optional] 
**name** | **str** |  | 
**roles** | [**List[ApiTokenRole]**](ApiTokenRole.md) |  | 
**short_token** | **str** |  | 
**start_at** | **datetime** |  | 
**token** | **str** |  | [optional] 
**type** | **str** |  | 
**updated_at** | **datetime** |  | 
**updated_by** | [**BasicSubjectProfile**](BasicSubjectProfile.md) |  | [optional] 
**updated_by_id** | **str** |  | 

## Example

```python
from astronomercoreapi.models.api_token import ApiToken

# TODO update the JSON string below
json = "{}"
# create an instance of ApiToken from a JSON string
api_token_instance = ApiToken.from_json(json)
# print the JSON string representation of the object
print ApiToken.to_json()

# convert the object into a dict
api_token_dict = api_token_instance.to_dict()
# create an instance of ApiToken from a dict
api_token_form_dict = api_token.from_dict(api_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


