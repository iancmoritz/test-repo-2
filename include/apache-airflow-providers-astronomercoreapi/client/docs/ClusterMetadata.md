# ClusterMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_ips** | **List[str]** |  | [optional] 

## Example

```python
from astronomercoreapi.models.cluster_metadata import ClusterMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMetadata from a JSON string
cluster_metadata_instance = ClusterMetadata.from_json(json)
# print the JSON string representation of the object
print ClusterMetadata.to_json()

# convert the object into a dict
cluster_metadata_dict = cluster_metadata_instance.to_dict()
# create an instance of ClusterMetadata from a dict
cluster_metadata_form_dict = cluster_metadata.from_dict(cluster_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


