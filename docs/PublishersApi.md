# isbnlab.PublishersApi

All URIs are relative to *https://www.isbnlab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_publisher**](PublishersApi.md#find_publisher) | **GET** /api/publisher/search/{search} | Find a publisher by name.
[**get_publisher**](PublishersApi.md#get_publisher) | **GET** /api/publisher/{id} | Look up a publisher by id.
[**get_publishers_by_prefix**](PublishersApi.md#get_publishers_by_prefix) | **GET** /api/publisher/prefix/{prefix} | List the publishers that use an ISBN registrant prefix.


# **find_publisher**
> Publisher find_publisher(search)

Find a publisher by name.

### Example

* Api Key Authentication (UrlKey):
* Bearer Authentication (Token):

```python
import isbnlab
from isbnlab.models.publisher import Publisher
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
    api_instance = isbnlab.PublishersApi(api_client)
    search = 'search_example' # str | Name to search for.

    try:
        # Find a publisher by name.
        api_response = api_instance.find_publisher(search)
        print("The response of PublishersApi->find_publisher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublishersApi->find_publisher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Name to search for. | 

### Return type

[**Publisher**](Publisher.md)

### Authorization

[UrlKey](../README.md#UrlKey), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Publisher resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_publisher**
> Publisher get_publisher(id)

Look up a publisher by id.

### Example

* Api Key Authentication (UrlKey):
* Bearer Authentication (Token):

```python
import isbnlab
from isbnlab.models.publisher import Publisher
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
    api_instance = isbnlab.PublishersApi(api_client)
    id = 'id_example' # str | Publisher identifier

    try:
        # Look up a publisher by id.
        api_response = api_instance.get_publisher(id)
        print("The response of PublishersApi->get_publisher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublishersApi->get_publisher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Publisher identifier | 

### Return type

[**Publisher**](Publisher.md)

### Authorization

[UrlKey](../README.md#UrlKey), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Publisher resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_publishers_by_prefix**
> List[Publisher] get_publishers_by_prefix(prefix, page=page)

List the publishers that use an ISBN registrant prefix.

### Example

* Api Key Authentication (UrlKey):
* Bearer Authentication (Token):

```python
import isbnlab
from isbnlab.models.publisher import Publisher
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
    api_instance = isbnlab.PublishersApi(api_client)
    prefix = 'prefix_example' # str | ISBN registrant prefix, for example 978-0-7653.
    page = 1 # int | The collection page number (optional) (default to 1)

    try:
        # List the publishers that use an ISBN registrant prefix.
        api_response = api_instance.get_publishers_by_prefix(prefix, page=page)
        print("The response of PublishersApi->get_publishers_by_prefix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublishersApi->get_publishers_by_prefix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| ISBN registrant prefix, for example 978-0-7653. | 
 **page** | **int**| The collection page number | [optional] [default to 1]

### Return type

[**List[Publisher]**](Publisher.md)

### Authorization

[UrlKey](../README.md#UrlKey), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Publisher collection |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

