import hou
import os
import shutil

def publish_project():
    # Get the current file path
    current_file_path = hou.hipFile.path()
    
    if current_file_path == "untitled.hip":
        hou.ui.displayMessage("Please save the project before publishing.", severity=hou.severityType.Error)
        return

    # Use Desktop for publishing
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    shared_drive_base = os.path.join(desktop_path, "Published_Houdini_Projects")

    # Check if the shared drive directory exists, if not, create it
    if not os.path.exists(shared_drive_base):
        try:
            os.makedirs(shared_drive_base)
        except OSError as e:
            hou.ui.displayMessage(f"Could not create shared drive directory: {e}", severity=hou.severityType.Error)
            return

    # Get the current project directory and name
    project_dir = hou.getenv("HIP")
    project_name = hou.getenv("HIPNAME")  # Gets the filename without extension

    # Define source and destination paths
    dest_dir = os.path.join(shared_drive_base, project_name)

    # Ask user if they want to include cache files
    include_cache = hou.ui.displayMessage(
        "Include cache files (e.g., bgeo, sim data)?",
        buttons=("Yes", "No"),
        default_choice=1,
        close_choice=1
    )

    # Copy the project
    try:
        # If destination exists, remove it to avoid merge conflicts
        if os.path.exists(dest_dir):
            shutil.rmtree(dest_dir)
        
        # Copy the entire project directory
        shutil.copytree(
            project_dir,
            dest_dir,
            ignore=None if include_cache == 0 else shutil.ignore_patterns("*.bgeo", "*.bgeo.sc", "*.sim", "*.vdb", "*.ifd", "*.pic", "*.rat", "*.txt")
        )
        hou.ui.displayMessage(f"Project published successfully to:\n{dest_dir}", severity=hou.severityType.ImportantMessage)
    
    except Exception as e:
        hou.ui.displayMessage(f"Publishing failed: {str(e)}", severity=hou.severityType.Error)

# Run the function
publish_project()