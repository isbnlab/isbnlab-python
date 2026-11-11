# Ratings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | [**RatingSummary**](RatingSummary.md) |  | [optional] 
**counts** | [**RatingCounts**](RatingCounts.md) |  | [optional] 

## Example

```python
from isbnlab.models.ratings import Ratings

# TODO update the JSON string below
json = "{}"
# create an instance of Ratings from a JSON string
ratings_instance = Ratings.from_json(json)
# print the JSON string representation of the object
print(Ratings.to_json())

# convert the object into a dict
ratings_dict = ratings_instance.to_dict()
# create an instance of Ratings from a dict
ratings_from_dict = Ratings.from_dict(ratings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


