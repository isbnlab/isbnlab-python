# coding: utf-8

"""
Reads the headers the API adds when a response leaves out fields that need a
higher plan. A book lookup on a Free or Standard plan, for example, returns
other_editions, previous_edition and next_edition as None and names them here.

Pass the response from a ..._with_http_info() call, or its headers::

    response = books.get_book_by_isbn_with_http_info("9780765302304")

    isbnlab.restricted_fields(response)  # ['otherEditions', 'previousEdition', 'nextEdition']
    isbnlab.upgrade_url(response)        # 'https://www.isbnlab.com/pricing'
"""

from typing import Any, List, Mapping, Optional, Union

RESTRICTED_FIELDS_HEADER = "X-Plan-Restricted-Fields"
UPGRADE_HEADER = "X-Plan-Upgrade"


def _header(response_or_headers: Union[Any, Mapping[str, str], None], name: str) -> Optional[str]:
    headers = getattr(response_or_headers, "headers", response_or_headers)
    if not headers:
        return None
    for key, value in headers.items():
        if key.lower() == name.lower():
            value = (value or "").strip()
            return value or None
    return None


def restricted_fields(response_or_headers: Union[Any, Mapping[str, str], None]) -> List[str]:
    """The fields your plan left empty in this response, by their API names
    (otherEditions), or an empty list when nothing was left out."""
    value = _header(response_or_headers, RESTRICTED_FIELDS_HEADER)
    if value is None:
        return []
    return [field.strip() for field in value.split(",") if field.strip()]


def upgrade_url(response_or_headers: Union[Any, Mapping[str, str], None]) -> Optional[str]:
    """The page that lists the plans which include the left-out fields, or None
    when nothing was left out."""
    return _header(response_or_headers, UPGRADE_HEADER)
