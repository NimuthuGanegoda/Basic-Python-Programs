#Name: Nimuthu Ganegoda
#Student ID: 10695889

# Prompt user to type something
user_input = input("Type something: ")

# Check if the string is all upper case
if user_input.isupper():
    print("Your input is all upper case.")

# Check if the string is all lower case
if user_input.islower():
    print("Your input is all lower case.")

# Check if the string contains only letters
if user_input.isalpha():
    print("Your input contains only letters.")

# Check if the string contains only numbers
if user_input.isdigit():
    print("Your input contains only numbers.")

# Check if the string contains only spaces
if user_input.isspace():
    print("Your input contains only spaces.")

# Check if the string starts with "sh"
if user_input.startswith("sh"):
    print('Your input starts with "sh".')

# Check if the string ends with "p"
if user_input.endswith("p"):
    print('Your input ends with "p".')

# Check if the string contains at least two "e"s
if user_input.count('e') >= 2:
    print('Your input contains at least two "e"s.')

# Print the length of the string
print(f"The length of your input is {len(user_input)}") 