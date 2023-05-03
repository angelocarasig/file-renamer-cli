import os

print("Credits: https://github.com/angelocarasig")

# Replaces a substring in all filenames in a directory
directory = input("Directory Path: ")
input_string = input("Input String: ")
replacement_string = input("Replacement String: ")

try:
    for filename in os.listdir(directory):
        if input_string in filename:
            new_filename = filename.replace(input_string, replacement_string)
            try:
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            except FileExistsError:
                print(f"File {new_filename} already exists. Skipping...")
                continue
            except Exception as e:
                print(f"Unknown Error while renaming file: {e}")
                continue
    print("Strings replaced successfully!")
except FileNotFoundError:
    print("File Location not found!")
except Exception as e:
    print(f"Unknown Error: {e}")