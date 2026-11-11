# IsbnDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**isbn10** | **str** |  | [optional] 
**isbn10_formatted** | **str** |  | [optional] 
**isbn13** | **str** |  | [optional] 
**isbn13_formatted** | **str** |  | [optional] 
**ean** | **str** |  | [optional] 
**asin** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**registration_group** | **str** |  | [optional] 
**registration_group_name** | **str** |  | [optional] 
**group_identifier** | **str** |  | [optional] 
**registrant** | **str** |  | [optional] 
**publication** | **str** |  | [optional] 
**check_digit** | **str** |  | [optional] 

## Example

```python
from isbnlab.models.isbn_details import IsbnDetails

# TODO update the JSON string below
json = "{}"
# create an instance of IsbnDetails from a JSON string
isbn_details_instance = IsbnDetails.from_json(json)
# print the JSON string representation of the object
print(IsbnDetails.to_json())

# convert the object into a dict
isbn_details_dict = isbn_details_instance.to_dict()
# create an instance of IsbnDetails from a dict
isbn_details_from_dict = IsbnDetails.from_dict(isbn_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


