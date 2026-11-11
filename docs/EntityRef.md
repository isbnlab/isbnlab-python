# EntityRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**slug** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from isbnlab.models.entity_ref import EntityRef

# TODO update the JSON string below
json = "{}"
# create an instance of EntityRef from a JSON string
entity_ref_instance = EntityRef.from_json(json)
# print the JSON string representation of the object
print(EntityRef.to_json())

# convert the object into a dict
entity_ref_dict = entity_ref_instance.to_dict()
# create an instance of EntityRef from a dict
entity_ref_from_dict = EntityRef.from_dict(entity_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


