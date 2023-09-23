# Define the list
numbers = [10, 0, 55, 88, 100, -56, 80]

# Initialize a variable to store the largest number
largest = numbers[0]  # Start with the first number in the list

# Iterate through the list to find the largest number
for number in numbers:
    if number > largest:
        largest = number

# Print the largest number
print("The largest number in the list is:", largest)
