# InternalMappedTaskInstanceSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **str** |  | [optional] 
**overall_state** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**states** | **Dict[str, int]** |  | [optional] 
**task_id** | **str** |  | [optional] 
**try_number** | **int** |  | [optional] 

## Example

```python
from astronomercoreapi.models.internal_mapped_task_instance_summary import InternalMappedTaskInstanceSummary

# TODO update the JSON string below
json = "{}"
# create an instance of InternalMappedTaskInstanceSummary from a JSON string
internal_mapped_task_instance_summary_instance = InternalMappedTaskInstanceSummary.from_json(json)
# print the JSON string representation of the object
print InternalMappedTaskInstanceSummary.to_json()

# convert the object into a dict
internal_mapped_task_instance_summary_dict = internal_mapped_task_instance_summary_instance.to_dict()
# create an instance of InternalMappedTaskInstanceSummary from a dict
internal_mapped_task_instance_summary_form_dict = internal_mapped_task_instance_summary.from_dict(internal_mapped_task_instance_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


