input_filename = "input.txt"
output_filename = "output.txt"

try:
    # 1. Read data from the input file
    with open(input_filename, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    # 2. Count total lines
    line_count = len(lines)
    print(f"Total number of lines: {line_count}")

    # 3. Extract the first two lines
    first_two_lines = lines[:2]

    # 4. Write the extracted data into a new file
    with open(output_filename, "w", encoding="utf-8") as outfile:
        outfile.writelines(first_two_lines)

    print(f"Successfully wrote the first {len(first_two_lines)} line(s) to '{output_filename}'.")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' was not found.")
