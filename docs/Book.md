# Book


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**isbn10** | **str** |  | [optional] 
**isbn13** | **str** |  | [optional] 
**work_id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**subtitle** | **str** |  | [optional] 
**number_of_pages** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**publishers** | [**List[EntityRef]**](EntityRef.md) |  | [optional] 
**imprint** | [**List[EntityRef]**](EntityRef.md) |  | [optional] 
**publish_date** | **datetime** |  | [optional] 
**physical_format** | **str** |  | [optional] 
**covers** | **List[str]** |  | [optional] 
**authors** | [**List[EntityRef]**](EntityRef.md) |  | [optional] 
**contributors** | [**List[Contributor]**](Contributor.md) |  | [optional] 
**subjects** | [**List[SubjectRef]**](SubjectRef.md) |  | [optional] 
**series** | [**Series**](Series.md) |  | [optional] 
**genres** | [**List[EntityRef]**](EntityRef.md) |  | [optional] 
**other_editions** | [**List[EditionRef]**](EditionRef.md) |  | [optional] 
**previous_edition** | [**EditionRef**](EditionRef.md) |  | [optional] 
**next_edition** | [**EditionRef**](EditionRef.md) |  | [optional] 
**physical_dimensions** | **str** |  | [optional] 
**ratings** | [**Ratings**](Ratings.md) |  | [optional] 
**language** | **str** |  | [optional] 
**sale_status** | **str** |  | [optional] 
**excerpt** | **str** |  | [optional] 
**review_quotes** | **str** |  | [optional] 
**retail_links** | [**List[RetailLink]**](RetailLink.md) |  | [optional] 
**categories** | [**List[Category]**](Category.md) |  | [optional] 
**ai_summary** | **str** |  | [optional] 
**canonical_edition_id** | **int** |  | [optional] 
**language_code** | **str** |  | [optional] 
**publish_date_precision** | **str** |  | [optional] 
**estimated_read_time** | **int** |  | [optional] 
**languages_count** | **int** |  | [optional] 
**link** | **str** |  | [optional] 
**isbn_model** | [**IsbnDetails**](IsbnDetails.md) |  | [optional] 

## Example

```python
from isbnlab.models.book import Book

# TODO update the JSON string below
json = "{}"
# create an instance of Book from a JSON string
book_instance = Book.from_json(json)
# print the JSON string representation of the object
print(Book.to_json())

# convert the object into a dict
book_dict = book_instance.to_dict()
# create an instance of Book from a dict
book_from_dict = Book.from_dict(book_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


