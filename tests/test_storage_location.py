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
