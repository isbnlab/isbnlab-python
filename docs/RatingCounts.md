# RatingCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_1** | **int** |  | [optional] 
**var_2** | **int** |  | [optional] 
**var_3** | **int** |  | [optional] 
**var_4** | **int** |  | [optional] 
**var_5** | **int** |  | [optional] 

## Example

```python
from isbnlab.models.rating_counts import RatingCounts

# TODO update the JSON string below
json = "{}"
# create an instance of RatingCounts from a JSON string
rating_counts_instance = RatingCounts.from_json(json)
# print the JSON string representation of the object
print(RatingCounts.to_json())

# convert the object into a dict
rating_counts_dict = rating_counts_instance.to_dict()
# create an instance of RatingCounts from a dict
rating_counts_from_dict = RatingCounts.from_dict(rating_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


