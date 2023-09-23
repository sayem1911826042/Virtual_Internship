# Define a list to store the extracted text from files
text_list = []

# List of file names
file_names = ['words1.txt', 'words2.txt']

# Iterate through each file
for file_name in file_names:
    try:
        # Open and read the file
        with open(file_name, 'r') as file:
            text = file.read()
            text_list.append(text)
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Skipping...")

# Print the list of extracted text
for i, text in enumerate(text_list, start=1):
    print(f"Text from file {i}:\n{text}\n")
