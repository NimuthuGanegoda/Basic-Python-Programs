#Name: Nimuthu Ganegoda
#Student ID: 10695889

# Enhanced Lap Time Recorder with Explanatory Comments

# Create an empty list to store lap times
lap_times = []
# Start lap count at 1
lap_count = 1

# Loop to collect lap times until user enters 'x'
while True:
	# Prompt user for lap time, showing current lap number and how to end
	user_input = input(f'Enter lap time {lap_count} ("x" to end): ')
	# If user enters 'x', exit the loop
	if user_input.lower() == 'x':
		break
	try:
		# Try to convert input to float and add to lap_times list
		lap_times.append(float(user_input))
		# Increment lap count for next prompt
		lap_count += 1
	except ValueError:
		# If input is not a valid number or 'x', show error and continue
		print("Invalid input. Please enter a number or 'x' to end.")

# After collecting lap times, check if any were entered
if lap_times:
	# Print the fastest lap time (minimum value)
	print(f"Fastest Lap Time: {min(lap_times)}")
	# Print the slowest lap time (maximum value)
	print(f"Slowest Lap Time: {max(lap_times)}")
	# Print the average lap time (sum divided by count, rounded to 2 decimals)
	print(f"Average Lap Time: {sum(lap_times)/len(lap_times):.2f}")
else:
	# If no lap times entered, print message
	print("No lap times were entered.")
