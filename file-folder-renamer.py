# Differs from file-renamer.py as it appends the parent folder's name on top of the filename. Renames files a depth of 1 from the provided directory.
# This case is specific in the sense that certain files would be inside folders that are named independently from the folder name, so this script would be useful in order to provide more detail for each file.

import os
import sys
import traceback
from tabulate import tabulate

class FileRenameStruct:
    def __init__(self, original_string, replacement_string, directory, skip_file=False) -> None:
        self.original_string = original_string
        self.replacement_string = replacement_string
        self.directory = directory
        self.skip_file = skip_file
    
    def __str__(self) -> str:
        return f"\n\tOriginal String: {self.original_string}\n\tReplacement String: {self.replacement_string}\n\tDirectory: {self.directory}\n\tSkip File: {self.skip_file}"
    
    def get_file_location(self) -> str:
        return os.path.join(self.directory, self.original_string)

def seperator() -> None:
    print("-" * 50)
    print()
    return

# Prints from a filerename struct array
def print_filerename_struct(filerename_struct_list: list[FileRenameStruct]) -> None:
    properties = [
        ["Original String", "Replacement String", "Directory", "Skip File"],
    ]

    for filerename_struct in filerename_struct_list:
        properties.append([filerename_struct.original_string, filerename_struct.replacement_string, filerename_struct.directory, filerename_struct.skip_file])
    
    print(tabulate(properties, headers="firstrow", tablefmt="grid"))
    return

def print_directory_original_contents(directory: str, print_only_directories: bool = False) -> None:
    file_data = []
    folder_data = []

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        if os.path.isdir(item_path):
            folder_data.append([item, "<DIR>"])
        else:
            filename, file_extension = os.path.splitext(item)
            file_data.append([filename, file_extension, os.path.getsize(item_path)])

    table_data = folder_data + file_data
    headers = ["Name", "Extension", "Size"]

    if (print_only_directories):
        print(tabulate(folder_data, headers=headers, tablefmt="grid"))
    else:
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
    
    # Newline to finish
    print()


def print_directory_renamed_contents(rename_array: list[FileRenameStruct]) -> None:

    headers = ["Original Name", "Replaced Name", "Extension", "Size", "Directory", "Status"]
    rename_data = []

    for rename_struct in rename_array:
        file_location = os.path.join(rename_struct.directory, rename_struct.original_string)
        file_size = os.path.getsize(file_location)
        _, file_extension = os.path.splitext( file_location )
        rename_data.append( [rename_struct.original_string, rename_struct.original_string if rename_struct.skip_file else rename_struct.replacement_string, file_extension, file_size, file_location, "ALREADY FORMATTED" if rename_struct.skip_file else "RENAMING"] )

    print(tabulate(rename_data, headers=headers, tablefmt="grid"))

def rename_files(rename_array: list[FileRenameStruct]) -> tuple[int, int]:

    results = [0, 0]

    try:
        for rename_struct in rename_array:
            if not rename_struct.skip_file:
                os.rename(rename_struct.get_file_location(), os.path.join(rename_struct.directory, rename_struct.replacement_string))
                results[0] += 1
            else:
                results[1] += 1

    except FileExistsError:
        print("File already exists. Skipping...")
        results[1] += 1

    except Exception as e:
        print(f"Unknown error...")
        print(traceback.print_exc())
        results[1] += 1

    return tuple(results)

# Performs the function to all files for a depth of 1 currently
def main(directory: str = None) -> None:
    print()

    # Error checking
    if directory is None:
        directory = input("Directory Path: ")
    
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory {directory} not found")
    
    seperator()

    # Get the list of folders (depth of 1) from the current directory
    folder_list = [folder for folder in os.listdir(directory) if os.path.isdir(os.path.join(directory, folder))]
    print(f"There are {len(folder_list)} folders in {directory}.")
    print_directory_original_contents(directory)

    # Remove folders that start with '.'
        # Counts total number of folders that start with '.'
    print(f"There are {sum(1 for string in folder_list if string.startswith('.'))} folders that are hidden in {directory} (starts with '.') and will be ignored.\n")
    folder_list = [folder for folder in folder_list if not folder.startswith('.')]

    seperator()

    # [0] == number of files renamed
    # [1] == number of files ignored
    global_results = [0, 0]

    # Iterate through each sub-folder
    for folder in folder_list:
        rename_array: list[FileRenameStruct] = []
        subfolder_directory = os.path.join(directory, folder)
        
        print(f"Contents of {subfolder_directory}:")
        print_directory_original_contents(subfolder_directory)

        subfolder_files = [file for file in os.listdir(subfolder_directory) if os.path.isfile(os.path.join(subfolder_directory, file))]

        # Process each file in the subfolder
        for subfolder_file in subfolder_files:

            filename, file_extension = os.path.splitext(subfolder_file)

            # Check if the file is already formatted
            if os.path.basename(os.path.normpath(subfolder_directory)) not in subfolder_file:
                rename_array.append(FileRenameStruct(subfolder_file, f"[{filename}] {folder + file_extension}", subfolder_directory))
            else:
                print(f"File {subfolder_file} is already formatted. Skipping...")
                rename_array.append(FileRenameStruct(subfolder_file, f"[{subfolder_file}] {folder}", subfolder_directory, skip_file=True))


        seperator()

        print(f"Formatting the following files in {subfolder_directory}:")
        print_directory_renamed_contents(rename_array)

        input("\nPress enter to continue...\n\n")

        # Rename files
        results: tuple[int, int] = rename_files(rename_array)
        
        print(f"Renamed {results[0]} files with {results[1]} files ignored in {subfolder_directory}.")
        global_results[0] += results[0]
        global_results[1] += results[1]

        seperator()
    
    print(f"\nRenamed in total: {global_results[0]} files with {global_results[1]} files ignored.")


if __name__=="__main__":
    try:
        if len(sys.argv) == 1:
            main()

        elif len(sys.argv) == 2 and sys.argv[1]:
            main(sys.argv[1])
    
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)    
