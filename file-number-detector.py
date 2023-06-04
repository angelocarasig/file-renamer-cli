# Detects missing numbers from a collection of files in a directory
# TODO: Maybe add in substring support for the seperator

import os
import sys

def main(directory=None): 
    # Error checking
    if directory is None:
        directory = input("Directory Path: ")
    
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory {directory} not found")
    
    word_seperator = input("Enter Seperator: ")
    
    file_list_numbers = [int(file.split(word_seperator)[1]) for file in os.listdir(directory)]
    missing_values = [value for value in range(1, max(file_list_numbers) + 1) if value not in file_list_numbers]
    print("Missing values:", missing_values)

if __name__ == "__main__":
    try:
        if len(sys.argv) == 1:
            main()
        elif len(sys.argv) == 2:
            main(sys.argv[1])
    
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)

    
