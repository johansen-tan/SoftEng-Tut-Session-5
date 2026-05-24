_SUCCESS_MESSAGES = {"domestic": "Checked in successful.", 
                        "international": "Checked in successful. Passport is required"}

_FAILED_MESSAGES = {
    "hazardous": "Hazardous items detected. Can't proceed further.",
    "overweight": "Weight surpasses limit.", 
    "invalid": "Data is invalid."
}

def isHazardous(hazardous_item):
    if hazardous_item:
        return True
    return False
  
def isDomestic(type):
    if (type == "international"):
        return False
    else:
        return True

def isCarryOn(type):
    if (type == "carry-on"):
        return True
    else:
        return False

def isOverweight(weight, max_weight):
    if weight > max_weight:
        return True
    else:
        return False
    
def isChecked(type):
    if (type == "checked"):
        return True
    else:
        return False

def isInvalid(weight):
    if weight < 0:
        return True
    else:
        return False
    
def validate_baggage(baggage_weight, baggage_type, passenger_class, flight_type, hazardous_item):
    """
    Business Rules:
    - Carry-on baggage max 7 kg
    - Checked baggage max 30 kg
    - Business class gets extra 10 kg allowance for checked baggage
    - Hazardous items are prohibited
    """
    max_weight = 0
    if isCarryOn(baggage_type):
        max_weight = 7
    elif isChecked(baggage_type):
        max_weight = 30
        if passenger_class == "business":
            max_weight += 10


    
    if isOverweight(baggage_weight, max_weight):
        return _FAILED_MESSAGES["overweight"]
    elif isInvalid(baggage_weight):
        return _FAILED_MESSAGES["invalid"]
    
    if isHazardous(hazardous_item):
        return _FAILED_MESSAGES["hazardous"]
    
    if isDomestic(flight_type):
        return _SUCCESS_MESSAGES["domestic"]
    else:
        return _SUCCESS_MESSAGES["international"]

