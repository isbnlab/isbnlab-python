# Series


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**number** | **int** |  | [optional] 
**kind** | **str** |  | [optional] 
**parent** | [**SeriesParent**](SeriesParent.md) |  | [optional] 
**other_series** | [**List[OtherSeries]**](OtherSeries.md) |  | [optional] 
**previous_book** | [**SeriesBook**](SeriesBook.md) |  | [optional] 
**next_book** | [**SeriesBook**](SeriesBook.md) |  | [optional] 

## Example

```python
from isbnlab.models.series import Series

# TODO update the JSON string below
json = "{}"
# create an instance of Series from a JSON string
series_instance = Series.from_json(json)
# print the JSON string representation of the object
print(Series.to_json())

# convert the object into a dict
series_dict = series_instance.to_dict()
# create an instance of Series from a dict
series_from_dict = Series.from_dict(series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


