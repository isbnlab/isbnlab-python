# BookEditions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isbn13** | **str** |  | [optional] 
**other_editions** | [**List[EditionRef]**](EditionRef.md) |  | [optional] 
**previous_edition** | [**EditionRef**](EditionRef.md) |  | [optional] 
**next_edition** | [**EditionRef**](EditionRef.md) |  | [optional] 

## Example

```python
from isbnlab.models.book_editions import BookEditions

# TODO update the JSON string below
json = "{}"
# create an instance of BookEditions from a JSON string
book_editions_instance = BookEditions.from_json(json)
# print the JSON string representation of the object
print(BookEditions.to_json())

# convert the object into a dict
book_editions_dict = book_editions_instance.to_dict()
# create an instance of BookEditions from a dict
book_editions_from_dict = BookEditions.from_dict(book_editions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


