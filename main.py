"""
Project Name: Sunil Sir ko note save garne program.
Project Author: Kaushal Rijal
Project Start Date: 5 January, 2023
Project End Date: 
"""

import os
import shutil

# Function to copy files from one directory to another
def copy_files(src_dir, dest_dir):
    # Check if the source directory exists
    if os.path.exists(src_dir):
        # Iterate over all the files in the source directory
        for file in os.listdir(src_dir):
            # Construct the full path of the file
            src_path = os.path.join(src_dir, file)
            # Construct the full path of the destination
            dest_path = os.path.join(dest_dir, file)
            # Check if the file is a regular file (not a directory)
            if os.path.isfile(src_path):
                # Copy the file from the source to the destination
                shutil.copy(src_path, dest_path)

# Function to be called when a pen drive is inserted
def on_pen_drive_inserted(pen_drive_path):
    # Construct the destination directory for the files
    dest_dir = os.path.join(os.getcwd(), 'pendrive_files')
    # Create the destination directory if it does not exist
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    # Copy the files from the pen drive to the destination directory
    copy_files(pen_drive_path, dest_dir)

# Run the code when this python script is executed
if __name__ == '__main__':
    print("Hello, welcome to Sunil Sirko Pen Drive ko note save garne program.")
    print("The program is developed by Kaushal Rijal.")
    input("Press enter to start the program, when the pen drive is inserted, and it takes the path of the pen drive as an argument. It constructs the destination directory for the files and creates it if it does not exist. It then calls the copy_files() function to copy the files from the pen drive to the destination directory.")
    # Find the path of the pen drive (assuming it is the first removable drive)
    pen_drive_path = os.path.join('/media/user/', os.listdir('/media/user/')[0])
    # Call the function to handle the pen drive insertion
    on_pen_drive_inserted(pen_drive_path)
