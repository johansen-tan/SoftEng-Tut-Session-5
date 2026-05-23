import pytest
from src.baggage import validate_baggage 

_FAILED_MESSAGES = {
    "hazardous": "Hazardous items detected. Can't proceed further.",
}

def test_hazardous_item_prohibited():
    assert validate_baggage(5, "carry-on", "economy", "domestic", hazardous_item=True) == _FAILED_MESSAGES["hazardous"]