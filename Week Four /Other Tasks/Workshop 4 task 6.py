# Name: Nimuthu Ganegoda
# Student ID: 10695889

# --- Helper Functions for Getting Validated Input ---

def get_valid_float(min_val=None, max_val=None):
    """
    Gets a float from the user, handling errors and optional range checks.
    This function does not print the initial prompt.
    """
    while True:
        try:
            # Use a simple ">" to show the user where to type
            value_str = input("> ")
            value = float(value_str)

            if min_val is not None and value < min_val:
                print("Error: Value is too low. The minimum is", min_val)
                continue 
            
            if max_val is not None and value > max_val:
                print("Error: Value is too high. The maximum is", max_val)
                continue
                
            return value 
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

def get_valid_int(min_val=None, max_val=None):
    """
    Gets an integer from the user, handling errors and optional range checks.
    This function does not print the initial prompt.
    """
    while True:
        try:
            # Use a simple ">" to show the user where to type
            value_str = input("> ")
            value = int(value_str)

            if min_val is not None and value < min_val:
                print("Error: Value is too low. The minimum is", min_val)
                continue

            if max_val is not None and value > max_val:
                print("Error: Value is too high. The maximum is", max_val)
                continue
                
            return value
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.")


# --- Main Script ---
# This part of the script calls the helper functions defined above.

# --- Question 1: Get Age ---
print("First, let's get your age.")
print("Enter your age:") # Print the question first
age_number = get_valid_int(min_val=0) # Then get the valid input
print("Age entered:", age_number)
print("---------------------------------")


# --- Question 2: Get Test Score ---
print("\nNext, let's get your test score.")
print("Enter test score (0-100):") # Print the question first
score_number = get_valid_int(min_val=0, max_val=100) # Then get the valid input
print("Score entered:", score_number)
print("---------------------------------")


# --- Question 3: Get Temperature ---
print("\nNow, let's get the temperature.")
print("Enter temperature:") # Print the question first
temperature_number = get_valid_float() # Then get the valid input
print("Temperature entered:", temperature_number)
print("---------------------------------")


# --- Question 4: Get Weight ---
print("\nFinally, let's get your weight.")
print("Enter weight (30-200 kg):") # Print the question first
weight_number = get_valid_float(min_val=30.0, max_val=200.0) # Then get the valid input
print("Weight entered:", weight_number)
print("---------------------------------")


print("\nAll tests completed!")