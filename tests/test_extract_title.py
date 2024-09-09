import pytest
from main import extract_title


def test_extract_title():
    
    item = {"title": "Wanted Person 1", "subjects": ["Subject A"], "field_offices": ["New York"]}
    title = extract_title(item)
    assert title == "Wanted Person 1", "Expected Value Differs"
