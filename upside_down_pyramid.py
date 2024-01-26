# pseudocode

# Ask user for the number of rows
rows = int(input("How many rows would you like?: "))

# Create a loop
for i in range(rows, 0, -1):
    for j in range(0, i):
        print("*", end=" ")
    # Print results