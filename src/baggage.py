_SUCCESS_MESSAGES = {"domestic": "Checked in successful.", 
                        "international": "Checked in successful. Passport is required"}

def validate_baggage(baggage_weight, baggage_type, passenger_class, flight_type, hazardous_item):
    if flight_type == "international":
        return _SUCCESS_MESSAGES["international"]
    else:
        return _SUCCESS_MESSAGES["domestic"]



