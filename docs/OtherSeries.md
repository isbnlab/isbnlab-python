# OtherSeries


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

## Example

```python
from isbnlab.models.other_series import OtherSeries

# TODO update the JSON string below
json = "{}"
# create an instance of OtherSeries from a JSON string
other_series_instance = OtherSeries.from_json(json)
# print the JSON string representation of the object
print(OtherSeries.to_json())

# convert the object into a dict
other_series_dict = other_series_instance.to_dict()
# create an instance of OtherSeries from a dict
other_series_from_dict = OtherSeries.from_dict(other_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


