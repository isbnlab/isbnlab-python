# Genre


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bisac_code** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**edition_count** | **int** |  | [optional] 

## Example

```python
from isbnlab.models.genre import Genre

# TODO update the JSON string below
json = "{}"
# create an instance of Genre from a JSON string
genre_instance = Genre.from_json(json)
# print the JSON string representation of the object
print(Genre.to_json())

# convert the object into a dict
genre_dict = genre_instance.to_dict()
# create an instance of Genre from a dict
genre_from_dict = Genre.from_dict(genre_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


