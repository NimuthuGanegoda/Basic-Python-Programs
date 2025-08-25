# Name: Nimuthu Ganegoda
# Student ID: 10695889

# Create an empty list to store lap times
lap_times = []

# Ask the user how many laps they want to record
num_laps = int(input("How many laps will you record?: "))

# Loop for the number of laps specified by the user
for i in range(num_laps):
    # Prompt the user to enter the lap time for each lap
    lap_time = float(input(f"Enter lap time {i+1} of {num_laps}: "))
    # Add the entered lap time to the list
    lap_times.append(lap_time)

# Find the fastest lap time (minimum value)
fastest = min(lap_times)
# Find the slowest lap time (maximum value)
slowest = max(lap_times)
# Calculate the average lap time, rounded to 2 decimal places
average = round(sum(lap_times) / len(lap_times), 2)

# Print the results
print("Fastest lap time:", fastest)
print("Slowest lap time:", slowest)
print("Average lap time:" ,average)
