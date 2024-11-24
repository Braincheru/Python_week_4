def read_and_write_file(input_filename, output_filename):
    try:
       with open(input_filename, 'r') as file:
            content = file.read()
        modified_content = content.upper()

        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"File '{output_filename}' has been created with the modified content.")
        except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError as e:
        print(f"Error: An I/O error occurred - {e}")


input_filename = ""
output_filename = ""

read_and_write_file(input_filename, output_filename)
