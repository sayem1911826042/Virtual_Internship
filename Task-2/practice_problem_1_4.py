# Define the sample list of strings
string_list = ['abc', 'xyz', 'aba', '1221']

# Initialize a variable to count matching strings
count = 0

# Iterate through the list of strings
for s in string_list:
    # Check if the string has a length of 2 or more and the first and last characters are the same
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1

# Print the count of matching strings
print("Number of strings meeting the criteria:", count)
