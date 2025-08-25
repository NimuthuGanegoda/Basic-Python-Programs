# Name: Nimuthu Ganegoda
# Student ID: 10695889
#
# This module provides functions for metric to imperial conversions.

# --- Conversion Factors ---
CM_TO_INCHES_FACTOR = 0.393700787
M_TO_FEET_FACTOR = 3.2808399
M_TO_YARDS_FACTOR = 1.0936133
KM_TO_MILES_FACTOR = 0.621371192

def cm_to_inches(cm):
    """Converts centimetres to inches and rounds to 2 decimal places."""
    return round(cm * CM_TO_INCHES_FACTOR, 2)

def m_to_feet(m):
    """Converts metres to feet and rounds to 2 decimal places."""
    return round(m * M_TO_FEET_FACTOR, 2)

def m_to_yards(m):
    """Converts metres to yards and rounds to 2 decimal places."""
    return round(m * M_TO_YARDS_FACTOR, 2)

def km_to_miles(km):
    """Converts kilometres to miles and rounds to 2 decimal places."""
    return round(km * KM_TO_MILES_FACTOR, 2)
