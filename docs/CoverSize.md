# CoverSize


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**w200** | **str** |  | [optional] 
**w400** | **str** |  | [optional] 
**w800** | **str** |  | [optional] 

## Example

```python
from isbnlab.models.cover_size import CoverSize

# TODO update the JSON string below
json = "{}"
# create an instance of CoverSize from a JSON string
cover_size_instance = CoverSize.from_json(json)
# print the JSON string representation of the object
print(CoverSize.to_json())

# convert the object into a dict
cover_size_dict = cover_size_instance.to_dict()
# create an instance of CoverSize from a dict
cover_size_from_dict = CoverSize.from_dict(cover_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


