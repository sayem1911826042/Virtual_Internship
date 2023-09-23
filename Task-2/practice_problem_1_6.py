# Accept a comma-separated sequence of words as input
input_sequence = input("Enter a comma-separated sequence of words: ")

# Split the input into words using the comma as the separator
words = input_sequence.split(',')

# Convert the list of words into a set to remove duplicates
unique_words = set(words)

# Convert the set back to a sorted list
sorted_unique_words = sorted(unique_words)

# Join the sorted words into a single string
result = ', '.join(sorted_unique_words)

# Print the result
print("Unique words in sorted form:", result)
