import pytest
from main import print_fbi_data


def test_print_fbi_data(capsys):
    sample_data = {
        "items": [
            {"title": "Wanted Person 1", "subjects": ["Subject A", "Subject B"], "field_offices": ["New York", "Los Angeles"]}
        ]
    }

    print_fbi_data(sample_data)

    captured = capsys.readouterr()
    expected_output = "Wanted Person 1þSubject A,Subject BþNew York,Los Angeles\n" 
    assert captured.out == expected_output, "Expected output differs"
