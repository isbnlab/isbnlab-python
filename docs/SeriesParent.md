# SeriesParent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**slug** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from isbnlab.models.series_parent import SeriesParent

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesParent from a JSON string
series_parent_instance = SeriesParent.from_json(json)
# print the JSON string representation of the object
print(SeriesParent.to_json())

# convert the object into a dict
series_parent_dict = series_parent_instance.to_dict()
# create an instance of SeriesParent from a dict
series_parent_from_dict = SeriesParent.from_dict(series_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


