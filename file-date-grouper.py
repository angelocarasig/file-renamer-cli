import os
import shutil
from datetime import datetime

def organize_files(directory):
    items = os.listdir(directory)
    folder_counts = {}

    for item in items:
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            ctime = os.path.getctime(item_path)
            date = datetime.fromtimestamp(ctime)
            year = date.year
            month_name = date.strftime("%B")
            folder_name = f"{month_name} {year}"
            folder_dir = os.path.join(directory, folder_name)

            if not os.path.exists(folder_dir):
                os.mkdir(folder_dir)
                print(f"Created folder: {folder_name}")
            
            if folder_counts[folder_name] is None:
                folder_counts[folder_name] = 0

            shutil.move(item_path, folder_dir)
            folder_counts[folder_name] = folder_counts.get(folder_name, 0) + 1

    for folder, count in folder_counts.items():
        print(f"{count} items have been moved to {folder}!")
    print(f"A total of {sum(folder_counts.values())} items have been moved!")

def main():
    try:
        directory = input("Directory Path: ")
        organize_files(directory)
    except FileNotFoundError:
        print(f"Directory {directory} not found")
    except Exception as e:
        print(f"Unknown error: {e}")

if __name__ == "__main__":
    main()
