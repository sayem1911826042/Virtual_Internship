# Define the sentence
rima_sentence = "Your daughter is very pretty"

# Create an empty string to store the result
unique_chars = ""

# Iterate through each character in the sentence
for char in rima_sentence:
    # Check if the character is not already in the unique_chars string
    if char not in unique_chars:
        unique_chars += char

# Print the sentence with duplicate characters removed
print("Rima's sentence without duplicate characters:", unique_chars)
