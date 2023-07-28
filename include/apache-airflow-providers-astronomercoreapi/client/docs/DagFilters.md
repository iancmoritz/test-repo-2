# DagFilters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployments** | **Dict[str, str]** |  | 
**owners** | **List[str]** |  | 
**tags** | **List[str]** |  | 
**warnings** | **List[str]** |  | [optional] 

## Example

```python
from astronomercoreapi.models.dag_filters import DagFilters

# TODO update the JSON string below
json = "{}"
# create an instance of DagFilters from a JSON string
dag_filters_instance = DagFilters.from_json(json)
# print the JSON string representation of the object
print DagFilters.to_json()

# convert the object into a dict
dag_filters_dict = dag_filters_instance.to_dict()
# create an instance of DagFilters from a dict
dag_filters_form_dict = dag_filters.from_dict(dag_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


