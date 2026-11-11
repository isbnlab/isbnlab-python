# isbnlab.IsbnApi

All URIs are relative to *https://www.isbnlab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asin_to_isbn**](IsbnApi.md#asin_to_isbn) | **GET** /api/isbn/asin-to-isbn/{asin} | Convert an Amazon ASIN to ISBN.
[**ean_to_isbn**](IsbnApi.md#ean_to_isbn) | **GET** /api/isbn/ean-to-isbn/{ean} | Convert an EAN to ISBN.
[**isbn10_to_isbn13**](IsbnApi.md#isbn10_to_isbn13) | **GET** /api/isbn/isbn10-to-isbn13/{isbn10} | Convert an ISBN-10 to ISBN-13.
[**isbn13_to_isbn10**](IsbnApi.md#isbn13_to_isbn10) | **GET** /api/isbn/isbn13-to-isbn10/{isbn13} | Convert an ISBN-13 to ISBN-10.
[**isbn_to_asin**](IsbnApi.md#isbn_to_asin) | **GET** /api/isbn/isbn-to-asin/{isbn} | Convert an ISBN to Amazon ASIN.
[**isbn_to_ean**](IsbnApi.md#isbn_to_ean) | **GET** /api/isbn/isbn-to-ean/{isbn} | Convert an ISBN to EAN.
[**parse_isbn**](IsbnApi.md#parse_isbn) | **GET** /api/isbn/isbn-lookup/{isbn} | Validate an ISBN and split it into its parts.


# **asin_to_isbn**
> IsbnDetails asin_to_isbn(asin)

Convert an Amazon ASIN to ISBN.

### Example

* Api Key Authentication (UrlKey):
* Bearer Authentication (Token):

```python
import isbnlab
from isbnlab.models.isbn_details import IsbnDetails
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
    api_instance = isbnlab.IsbnApi(api_client)
    asin = 'asin_example' # str | ASIN

    try:
        # Convert an Amazon ASIN to ISBN.
        api_response = api_instance.asin_to_isbn(asin)
        print("The response of IsbnApi->asin_to_isbn:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IsbnApi->asin_to_isbn: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asin** | **str**| ASIN | 

### Return type

[**IsbnDetails**](IsbnDetails.md)

### Authorization

[UrlKey](../README.md#UrlKey), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ISBN Tools API resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ean_to_isbn**
> IsbnDetails ean_to_isbn(ean)

Convert an EAN to ISBN.

### Example

* Api Key Authentication (UrlKey):
* Bearer Authentication (Token):

```python
import isbnlab
from isbnlab.models.isbn_details import IsbnDetails
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
    api_instance = isbnlab.IsbnApi(api_client)
    ean = 'ean_example' # str | EAN

    try:
        # Convert an EAN to ISBN.
        api_response = api_instance.ean_to_isbn(ean)
        print("The response of IsbnApi->ean_to_isbn:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IsbnApi->ean_to_isbn: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ean** | **str**| EAN | 

### Return type

[**IsbnDetails**](IsbnDetails.md)

### Authorization

[UrlKey](../README.md#UrlKey), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ISBN Tools API resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **isbn10_to_isbn13**
> IsbnDetails isbn10_to_isbn13(isbn10)

Convert an ISBN-10 to ISBN-13.

### Example

* Api Key Authentication (UrlKey):
* Bearer Authentication (Token):

```python
import isbnlab
from isbnlab.models.isbn_details import IsbnDetails
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
    api_instance = isbnlab.IsbnApi(api_client)
    isbn10 = 'isbn10_example' # str | ISBN-10

    try:
        # Convert an ISBN-10 to ISBN-13.
        api_response = api_instance.isbn10_to_isbn13(isbn10)
        print("The response of IsbnApi->isbn10_to_isbn13:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IsbnApi->isbn10_to_isbn13: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **isbn10** | **str**| ISBN-10 | 

### Return type

[**IsbnDetails**](IsbnDetails.md)

### Authorization

[UrlKey](../README.md#UrlKey), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ISBN Tools API resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **isbn13_to_isbn10**
> IsbnDetails isbn13_to_isbn10(isbn13)

Convert an ISBN-13 to ISBN-10.

### Example

* Api Key Authentication (UrlKey):
* Bearer Authentication (Token):

```python
import isbnlab
from isbnlab.models.isbn_details import IsbnDetails
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
    api_instance = isbnlab.IsbnApi(api_client)
    isbn13 = 'isbn13_example' # str | ISBN-13

    try:
        # Convert an ISBN-13 to ISBN-10.
        api_response = api_instance.isbn13_to_isbn10(isbn13)
        print("The response of IsbnApi->isbn13_to_isbn10:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IsbnApi->isbn13_to_isbn10: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **isbn13** | **str**| ISBN-13 | 

### Return type

[**IsbnDetails**](IsbnDetails.md)

### Authorization

[UrlKey](../README.md#UrlKey), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ISBN Tools API resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **isbn_to_asin**
> IsbnDetails isbn_to_asin(isbn)

Convert an ISBN to Amazon ASIN.

### Example

* Api Key Authentication (UrlKey):
* Bearer Authentication (Token):

```python
import isbnlab
from isbnlab.models.isbn_details import IsbnDetails
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
    api_instance = isbnlab.IsbnApi(api_client)
    isbn = 'isbn_example' # str | ISBN

    try:
        # Convert an ISBN to Amazon ASIN.
        api_response = api_instance.isbn_to_asin(isbn)
        print("The response of IsbnApi->isbn_to_asin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IsbnApi->isbn_to_asin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **isbn** | **str**| ISBN | 

### Return type

[**IsbnDetails**](IsbnDetails.md)

### Authorization

[UrlKey](../README.md#UrlKey), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ISBN Tools API resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **isbn_to_ean**
> IsbnDetails isbn_to_ean(isbn)

Convert an ISBN to EAN.

### Example

* Api Key Authentication (UrlKey):
* Bearer Authentication (Token):

```python
import isbnlab
from isbnlab.models.isbn_details import IsbnDetails
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
    api_instance = isbnlab.IsbnApi(api_client)
    isbn = 'isbn_example' # str | ISBN

    try:
        # Convert an ISBN to EAN.
        api_response = api_instance.isbn_to_ean(isbn)
        print("The response of IsbnApi->isbn_to_ean:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IsbnApi->isbn_to_ean: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **isbn** | **str**| ISBN | 

### Return type

[**IsbnDetails**](IsbnDetails.md)

### Authorization

[UrlKey](../README.md#UrlKey), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ISBN Tools API resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_isbn**
> IsbnDetails parse_isbn(isbn)

Validate an ISBN and split it into its parts.

### Example

* Api Key Authentication (UrlKey):
* Bearer Authentication (Token):

```python
import isbnlab
from isbnlab.models.isbn_details import IsbnDetails
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
    api_instance = isbnlab.IsbnApi(api_client)
    isbn = 'isbn_example' # str | ISBN

    try:
        # Validate an ISBN and split it into its parts.
        api_response = api_instance.parse_isbn(isbn)
        print("The response of IsbnApi->parse_isbn:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IsbnApi->parse_isbn: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **isbn** | **str**| ISBN | 

### Return type

[**IsbnDetails**](IsbnDetails.md)

### Authorization

[UrlKey](../README.md#UrlKey), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ISBN Tools API resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

