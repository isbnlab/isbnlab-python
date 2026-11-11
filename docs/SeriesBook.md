# SeriesBook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isbn10** | **str** |  | [optional] 
**isbn13** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**number** | **int** |  | [optional] 
**work_id** | **int** |  | [optional] 
**work_slug** | **str** |  | [optional] 

## Example

```python
from isbnlab.models.series_book import SeriesBook

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesBook from a JSON string
series_book_instance = SeriesBook.from_json(json)
# print the JSON string representation of the object
print(SeriesBook.to_json())

# convert the object into a dict
series_book_dict = series_book_instance.to_dict()
# create an instance of SeriesBook from a dict
series_book_from_dict = SeriesBook.from_dict(series_book_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


