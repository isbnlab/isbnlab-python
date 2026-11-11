# RetailLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retailer** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from isbnlab.models.retail_link import RetailLink

# TODO update the JSON string below
json = "{}"
# create an instance of RetailLink from a JSON string
retail_link_instance = RetailLink.from_json(json)
# print the JSON string representation of the object
print(RetailLink.to_json())

# convert the object into a dict
retail_link_dict = retail_link_instance.to_dict()
# create an instance of RetailLink from a dict
retail_link_from_dict = RetailLink.from_dict(retail_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


