# Author


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**alternative_names** | **List[str]** |  | [optional] 
**death_date** | **datetime** |  | [optional] 
**birth_date** | **datetime** |  | [optional] 
**bio** | **str** |  | [optional] 
**photos** | [**List[AuthorPhoto]**](AuthorPhoto.md) |  | [optional] 

## Example

```python
from isbnlab.models.author import Author

# TODO update the JSON string below
json = "{}"
# create an instance of Author from a JSON string
author_instance = Author.from_json(json)
# print the JSON string representation of the object
print(Author.to_json())

# convert the object into a dict
author_dict = author_instance.to_dict()
# create an instance of Author from a dict
author_from_dict = Author.from_dict(author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


