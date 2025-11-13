# Houdini Shelf Tools

This repository contains three Python scripts for Houdini shelf tools created for VFX Theory III assignment.

## Tools

### 1. Version Up Tool (`version_up.py`)
- Checks if the file name follows the `name_version.hip` pattern
- Versions up only if it matches `filename_version.extension` format
- Saves a new file with incremented version number

### 2. Publish Project Tool (`publish_project.py`)
- Copies the contents of the current project to a shared drive (Desktop)
- Offers a dialog box to include or omit cache files
- Creates a "Published_Houdini_Projects" folder on Desktop

### 3. Create Out Null Tool (`create_out_null.py`)
- Adds and connects a null node to selected nodes
- Names them with `_OUT_` prefix
- Positions them correctly using `.moveToGoodPosition()`
- Colors them black

## Installation
1. Copy the Python code for each tool
2. Create new shelf tools in Houdini
3. Paste the code into each tool's script section
4. Save and use the shelf buttons

## Requirements
- Houdini with Python support
- Compatible Python version