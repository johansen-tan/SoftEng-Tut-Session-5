import pytest
from src.baggage import validate_baggage 

_FAILED_MESSAGES = {"overweight": "Weight surpasses limit.", 
                     "invalid": "Data is invalid."}

def test_carry_on():
    assert validate_baggage(-1, "carry-on", "economy", "domestic", hazardous_item=False) == _FAILED_MESSAGES["invalid"]
    assert validate_baggage(-1, "carry-on", "business", "domestic", hazardous_item=False) == _FAILED_MESSAGES["invalid"]
    assert validate_baggage(7, "carry-on", "economy", "domestic", hazardous_item=False) == _SUCCESS_MESSAGES["domestic"]
    assert validate_baggage(7, "carry-on", "business", "domestic", hazardous_item=False) == _SUCCESS_MESSAGES["domestic"]
    assert validate_baggage(8, "carry-on", "economy", "domestic", hazardous_item=False) == _FAILED_MESSAGES["overweight"]
    assert validate_baggage(8, "carry-on", "business", "domestic", hazardous_item=False) == _FAILED_MESSAGES["overweight"]
from src.baggage import validate_baggage

_SUCCESS_MESSAGES = {"domestic": "Checked in successful.", 
                        "international": "Checked in successful. Passport is required"}



def test_flight_type():
    assert validate_baggage(5, "carry-on", "economy", "domestic", hazardous_item=False) == _SUCCESS_MESSAGES["domestic"]
    assert validate_baggage(25, "checked", "economy", "domestic", hazardous_item=False) == _SUCCESS_MESSAGES["domestic"]
    assert validate_baggage(7, "carry-on", "economy", "international", hazardous_item=False) == _SUCCESS_MESSAGES["international"]
    assert validate_baggage(30, "checked", "economy", "international", hazardous_item=False) == _SUCCESS_MESSAGES["international"]
