import pytest
from src.cc_json_parser.validator import JsonValidator

@pytest.mark.parametrize(
        'file_path, expected_result',
        [
            ('.\\tests\\step1\\valid.json', True),
            ('.\\tests\\step2\\valid.json', True),
            ('.\\tests\\step2\\valid2.json', True),
            ('.\\tests\\step1\\invalid.json', False),
            ('.\\tests\\step2\\invalid.json', False),
            ('.\\tests\\step2\\invalid2.json', False)
        ]
)
def test_json(file_path, expected_result):
    validator = JsonValidator(file_path)
    assert validator.validate() == expected_result