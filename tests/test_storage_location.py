import pytest

from warehouse_analytics.storage_location import parse_location_code


def test_parse_location_code():
    location = parse_location_code("A-03-12-2")

    assert location.aisle == "A"
    assert location.rack == "03"
    assert location.slot == "12"
    assert location.level == "2"


def test_parse_highest_location_code():
    location = parse_location_code("Z-99-99-6")

    assert location.aisle == "Z"
    assert location.rack == "99"
    assert location.slot == "99"
    assert location.level == "6"


def test_parse_lowest_location_code():
    location = parse_location_code("A-01-01-1")

    assert location.aisle == "A"
    assert location.rack == "01"
    assert location.slot == "01"
    assert location.level == "1"


def test_parse_location_code_rejects_empty_string():
    with pytest.raises(ValueError):
        parse_location_code("")


@pytest.mark.parametrize(
    "code, part",
    [
        ("a-01-01-1", "aisle"),
        ("1-01-01-1", "aisle"),
        ("A-1-01-1", "rack"),
        ("A-101-01-1", "rack"),
        ("A-00-01-1", "rack"),
        ("A-01-01-0", "level"),
        ("A-01-01-7", "level"),
        (" A-01-01-1", "aisle"),
        ("A-01-01-1 ", "level"),
        ("A- 01-01-1", "rack"),
        ("A-01-00-1", "slot"),
        ("Ä-01-01-1", "aisle"),
    ],
)
def test_parse_location_code_rejects_invalid_code(code, part):
    with pytest.raises(ValueError, match=part):
        parse_location_code(code)
