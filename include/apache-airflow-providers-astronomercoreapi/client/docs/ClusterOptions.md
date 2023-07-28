# ClusterOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_instances** | [**List[ProviderInstanceType]**](ProviderInstanceType.md) |  | 
**default_database_instance** | [**ProviderInstanceType**](ProviderInstanceType.md) |  | 
**default_node_instance** | [**ProviderInstanceType**](ProviderInstanceType.md) |  | 
**default_pod_subnet_range** | **str** |  | [optional] 
**default_region** | [**ProviderRegion**](ProviderRegion.md) |  | 
**default_service_peering_range** | **str** |  | [optional] 
**default_service_subnet_range** | **str** |  | [optional] 
**default_vpc_subnet_range** | **str** |  | 
**node_count_default** | **int** |  | 
**node_count_max** | **int** |  | 
**node_count_min** | **int** |  | 
**node_instances** | [**List[ProviderInstanceType]**](ProviderInstanceType.md) |  | 
**provider** | **str** |  | 
**regions** | [**List[ProviderRegion]**](ProviderRegion.md) |  | 
**template_versions** | [**List[TemplateVersion]**](TemplateVersion.md) |  | 

## Example

```python
from astronomercoreapi.models.cluster_options import ClusterOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterOptions from a JSON string
cluster_options_instance = ClusterOptions.from_json(json)
# print the JSON string representation of the object
print ClusterOptions.to_json()

# convert the object into a dict
cluster_options_dict = cluster_options_instance.to_dict()
# create an instance of ClusterOptions from a dict
cluster_options_form_dict = cluster_options.from_dict(cluster_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


