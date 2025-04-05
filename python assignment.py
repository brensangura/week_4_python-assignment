def modify_and_write_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"File successfully modified and written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    except IOError:
        print(f"Error: Could not read {input_filename} or write to {output_filename}")

# Example usage
modify_and_write_file('original.txt', 'modified.txt')


def read_file_with_handling():
    while True:
        filename = input("Please enter the filename to read: ")
        
        try:
            with open(filename, 'r') as file:
                content = file.read()
                print("\nFile content:")
                print(content)
                break
                
        except FileNotFoundError:
            print(f"Error: The file '{filename}' doesn't exist. Please try again.")
        except PermissionError:
            print(f"Error: You don't have permission to read '{filename}'. Please try another file.")
        except UnicodeDecodeError:
            print(f"Error: Couldn't decode the file '{filename}'. It might be a binary file.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}. Please try again.")

# Example usage
read_file_with_handling()