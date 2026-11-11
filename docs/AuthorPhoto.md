# AuthorPhoto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 
**credit** | **str** |  | [optional] 
**license** | **str** |  | [optional] 
**license_url** | **str** |  | [optional] 

## Example

```python
from isbnlab.models.author_photo import AuthorPhoto

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorPhoto from a JSON string
author_photo_instance = AuthorPhoto.from_json(json)
# print the JSON string representation of the object
print(AuthorPhoto.to_json())

# convert the object into a dict
author_photo_dict = author_photo_instance.to_dict()
# create an instance of AuthorPhoto from a dict
author_photo_from_dict = AuthorPhoto.from_dict(author_photo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


