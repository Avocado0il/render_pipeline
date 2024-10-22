import os
import time

# Define the folder to monitor (your Mac Desktop's "renamefile" folder)
folder_to_watch = os.path.expanduser("~/Desktop/renamefile")

# Define the new name for the file
new_file_name = "123renamedfile"  # You can adjust the extension handling below

def rename_file(file_path, new_name):
    # Get the directory and the original file extension
    directory, original_file = os.path.split(file_path)
    _, file_extension = os.path.splitext(original_file)

    # Create the full new file path with the same extension
    new_file_path = os.path.join(directory, f"{new_name}{file_extension}")

    # If a file with the new name already exists, delete it
    if os.path.exists(new_file_path):
        os.remove(new_file_path)

    # Rename the file
    os.rename(file_path, new_file_path)
    print(f"Renamed: {file_path} -> {new_file_path}")

def monitor_folder():
    print(f"Monitoring folder: {folder_to_watch}")
    
    # Initial list of files
    before = dict((f, None) for f in os.listdir(folder_to_watch))
    
    while True:
        time.sleep(2)  # Check every 2 seconds
        # Get the current list of files
        after = dict((f, None) for f in os.listdir(folder_to_watch))
        
        # Check for new files
        added = [f for f in after if not f in before]
        
        if added:
            for file in added:
                file_path = os.path.join(folder_to_watch, file)
                print(f"New file detected: {file}")
                rename_file(file_path, new_file_name)
        
        before = after  # Update the list of files

if __name__ == "__main__":
    monitor_folder()
