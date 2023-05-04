import os
import sys

def main(directory=None, input_string=None, replacement_string=None):
    if directory is None:
        directory = input("Directory Path: ")
    if input_string is None:
        input_string = input("Input String: ")
    if replacement_string is None:
        replacement_string = input("Replacement String: ")

    renamed_successful_count = 0

    try:
        for filename in os.listdir(directory):
            if input_string in filename:
                new_filename = filename.replace(input_string, replacement_string)
                try:
                    os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
                    renamed_successful_count += 1
                except FileExistsError:
                    print(f"File {new_filename} already exists. Skipping...")
                    continue
                except Exception as e:
                    print(f"Unknown Error while renaming file: {e}")
                    continue
        print(f"{renamed_successful_count} strings replaced successfully!")

    except FileNotFoundError:
        print("File Location not found!")

    except Exception as e:
        print(f"General Error: {e}")

if __name__ == "__main__":
    try:
        if len(sys.argv) == 1:
            main()
        elif len(sys.argv) == 2 and sys.argv[1] == "--jfif-png":
            main(None, "jfif", "png")
        else:
            print("Usage: python <script_name> [(optional) flags]")
            print("Currently available flags:")
            print("--jfif-png: Replaces all jfif files with png files")
    
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)

    
