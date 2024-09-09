import pytest
from main import extract_field_offices


def test_extract_field_offices():
    
    item = {"title": "Wanted Person 1", "subjects": ["Subject A"], "field_offices": ["New York", "Los Angeles"]}
    field_offices = extract_field_offices(item)
    assert field_offices == "New York,Los Angeles", "Expected value differs"

    item_one_office = {"title": "Wanted Person 2", "subjects": ["Subject B"], "field_offices": ["Miami"]}
    field_offices = extract_field_offices(item_one_office)
    assert field_offices == "Miami", "Expected value differs"
