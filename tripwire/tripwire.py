"""
tripwire.py

Reading from a file, writing, appending, and recording in a seperate file. + hashing the contents of the given directory

Keiran McNeal Jan 9/2023

tripwireDir = directory: is the name of the directory that needs to be evaluated

tripwireRecord = record: is the name of the record file

create = c: create a record file containing the static information
"""



# define tripwireDir, test to see if the file can be opened and writted to

import os
from datetime import datetime
import hashlib

def tripwireDir(directory, record, c):
    # Open the file in read mode
    with open(directory, "r") as file:
        # Read the contents of the file
        original_contents = file.read()
    # Add new text to the file
    current_contents = (original_contents + input())
    # Open the file in append mode
    with open(directory, "a") as file:
        # append the new contents to the file
        file.write(current_contents)
        
    # Open the changes log file in read mode
    try:
        with open(record, "r") as file:
            # Read the contents of the changes log file
            changes_log_contents = file.read()
    except FileNotFoundError:
        # create log file 
        open(record, "w").close()
        changes_log_contents = ""
    # Compare the contents of the original file to the current contents
    with open(directory, "r") as file:
        current_contents = file.read()
         
    if current_contents != original_contents:
        # If the contents have changed, record the change in the log file
        changes_log_contents += f"{os.linesep}File: {directory} changed on {datetime.now()}{os.linesep}Old contents:{os.linesep}{original_contents}{os.linesep}New contents:{os.linesep}{current_contents}{os.linesep}"
        # open changes_log in append mode and write new changes
        with open(record, "a") as file:
            file.write(changes_log_contents)

#read file content and return a hash result using a hash algorithm
# such as:    fileHash = hashlib.md5(data).hexdigest()import hashlib

def hash_file(directory, algorithm):
    # Open the file in read mode
    with open(directory, "rb") as file:
        # Read the contents of the file
        file_contents = file.read()
        
    # Create a new hash object using the specified algorithm
    if algorithm == "sha256":
        fileHash = hashlib.sha256()
    elif algorithm == "md5":
        fileHash = hashlib.md5()
    elif algorithm == "sha1":
        fileHash = hashlib.sha1()
    else:
        raise ValueError(f"Invalid algorithm: {algorithm}")
    
    # Update the hash object with the file's contents
    fileHash.update(file_contents)
    
    # Return the hexadecimal representation of the hash object
    return fileHash.hexdigest()