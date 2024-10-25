import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

# Define the paths
source_folder = "/Users/connermurphy/Desktop/renamefile"
target_folder = "/Users/connermurphy/Desktop/0001testrename"
target_filename = "the_test_worked 100%"

# Create target folder if it doesn't exist
os.makedirs(target_folder, exist_ok=True)

# Define the event handler class
class FileRenameHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Check if the event is a file (not a directory)
        if not event.is_directory:
            # Get the original file path
            original_file = event.src_path
            # Define the new file path
            target_path = os.path.join(target_folder, target_filename)

            # Move and rename the file
            shutil.move(original_file, target_path)
            print(f"File renamed and moved to {target_path}")

# Set up the observer
observer = Observer()
event_handler = FileRenameHandler()
observer.schedule(event_handler, path=source_folder, recursive=False)

# Start observing
observer.start()
try:
    while True:
        time.sleep(1)  # Keep the script running
except KeyboardInterrupt:
    observer.stop()

observer.join()