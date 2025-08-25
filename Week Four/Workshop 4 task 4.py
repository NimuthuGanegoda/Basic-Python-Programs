# Name: Nimuthu Ganegoda
# Student ID: 10695889

def get_number(prompt, target_type, error_message):
    """
    Prompts the user for numeric input until a valid type is entered.
    """
    while True:
        try:
            # Ask the user for input and try to convert it
            value = target_type(input(prompt))
            return value
        except ValueError:
            # If conversion fails, show the error message
            print(error_message)

def get_ranged_number(prompt, target_type, min_val, max_val):
    """
    Prompts for numeric input and validates that it is within a range.
    """
    while True:
        try:
            value_text = input(prompt)
            value = target_type(value_text)

            # Check if the number is within the valid range
            if value < min_val:
                print(f"Too low! The minimum is {min_val}.")
            elif value > max_val:
                print(f"Too high! The maximum is {max_val}.")
            else:
                # If the number is valid, return it and exit the loop
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# --- Main Program ---

# --- Question 1: Get Age ---
print("First, let's get your age.")
age_number = get_number(
    prompt="Enter your age: ",
    target_type=int,
    error_message="That's not a whole number. Try again:"
)
print("Age entered:", age_number)
print("---------------------------------")

# --- Question 2: Get Test Score ---
print("\nNext, let's get your test score.")
score_number = get_ranged_number(
    prompt="Enter test score (0-100): ",
    target_type=int,
    min_val=0,
    max_val=100
)
print("Score entered:", score_number)
print("---------------------------------")

# --- Question 3: Get Temperature ---
print("\nNow, let's get the temperature.")
temperature_number = get_number(
    prompt="Enter temperature: ",
    target_type=float,
    error_message="That doesn't look like a number. Try again:"
)
print("Temperature entered:", temperature_number)
print("---------------------------------")

# --- Question 4: Get Weight ---
print("\nFinally, let's get your weight.")
weight_number = get_ranged_number(
    prompt="Enter weight (30-200 kg): ",
    target_type=float,
    min_val=30.0,
    max_val=200.0
)
print("Weight entered:", weight_number)
print("---------------------------------")

print("\nAll tests completed!")