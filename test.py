import sys
import os
import importlib
import time


def main():
    # Ensure the user provides the correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: python test.py <day_number> <part>")
        sys.exit(1)

    # Parse the day number and part number from command-line arguments
    day_number = sys.argv[1]
    part = sys.argv[2]

    # Validate that the folder exists
    day_folder = f"day_{day_number}"
    if not os.path.exists(day_folder):
        print(f"Error: Folder '{day_folder}' does not exist.")
        sys.exit(1)

    # Read the input string from 'input.txt' located in the day's folder
    input_path = os.path.join(day_folder, "input.txt")
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' does not exist.")
        sys.exit(1)

    with open(input_path, "r") as file:
        input_string = file.read()

    # Dynamically import the solution module
    solution_file = f"solution_part_{part}"
    module_path = f"{day_folder}.{solution_file}"
    try:
        solution_module = importlib.import_module(module_path)
    except ModuleNotFoundError:
        print(f"Error: Could not find module '{module_path}'.")
        sys.exit(1)

    # Call the solution function
    total_time = 0
    num_iterations = 100
    for _ in range(num_iterations):
        start_time = time.time()
        result = solution_module.solution(input_string)
        end_time = time.time()
        total_time += end_time - start_time

    average_time = total_time / num_iterations
    print("Result:", result)
    print("Average time:", average_time)


if __name__ == "__main__":
    main()

