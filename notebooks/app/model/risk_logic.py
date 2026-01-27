def get_risk_level(crime_count):
    if crime_count > 20:
        return "High"
    elif crime_count > 10:
        return "Medium"
    else:
        return "Low"
