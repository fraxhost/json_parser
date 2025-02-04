import pytest
from src.cc_json_parser.validator import JsonValidator

@pytest.fixture
def valid_json():
    return '{}'

@pytest.fixture
def invalid_json():
    return '{invalid}'

def test_valid_json(valid_json):
    validator = JsonValidator('/tests/step1/valid.json')
    assert validator.is_valid_json(valid_json) == True
    
def test_invalid_json(invalid_json):
    validator = JsonValidator('/tests/step1/invalid.json')
    assert validator.is_valid_json(invalid_json) == False