import hou
import re
import os

# Get the current file path
current_file_path = hou.hipFile.path()

# If the file is unsaved, prompt to save first
if current_file_path == "untitled.hip":
    hou.ui.displayMessage("Please save the file before versioning up.", severity=hou.severityType.Error)
else:
    # Extract the filename from the path
    file_name = os.path.basename(current_file_path)
    file_dir = os.path.dirname(current_file_path)
    
    # Recommended pattern: filename_version.extension (e.g., myProject_v001.hip)
    pattern = r'^(.+)_(v\d+)\.hip$'
    match = re.match(pattern, file_name, re.IGNORECASE)
    
    if not match:
        hou.ui.displayMessage(
            f"Filename '{file_name}' does not match the required pattern: name_version.hip (e.g., myProject_v001.hip).\nPlease save the file with the correct pattern.",
            severity=hou.severityType.Warning
        )
    else:
        # Extract name and version
        base_name = match.group(1)
        version_str = match.group(2)
        
        # Increment the version number
        try:
            version_num = int(version_str[1:])  # Remove the 'v' and convert to int
            new_version = f"v{version_num + 1:03d}"  # Increment and format back to 3 digits
        except ValueError:
            hou.ui.displayMessage("Error parsing version number.", severity=hou.severityType.Error)
            raise
        
        # Construct the new file name and path
        new_file_name = f"{base_name}_{new_version}.hip"
        new_file_path = os.path.join(file_dir, new_file_name)
        
        # Save the current file with the new versioned name
        hou.hipFile.save(file_name=new_file_path)
        hou.ui.displayMessage(f"File versioned up successfully!\nSaved as: {new_file_name}", severity=hou.severityType.ImportantMessage)