# Name: Nimuthu Ganegoda
# Student ID: 10695889

def get_user_age():
    """Keeps asking for age until a valid integer is entered."""
    while True:
        try:
            age_input = input("Enter your age: ")
            return int(age_input)
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_current_temperature():
    """Keeps asking for temperature until a valid number is entered."""
    while True:
        try:
            temp_input = input("Enter current temperature in Celsius: ")
            return float(temp_input)
        except ValueError:
            print("Invalid input. Please enter a number.")

# Get the age and temperature by calling the functions
age = get_user_age()
temperature = get_current_temperature()

# Print the final results
print("Your age is:", age)
print("Temperature is:", temperature, "C")