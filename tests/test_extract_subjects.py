import pytest
from main import extract_subjects


def test_extract_subjects():
    
    item = {"title": "Wanted Person 1", "subjects": ["Subject A", "Subject B"], "field_offices": ["New York"]}
    subjects = extract_subjects(item)
    assert subjects == "Subject A,Subject B", f"Expected 'Subject A,Subject B', got {subjects}"

    item_no_subjects = {"title": "Wanted Person 2", "subjects": [], "field_offices": ["Miami"]}
    subjects = extract_subjects(item_no_subjects)
    assert subjects == "", "Expected an empty string when there are no subjects"
