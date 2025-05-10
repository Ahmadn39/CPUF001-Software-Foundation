import sys
import os
import statistics


def read_file(file_path):
    # Read the file and extract numeric values
    try:
        with open(file_path, "r") as file:
            values = [float(line.strip()) for line in file if line.strip()]
        if len(values) < 3:
            raise ValueError("Minimum contain 3 numeric values.")
        return values
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

# Performs two basic calculations: mean and standard deviation
def calculations(values):
    # Calculate standard deviation
    std_dev = statistics.stdev(values)
    mean = sum(values) / len(values)
    return mean, std_dev


def write_output_file(output_path, total, average):
    # Writes output file.
    try:
        with open(output_path, "w") as file:
            file.write(f"Standard deviation: {total}\n")
            file.write(f"Average: {average}\n")
        print(f"Calculation result written to {output_path}")
    except IOError:
        print(f"Error: To write to file '{output_path}'.")
        sys.exit(1)


def main():
    # Handle command-line arguments and execute processing
    if len(sys.argv) != 2:
        print("Utilize python data_processing.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "output.txt"

    values = read_file(input_file)
    total, average = calculations(values)
    write_output_file(output_file, total, average)


if __name__ == "__main__":
    main()