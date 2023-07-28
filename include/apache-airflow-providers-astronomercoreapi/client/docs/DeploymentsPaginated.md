# DeploymentsPaginated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployments** | [**List[Deployment]**](Deployment.md) |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**total_count** | **int** |  | 

## Example

```python
from astronomercoreapi.models.deployments_paginated import DeploymentsPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentsPaginated from a JSON string
deployments_paginated_instance = DeploymentsPaginated.from_json(json)
# print the JSON string representation of the object
print DeploymentsPaginated.to_json()

# convert the object into a dict
deployments_paginated_dict = deployments_paginated_instance.to_dict()
# create an instance of DeploymentsPaginated from a dict
deployments_paginated_form_dict = deployments_paginated.from_dict(deployments_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


