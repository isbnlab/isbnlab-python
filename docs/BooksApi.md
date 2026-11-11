# isbnlab.BooksApi

All URIs are relative to *https://www.isbnlab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_book_by_asin**](BooksApi.md#get_book_by_asin) | **GET** /api/book/asin/{asin} | Look up a book by Amazon ASIN.
[**get_book_by_id**](BooksApi.md#get_book_by_id) | **GET** /api/book/{id} | Look up a book by ISBNLab book id.
[**get_book_by_isbn**](BooksApi.md#get_book_by_isbn) | **GET** /api/book/isbn/{isbn} | Look up a book by ISBN-10 or ISBN-13.
[**get_book_cover_by_asin**](BooksApi.md#get_book_cover_by_asin) | **GET** /api/book/cover/asin/{asin} | Get the cover image URLs for a book by ASIN.
[**get_book_cover_by_isbn**](BooksApi.md#get_book_cover_by_isbn) | **GET** /api/book/cover/isbn/{isbn} | Get the cover image URLs for a book by ISBN.
[**get_editions_by_asin**](BooksApi.md#get_editions_by_asin) | **GET** /api/editions/asin/{asin} | Get every other edition of a book by ASIN.
[**get_editions_by_isbn**](BooksApi.md#get_editions_by_isbn) | **GET** /api/editions/isbn/{isbn} | Get every other edition of a book by ISBN.
[**search_books**](BooksApi.md#search_books) | **GET** /api/search/book/{query} | Search books by title, subtitle, author or ISBN.


# **get_book_by_asin**
> Book get_book_by_asin(asin)

Look up a book by Amazon ASIN.

### Example

* Api Key Authentication (UrlKey):
* Bearer Authentication (Token):

```python
import isbnlab
from isbnlab.models.book import Book
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
    api_instance = isbnlab.BooksApi(api_client)
    asin = 'asin_example' # str | ASIN identifier

    try:
        # Look up a book by Amazon ASIN.
        api_response = api_instance.get_book_by_asin(asin)
        print("The response of BooksApi->get_book_by_asin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BooksApi->get_book_by_asin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asin** | **str**| ASIN identifier | 

### Return type

[**Book**](Book.md)

### Authorization

[UrlKey](../README.md#UrlKey), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Book resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_book_by_id**
> Book get_book_by_id(id)

Look up a book by ISBNLab book id.

### Example

* Api Key Authentication (UrlKey):
* Bearer Authentication (Token):

```python
import isbnlab
from isbnlab.models.book import Book
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
    api_instance = isbnlab.BooksApi(api_client)
    id = 'id_example' # str | Book identifier

    try:
        # Look up a book by ISBNLab book id.
        api_response = api_instance.get_book_by_id(id)
        print("The response of BooksApi->get_book_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BooksApi->get_book_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Book identifier | 

### Return type

[**Book**](Book.md)

### Authorization

[UrlKey](../README.md#UrlKey), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Book resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_book_by_isbn**
> Book get_book_by_isbn(isbn)

Look up a book by ISBN-10 or ISBN-13.

### Example

* Api Key Authentication (UrlKey):
* Bearer Authentication (Token):

```python
import isbnlab
from isbnlab.models.book import Book
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
    api_instance = isbnlab.BooksApi(api_client)
    isbn = 'isbn_example' # str | ISBN identifier

    try:
        # Look up a book by ISBN-10 or ISBN-13.
        api_response = api_instance.get_book_by_isbn(isbn)
        print("The response of BooksApi->get_book_by_isbn:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BooksApi->get_book_by_isbn: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **isbn** | **str**| ISBN identifier | 

### Return type

[**Book**](Book.md)

### Authorization

[UrlKey](../README.md#UrlKey), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Book resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_book_cover_by_asin**
> BookCover get_book_cover_by_asin(asin)

Get the cover image URLs for a book by ASIN.

### Example

* Api Key Authentication (UrlKey):
* Bearer Authentication (Token):

```python
import isbnlab
from isbnlab.models.book_cover import BookCover
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
    api_instance = isbnlab.BooksApi(api_client)
    asin = 'asin_example' # str | ASIN identifier

    try:
        # Get the cover image URLs for a book by ASIN.
        api_response = api_instance.get_book_cover_by_asin(asin)
        print("The response of BooksApi->get_book_cover_by_asin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BooksApi->get_book_cover_by_asin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asin** | **str**| ASIN identifier | 

### Return type

[**BookCover**](BookCover.md)

### Authorization

[UrlKey](../README.md#UrlKey), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Book Cover resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_book_cover_by_isbn**
> BookCover get_book_cover_by_isbn(isbn)

Get the cover image URLs for a book by ISBN.

### Example

* Api Key Authentication (UrlKey):
* Bearer Authentication (Token):

```python
import isbnlab
from isbnlab.models.book_cover import BookCover
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
    api_instance = isbnlab.BooksApi(api_client)
    isbn = 'isbn_example' # str | ISBN identifier

    try:
        # Get the cover image URLs for a book by ISBN.
        api_response = api_instance.get_book_cover_by_isbn(isbn)
        print("The response of BooksApi->get_book_cover_by_isbn:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BooksApi->get_book_cover_by_isbn: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **isbn** | **str**| ISBN identifier | 

### Return type

[**BookCover**](BookCover.md)

### Authorization

[UrlKey](../README.md#UrlKey), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Book Cover resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_editions_by_asin**
> BookEditions get_editions_by_asin(asin)

Get every other edition of a book by ASIN.

### Example

* Api Key Authentication (UrlKey):
* Bearer Authentication (Token):

```python
import isbnlab
from isbnlab.models.book_editions import BookEditions
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
    api_instance = isbnlab.BooksApi(api_client)
    asin = 'asin_example' # str | ASIN identifier

    try:
        # Get every other edition of a book by ASIN.
        api_response = api_instance.get_editions_by_asin(asin)
        print("The response of BooksApi->get_editions_by_asin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BooksApi->get_editions_by_asin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asin** | **str**| ASIN identifier | 

### Return type

[**BookEditions**](BookEditions.md)

### Authorization

[UrlKey](../README.md#UrlKey), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Book Other Editions resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_editions_by_isbn**
> BookEditions get_editions_by_isbn(isbn)

Get every other edition of a book by ISBN.

### Example

* Api Key Authentication (UrlKey):
* Bearer Authentication (Token):

```python
import isbnlab
from isbnlab.models.book_editions import BookEditions
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
    api_instance = isbnlab.BooksApi(api_client)
    isbn = 'isbn_example' # str | ISBN identifier

    try:
        # Get every other edition of a book by ISBN.
        api_response = api_instance.get_editions_by_isbn(isbn)
        print("The response of BooksApi->get_editions_by_isbn:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BooksApi->get_editions_by_isbn: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **isbn** | **str**| ISBN identifier | 

### Return type

[**BookEditions**](BookEditions.md)

### Authorization

[UrlKey](../README.md#UrlKey), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Book Other Editions resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_books**
> List[Book] search_books(query, limit=limit, page=page, max_results=max_results)

Search books by title, subtitle, author or ISBN.

### Example

* Api Key Authentication (UrlKey):
* Bearer Authentication (Token):

```python
import isbnlab
from isbnlab.models.book import Book
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
    api_instance = isbnlab.BooksApi(api_client)
    query = 'query_example' # str | Search text
    limit = 10 # int | Books per page, 1-100. Default 10. (optional) (default to 10)
    page = 1 # int | Page number, starting at 1. Default 1. (optional) (default to 1)
    max_results = 100 # int | Maximum number of results across all pages. Default 100. (optional) (default to 100)

    try:
        # Search books by title, subtitle, author or ISBN.
        api_response = api_instance.search_books(query, limit=limit, page=page, max_results=max_results)
        print("The response of BooksApi->search_books:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BooksApi->search_books: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search text | 
 **limit** | **int**| Books per page, 1-100. Default 10. | [optional] [default to 10]
 **page** | **int**| Page number, starting at 1. Default 1. | [optional] [default to 1]
 **max_results** | **int**| Maximum number of results across all pages. Default 100. | [optional] [default to 100]

### Return type

[**List[Book]**](Book.md)

### Authorization

[UrlKey](../README.md#UrlKey), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Book collection |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

