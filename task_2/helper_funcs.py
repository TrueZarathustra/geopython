def validate_latitude(string):
    try:
        return float(string) if abs(float(string)) <= 90 else None
    except:
        return None  # place for future logging


def validate_longitude(string):
    try:
        return float(string) if abs(float(string)) <= 180 else None
    except:
        return None  # place for future logging


def validate_range(string):
    try:
        return int(string) if int(string) > 0 else None
    except:
        return None  # place for future logging
        

def handle_category(string):
    category = {}
    category[string.split(',')[1]] = [int(string.split(',')[0])]
    return category
