# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Draw the Pattern using a while loop
while row < size:
    # Use a for loop to print asterisks in a row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1  # Increment the row counter
