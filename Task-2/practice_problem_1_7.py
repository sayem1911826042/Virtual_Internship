# Sample string
sample_string = "thequickbrownfoxjumpsoverthelazydog"

# Initialize a dictionary to store character counts
char_count = {}

# Iterate through the string
for char in sample_string:
    # If the character is already in the dictionary, increment its count
    if char in char_count:
        char_count[char] += 1
    # If the character is not in the dictionary, add it with a count of 1
    else:
        char_count[char] = 1

# Iterate through the dictionary and print character counts
for char, count in char_count.items():
    if count > 1:
        print(f"{char} {count}")
