# TestConnectionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra** | **Dict[str, str]** |  | [optional] 
**host** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**login** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**var_schema** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from astronomercoreapi.models.test_connection_request import TestConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestConnectionRequest from a JSON string
test_connection_request_instance = TestConnectionRequest.from_json(json)
# print the JSON string representation of the object
print TestConnectionRequest.to_json()

# convert the object into a dict
test_connection_request_dict = test_connection_request_instance.to_dict()
# create an instance of TestConnectionRequest from a dict
test_connection_request_form_dict = test_connection_request.from_dict(test_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


