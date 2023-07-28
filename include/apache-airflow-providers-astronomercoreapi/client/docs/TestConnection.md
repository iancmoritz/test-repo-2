# TestConnection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**success** | **bool** |  | 

## Example

```python
from astronomercoreapi.models.test_connection import TestConnection

# TODO update the JSON string below
json = "{}"
# create an instance of TestConnection from a JSON string
test_connection_instance = TestConnection.from_json(json)
# print the JSON string representation of the object
print TestConnection.to_json()

# convert the object into a dict
test_connection_dict = test_connection_instance.to_dict()
# create an instance of TestConnection from a dict
test_connection_form_dict = test_connection.from_dict(test_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


