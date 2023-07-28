# RuntimeRelease


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**airflow_database_migration** | **bool** |  | 
**airflow_version** | **str** |  | 
**channel** | **str** |  | 
**release_date** | **str** |  | 
**stellar_database_migration** | **bool** |  | 
**version** | **str** |  | 

## Example

```python
from astronomercoreapi.models.runtime_release import RuntimeRelease

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeRelease from a JSON string
runtime_release_instance = RuntimeRelease.from_json(json)
# print the JSON string representation of the object
print RuntimeRelease.to_json()

# convert the object into a dict
runtime_release_dict = runtime_release_instance.to_dict()
# create an instance of RuntimeRelease from a dict
runtime_release_form_dict = runtime_release.from_dict(runtime_release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


