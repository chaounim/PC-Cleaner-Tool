import os
import shutil
import time

def list_files(directory):
    """
    Lists all files in the given directory.
    """
    files_and_dirs = os.listdir(directory)
    files = [f for f in files_and_dirs if os.path.isfile(os.path.join(directory, f))]
    return files

def filter_files_by_date(directory, days_old):
    """
    Lists files in the given directory that were last modified more than 'days_old' days ago.
    """
    current_time = time.time()
    cutoff = current_time - (days_old * 86400)  # 86400 seconds in a day

    old_files = []

    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        if os.path.isfile(path):
            last_modified = os.path.getmtime(path)
            if last_modified < cutoff:
                old_files.append(file)

    return old_files

def delete_files(directory, files):
    """
    Deletes files from the given directory.
    """
    for file in files:
        try:
            os.remove(os.path.join(directory, file))
            print(f"Deleted: {file}")
        except Exception as e:
            print(f"Error deleting {file}: {e}")

def move_files(directory, files, destination):
    """
    Moves files from the given directory to the destination directory.
    """
    if not os.path.exists(destination):
        os.makedirs(destination)
    for file in files:
        try:
            shutil.move(os.path.join(directory, file), os.path.join(destination, file))
            print(f"Moved: {file}")
        except Exception as e:
            print(f"Error moving {file}: {e}")

# Main logic
if __name__ == "__main__":
    choice = input("Do you want to (d)elete or (m)ove the old files? (d/m): ")
    directory_path = input("Enter the directory path to clean: ")
    days_old = int(input("Enter the age in days to filter files: "))
    old_files = filter_files_by_date(directory_path, days_old)

    if not old_files:
        print(f"No files older than {days_old} days were found.")
    elif choice.lower() == 'd':
        confirm = input("Are you sure you want to delete these files? (yes/no): ")
        if confirm.lower() == 'yes':
            delete_files(directory_path, old_files)
        else:
            print("Operation canceled.")
    elif choice.lower() == 'm':
        destination = input("Enter the destination directory for moving files: ")
        move_files(directory_path, old_files, destination)
    else:
        print("Invalid choice. Operation canceled.")
