# ISBNLab Python client

The official Python client for the [ISBNLab book metadata API](https://www.isbnlab.com/api-information). Look up a book by ISBN and get its title, authors, publishers, series, BISAC genres, formats, page count, description and every other edition, from a catalog of more than 100 million editions. It also validates and converts ISBN-10, ISBN-13, EAN and Amazon ASIN.

## Install

```bash
pip install isbnlab
```

Python 3.9 or later.

## Get an API token

[Create a free ISBNLab account](https://www.isbnlab.com/register) and copy your API token from your profile. The Free plan includes 1,000 calls a day; see [pricing](https://www.isbnlab.com/pricing) for more.

## Quick start

```python
import os
import isbnlab

config = isbnlab.Configuration(access_token=os.environ["ISBNLAB_API_TOKEN"])

with isbnlab.ApiClient(config) as client:
    books = isbnlab.BooksApi(client)
    book = books.get_book_by_isbn("9780765302304")

    print(book.title)               # The Gathering Storm
    print(book.authors[0].name)     # Robert Jordan
    print(book.publish_date.year if book.publish_date else None)

    for edition in book.other_editions or []:
        print(edition.isbn13, edition.title)
```

Many fields are empty for some books, so every field can be `None`. Field names are snake_case (`book.number_of_pages`, `book.other_editions`); `book.to_dict()` gives the API's own camelCase names.

Linked records carry ids you can look up directly (author, publisher, subject and genre lookups need a Standard or Pro plan):

```python
with isbnlab.ApiClient(config) as client:
    book = isbnlab.BooksApi(client).get_book_by_isbn("9780765302304")
    author = isbnlab.AuthorsApi(client).get_author(str(book.authors[0].id))

    print(author.bio)
```

## Errors

Any response other than 2xx raises `isbnlab.ApiException` (or a subclass such as `NotFoundException` or `ForbiddenException`). It carries the HTTP status, the headers, and the response body, whose `detail` explains the reason:

```python
from isbnlab import ApiException

try:
    book = books.get_book_by_isbn("9780000000000")
except ApiException as e:
    if e.status == 404:
        print("Not in the catalog")
    elif e.status == 429:
        print("Daily limit reached; retry after", e.headers.get("Retry-After"), "seconds")
    elif e.status == 403:
        print("Your plan does not include this endpoint")
    else:
        raise
```

## What you can call

| Class | Method | Plan |
|---|---|---|
| `BooksApi` | `get_book_by_isbn(isbn)`, `get_book_by_asin(asin)`, `get_book_by_id(id)` | Free |
| `IsbnApi` | `parse_isbn`, `isbn10_to_isbn13`, `isbn13_to_isbn10`, `isbn_to_ean`, `ean_to_isbn`, `isbn_to_asin`, `asin_to_isbn` | Free |
| `BooksApi` | `get_book_cover_by_isbn(isbn)`, `get_book_cover_by_asin(asin)` | Standard |
| `AuthorsApi` | `get_author(id)`, `find_author(search)` | Standard |
| `PublishersApi` | `get_publisher(id)`, `find_publisher(search)`, `get_publishers_by_prefix(prefix)` | Standard |
| `SubjectsApi` | `get_subject(id)`, `find_subject(search)` | Standard |
| `GenresApi` | `get_genre(id)`, `find_genre(search)` (name or BISAC code) | Standard |
| `BooksApi` | `search_books(query, limit=, page=, max_results=)` | Pro |
| `BooksApi` | `get_editions_by_isbn(isbn)`, `get_editions_by_asin(asin)` | Pro |

Every method also has a `..._with_http_info()` version that returns the status code and headers as well (for example the rate-limit headers).

Reference for every method and model: [docs/](docs/). Field-by-field documentation: [API documentation](https://www.isbnlab.com/api-information).

## Development

`isbnlab/` and `docs/` are generated from the API's [OpenAPI document](https://www.isbnlab.com/api/docs.jsonopenapi) with [OpenAPI Generator](https://openapi-generator.tech/), so changes to them are made in the generator and arrive with the next release; please open an issue rather than a pull request for those folders. `README.md`, `pyproject.toml` and `tests/` are maintained by hand.

```bash
pip install -e ".[test]"
pytest
```

## License

MIT. Maintained by [ISBNLab](https://www.isbnlab.com/), the book metadata API.
