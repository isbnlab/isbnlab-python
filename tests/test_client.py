from __future__ import annotations

import pytest

import isbnlab
from isbnlab import AuthorsApi, BooksApi, GenresApi, IsbnApi, PublishersApi, SubjectsApi
from isbnlab.exceptions import ApiException, ForbiddenException, NotFoundException


def test_book_by_isbn_sends_bearer_token_and_reads_every_part(respond):
    client, pool = respond("book.json")

    book = BooksApi(client).get_book_by_isbn("9780765302304")

    assert pool.last["method"] == "GET"
    assert pool.last_path == "/api/book/isbn/9780765302304"
    assert pool.last["headers"]["Authorization"] == "Bearer test-token"
    assert pool.last["headers"]["Accept"] == "application/json"

    assert isinstance(book, isbnlab.Book)
    assert book.id == 15596406
    assert book.title == "The Gathering Storm"
    assert book.authors[0].name == "Robert Jordan"
    assert book.authors[0].id == 3705408
    assert book.publish_date.year == 2009
    assert book.series.name == "Wheel of time"
    assert book.series.number == 12
    assert book.series.next_book.title == "Memory of Light"
    assert all(isinstance(e, isbnlab.EditionRef) for e in book.other_editions)
    assert book.isbn_model.isbn10_formatted == "0-7653-0230-6"


def test_a_book_with_most_fields_empty_still_loads(respond):
    client, _ = respond("book-sparse.json")

    book = BooksApi(client).get_book_by_isbn("9780000000002")

    assert book.title == "A Sparse Book"
    assert book.ratings is None
    assert book.contributors is None
    assert book.publish_date is None
    assert book.series is None
    assert book.authors == []


def test_values_the_api_adds_later_do_not_break_loading(respond):
    client, _ = respond(body={
        "isbn13": "9780000000002",
        "title": "New Values",
        "publishDatePrecision": "season",
        "contributors": [{"name": "A. Person", "role": "foreword"}],
        "series": {"name": "Some Series", "kind": "anthology", "otherSeries": []},
    })

    book = BooksApi(client).get_book_by_isbn("9780000000002")

    assert book.publish_date_precision == "season"
    assert book.contributors[0].role == "foreword"
    assert book.series.kind == "anthology"


def test_search_sends_paging_parameters(respond):
    client, pool = respond("book-search.json")

    books = BooksApi(client).search_books("gathering storm", limit=5, page=2, max_results=100)

    assert pool.last_path == "/api/search/book/gathering%20storm"
    assert pool.last_query == "limit=5&page=2&max_results=100"
    assert books and all(isinstance(b, isbnlab.Book) for b in books)


def test_cover_and_editions(respond):
    client, pool = respond("book-cover.json")
    cover = BooksApi(client).get_book_cover_by_isbn("9780765302304")
    assert pool.last_path == "/api/book/cover/isbn/9780765302304"
    assert cover.covers[0].startswith("https://")

    client, pool = respond("book-editions.json")
    editions = BooksApi(client).get_editions_by_isbn("9780765302304")
    assert pool.last_path == "/api/editions/isbn/9780765302304"
    assert editions.other_editions and all(isinstance(e, isbnlab.EditionRef) for e in editions.other_editions)


def test_author_lookup_reads_photos_as_objects(respond):
    client, pool = respond("author.json")

    author = AuthorsApi(client).get_author("3705408")

    assert pool.last_path == "/api/author/3705408"
    assert author.name == "Robert Jordan"
    assert isinstance(author.photos[0], isbnlab.AuthorPhoto)
    assert author.photos[0].width == 330


def test_publisher_subject_and_genre_lookups(respond):
    client, pool = respond("publishers-by-prefix.json")
    publishers = PublishersApi(client).get_publishers_by_prefix("978-0-7653")
    assert pool.last_path == "/api/publisher/prefix/978-0-7653"
    assert len(publishers) == 2 and all(isinstance(p, isbnlab.Publisher) for p in publishers)

    client, _ = respond("publisher.json")
    assert isinstance(PublishersApi(client).get_publisher("1"), isbnlab.Publisher)

    client, _ = respond("subject.json")
    assert isinstance(SubjectsApi(client).get_subject("1"), isbnlab.Subject)

    client, pool = respond("genre.json")
    genre = GenresApi(client).find_genre("FIC009000")
    assert isinstance(genre, isbnlab.Genre)
    assert genre.bisac_code


def test_isbn_tools(respond):
    client, pool = respond("isbn-details.json")

    details = IsbnApi(client).parse_isbn("9780765302304")

    assert pool.last_path == "/api/isbn/isbn-lookup/9780765302304"
    assert details.isbn10 == "0765302306"
    assert details.isbn13_formatted == "978-0-7653-0230-4"
    assert details.registration_group_name == "English language"


@pytest.mark.parametrize(
    "status, exception, detail",
    [
        (404, NotFoundException, "Book not found."),
        (403, ForbiddenException, "This endpoint needs a Standard or Pro plan."),
        (429, ApiException, "Daily request limit reached."),
    ],
)
def test_errors_carry_status_and_detail(respond, status, exception, detail):
    client, _ = respond(status=status, body={"status": status, "detail": detail}, headers={"Retry-After": "60"})

    with pytest.raises(exception) as raised:
        BooksApi(client).get_book_by_isbn("9780000000000")

    assert raised.value.status == status
    assert detail in raised.value.body
    assert raised.value.headers["Retry-After"] == "60"
