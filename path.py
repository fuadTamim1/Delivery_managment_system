import sys
import os

# Function to get the root path of the application (D:/App)
def get_root_path():
    if getattr(sys, 'frozen', False):
        # If the app is bundled, the root path is where the executable is located
        return os.path.dirname(sys.executable)
    else:
        # If running as a script, the root path is where the main script (app.py) is located
        return os.path.dirname(os.path.abspath(__file__))

# For accessing the media folder
def get_media_folder_path():
    root_path = get_root_path()
    full_path = os.path.join(root_path, 'media')
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    return full_path
# For accessing the SQLite database file (app.db)
def get_db_path():
    root_path = get_root_path()
    return os.path.join(root_path, 'delivery_management.db')

def get_excel_export_path():# For exporting data to Excel file
    root_path = get_root_path()
    full_path = os.path.join(root_path, "exports")
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    return full_path

def init_folder():
    if not os.path.exists(get_excel_export_path()):
        os.makedirs(get_excel_export_path())

# Example of using these functions
media_folder_path = get_media_folder_path()
db_path = get_db_path()

print(f"Media folder path: {media_folder_path}")
print(f"Database path: {db_path}")