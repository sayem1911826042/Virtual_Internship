def count_upper_lower(string):
    # Initialize variables to count uppercase and lowercase letters
    upper_count = 0
    lower_count = 0

    # Iterate through each character in the input string
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    # Return the counts as a tuple
    return upper_count, lower_count

# Sample input string
input_string = "Bangladesh has played 396 ODI matches resulting in 142 victories"

# Call the function with the input string
upper, lower = count_upper_lower(input_string)

# Print the results
print("No. of Upper case characters:", upper)
print("No. of Lower case Characters:", lower)
