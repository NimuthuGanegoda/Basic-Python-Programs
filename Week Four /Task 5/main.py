# Name: Nimuthu Ganegoda
# Student ID: 10695889
#
# This script runs the user interface for the conversion tool.

# Import the functions from the conversions module
import conversions

def display_menu():
    """Prints the main menu options to the console."""
    print("\n--- Metric to Imperial Conversion Tool ---")
    print("1. Centimetres to Inches")
    print("2. Metres to Feet")
    print("3. Metres to Yards")
    print("4. Kilometres to Miles")
    print("5. Exit")

def get_value():
    """
    Prompts the user for a number to convert.
    Returns the number as a float, or None if input is invalid.
    """
    try:
        value_str = input("Enter the value to convert: ")
        return float(value_str)
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
        return None

def main():
    """The main function to run the conversion tool."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting the conversion tool. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            value = get_value()
            if value is not None:
                if choice == '1':
                    result = conversions.cm_to_inches(value)
                    print(f"Result: {value} cm is {result} inches")
                elif choice == '2':
                    result = conversions.m_to_feet(value)
                    print(f"Result: {value} m is {result} feet")
                elif choice == '3':
                    result = conversions.m_to_yards(value)
                    print(f"Result: {value} m is {result} yards")
                elif choice == '4':
                    result = conversions.km_to_miles(value)
                    print(f"Result: {value} km is {result} miles")
        else:
            print("Error: Invalid choice. Please enter a number from the menu.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
