# Name: Nimuthu Ganegoda
# Student ID: 10695889

import random  # Import the random module to generate random numbers

count = 1  # Initialize count to keep track of how many numbers have been generated
while True:
	# Generate a random integer between 0 and 10 (inclusive)
	num = random.randint(0, 10)
	# Print the current count and the generated number
	print("Number", count, "was", num)
	# If the number is 7, print a special message
	if num == 7:
		print("Lucky 7!")
	# If the number is 0, exit the loop
	if num == 0:
		break
	# Increment the count for the next iteration
	count += 1
