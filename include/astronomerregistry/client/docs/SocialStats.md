# SocialStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stars** | **int** |  | [optional] 
**views** | **int** |  | [optional] 

## Example

```python
from astronomerregistry.models.social_stats import SocialStats

# TODO update the JSON string below
json = "{}"
# create an instance of SocialStats from a JSON string
social_stats_instance = SocialStats.from_json(json)
# print the JSON string representation of the object
print SocialStats.to_json()

# convert the object into a dict
social_stats_dict = social_stats_instance.to_dict()
# create an instance of SocialStats from a dict
social_stats_form_dict = social_stats.from_dict(social_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


