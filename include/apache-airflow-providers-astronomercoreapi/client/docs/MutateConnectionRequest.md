# MutateConnectionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_name** | **str** |  | 
**extra** | **Dict[str, str]** |  | [optional] 
**host** | **str** |  | [optional] 
**login** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**var_schema** | **str** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from astronomercoreapi.models.mutate_connection_request import MutateConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MutateConnectionRequest from a JSON string
mutate_connection_request_instance = MutateConnectionRequest.from_json(json)
# print the JSON string representation of the object
print MutateConnectionRequest.to_json()

# convert the object into a dict
mutate_connection_request_dict = mutate_connection_request_instance.to_dict()
# create an instance of MutateConnectionRequest from a dict
mutate_connection_request_form_dict = mutate_connection_request.from_dict(mutate_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


