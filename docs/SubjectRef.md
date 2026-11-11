# SubjectRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**slug** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**inherited** | **bool** |  | [optional] 

## Example

```python
from isbnlab.models.subject_ref import SubjectRef

# TODO update the JSON string below
json = "{}"
# create an instance of SubjectRef from a JSON string
subject_ref_instance = SubjectRef.from_json(json)
# print the JSON string representation of the object
print(SubjectRef.to_json())

# convert the object into a dict
subject_ref_dict = subject_ref_instance.to_dict()
# create an instance of SubjectRef from a dict
subject_ref_from_dict = SubjectRef.from_dict(subject_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


