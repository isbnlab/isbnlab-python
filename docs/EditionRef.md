# EditionRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isbn10** | **str** |  | [optional] 
**isbn13** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**published** | **str** |  | [optional] 
**physical_format** | **str** |  | [optional] 
**pages** | **int** |  | [optional] 
**imprint** | **str** |  | [optional] 

## Example

```python
from isbnlab.models.edition_ref import EditionRef

# TODO update the JSON string below
json = "{}"
# create an instance of EditionRef from a JSON string
edition_ref_instance = EditionRef.from_json(json)
# print the JSON string representation of the object
print(EditionRef.to_json())

# convert the object into a dict
edition_ref_dict = edition_ref_instance.to_dict()
# create an instance of EditionRef from a dict
edition_ref_from_dict = EditionRef.from_dict(edition_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


