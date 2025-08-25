#Name: Nimuthu Ganegoda
#Student ID: 10695889

# Prompt the user to enter their taxable income
income = float(input("Enter your taxable income: "))

# Calculate tax based on Australian Tax Office table
if income <= 18200:
    tax = 0
elif income <= 37000:
    tax = (income - 18200) * 0.19
elif income <= 90000:
    tax = 3572 + (income - 37000) * 0.325
elif income <= 180000:
    tax = 20797 + (income - 90000) * 0.37
else:
    tax = 54097 + (income - 180000) * 0.45

# Display the calculated tax
print(f"The amount of tax you must is: ${tax:.2f}")