import pytest
from src.baggage import validate_baggage 

def test_flight_type():
    assert validate_baggage(5, "carry-on", "economy", "domestic", hazardous_item=False) == _SUCCESS_MESSAGES["domestic"]
    assert validate_baggage(25, "checked", "economy", "domestic", hazardous_item=False) == _SUCCESS_MESSAGES["domestic"]
    assert validate_baggage(7, "carry-on", "economy", "international", hazardous_item=False) == _SUCCESS_MESSAGES["international"]
    assert validate_baggage(30, "checked", "economy", "international", hazardous_item=False) == _SUCCESS_MESSAGES["international"]