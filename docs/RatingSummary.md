# RatingSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average** | **float** |  | [optional] 
**count** | **int** |  | [optional] 
**sum** | **int** |  | [optional] 

## Example

```python
from isbnlab.models.rating_summary import RatingSummary

# TODO update the JSON string below
json = "{}"
# create an instance of RatingSummary from a JSON string
rating_summary_instance = RatingSummary.from_json(json)
# print the JSON string representation of the object
print(RatingSummary.to_json())

# convert the object into a dict
rating_summary_dict = rating_summary_instance.to_dict()
# create an instance of RatingSummary from a dict
rating_summary_from_dict = RatingSummary.from_dict(rating_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


