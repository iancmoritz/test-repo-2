# PermissionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 

## Example

```python
from astronomercoreapi.models.permission_request import PermissionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionRequest from a JSON string
permission_request_instance = PermissionRequest.from_json(json)
# print the JSON string representation of the object
print PermissionRequest.to_json()

# convert the object into a dict
permission_request_dict = permission_request_instance.to_dict()
# create an instance of PermissionRequest from a dict
permission_request_form_dict = permission_request.from_dict(permission_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


