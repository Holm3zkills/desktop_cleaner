import os
import shutil
from tkinter import Tk, filedialog

def get_desktop_path():
    """Get the path to the user's desktop."""
    return os.path.join(os.path.expanduser('~'), 'Desktop')

def organize_files(src_folder, dest_folder):
    """Organize files from source to destination folder."""
    for file_name in os.listdir(src_folder):
        file_path = os.path.join(src_folder, file_name)

        # Check if it's a file (not a folder)
        if os.path.isfile(file_path):
            # Determine the file type based on the extension
            file_type = file_name.split('.')[-1].lower()

            # Define destination folder for each file type
            file_type_folders = {
                'txt': 'TextFiles',
                'jpg': 'Images',
                'pdf': 'PDFs'
                # Add more file types and corresponding folders as needed
            }

            # Get the destination folder based on file type
            dest_type_folder = file_type_folders.get(file_type, 'Other')

            # Create the destination folder if it doesn't exist
            dest_path = os.path.join(dest_folder, dest_type_folder)
            os.makedirs(dest_path, exist_ok=True)

            # Move the file to the destination folder
            shutil.move(file_path, os.path.join(dest_path, file_name))

def select_folder():
    """Open a folder selection dialog and return the selected path."""
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select Folder")
    return folder_path

def main():
    desktop_path = get_desktop_path()
    print("Desktop Cleaner App")

    # Ask the user to select a destination folder
    dest_folder = select_folder()

    # Organize files on the desktop
    organize_files(desktop_path, dest_folder)

    print("Cleaning complete.")

if __name__ == "__main__":
    main()