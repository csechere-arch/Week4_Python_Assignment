# Simple File Read & Write Program with Error Handling

# Ask the user for a file name
filename = input("Enter the name of the file to read: ")

try:
    # Try to open and read the file
    with open(filename, "r") as file:
        content = file.read()
    
    # Process the content
    # Example: make all letters uppercase
    modified_content = content.upper()
    
    # Save the modified content to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)
    
    print(f"Done! The modified file is saved as '{new_filename}'.")

# Handle errors if the file doesn't exist or cannot be read
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except PermissionError:
    print(f"Error: You do not have permission to read '{filename}'.")
except Exception as e:
    print(f"An error occurred: {e}")