# BookCover


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isbn13** | **str** |  | [optional] 
**covers** | **List[str]** |  | [optional] 

## Example

```python
from isbnlab.models.book_cover import BookCover

# TODO update the JSON string below
json = "{}"
# create an instance of BookCover from a JSON string
book_cover_instance = BookCover.from_json(json)
# print the JSON string representation of the object
print(BookCover.to_json())

# convert the object into a dict
book_cover_dict = book_cover_instance.to_dict()
# create an instance of BookCover from a dict
book_cover_from_dict = BookCover.from_dict(book_cover_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


