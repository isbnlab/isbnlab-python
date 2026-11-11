# isbnlab.GenresApi

All URIs are relative to *https://www.isbnlab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_genre**](GenresApi.md#find_genre) | **GET** /api/genre/search/{search} | Find a BISAC genre by name or BISAC code.
[**get_genre**](GenresApi.md#get_genre) | **GET** /api/genre/{id} | Look up a BISAC genre by id.


# **find_genre**
> Genre find_genre(search)

Find a BISAC genre by name or BISAC code.

### Example

* Api Key Authentication (UrlKey):
* Bearer Authentication (Token):

```python
import isbnlab
from isbnlab.models.genre import Genre
from isbnlab.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.isbnlab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = isbnlab.Configuration(
    host = "https://www.isbnlab.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: UrlKey
configuration.api_key['UrlKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['UrlKey'] = 'Bearer'

# Configure Bearer authorization: Token
configuration = isbnlab.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with isbnlab.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = isbnlab.GenresApi(api_client)
    search = 'search_example' # str | Name to search for.

    try:
        # Find a BISAC genre by name or BISAC code.
        api_response = api_instance.find_genre(search)
        print("The response of GenresApi->find_genre:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenresApi->find_genre: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Name to search for. | 

### Return type

[**Genre**](Genre.md)

### Authorization

[UrlKey](../README.md#UrlKey), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Genre resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_genre**
> Genre get_genre(id)

Look up a BISAC genre by id.

### Example

* Api Key Authentication (UrlKey):
* Bearer Authentication (Token):

```python
import isbnlab
from isbnlab.models.genre import Genre
from isbnlab.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.isbnlab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = isbnlab.Configuration(
    host = "https://www.isbnlab.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: UrlKey
configuration.api_key['UrlKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['UrlKey'] = 'Bearer'

# Configure Bearer authorization: Token
configuration = isbnlab.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with isbnlab.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = isbnlab.GenresApi(api_client)
    id = 'id_example' # str | Genre identifier

    try:
        # Look up a BISAC genre by id.
        api_response = api_instance.get_genre(id)
        print("The response of GenresApi->get_genre:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenresApi->get_genre: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Genre identifier | 

### Return type

[**Genre**](Genre.md)

### Authorization

[UrlKey](../README.md#UrlKey), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Genre resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

