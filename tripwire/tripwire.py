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

def tripwireDir():
    directory = input("Which directory is being evaluated?  ")
    record = input("What is the name of the record file?  ")
    
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
    hashFile()
    
#everything below handles the hashing of files: 
    
#read target content and return a hash result using a hash algorithm
# such as:    fileHash = hashlib.md5(data).hexdigest()import hashlib
def hashFile():
    target = input("What file/folder would you like to hash? ")
    algorithm = input("which algorithm would you like to use for hashing? (sha256, sha1, md5) ")
    # Open the file in read mode 
           
# check if the target input is a file or a directory   
    def hashing():
    # Create a new hash object using the specified algorithm
        if algorithm == "sha256":
            fileHash = hashlib.sha256(data)
        elif algorithm == "md5":
            fileHash = hashlib.md5(data)
        elif algorithm == "sha1":
            fileHash = hashlib.sha1(data)
        else:
            raise ValueError(f"Invalid algorithm: {algorithm}")
        print(f'{file_path}: {fileHash.hexdigest()}')
        while True:
            data = f.read(1024)
            if not data:
                break
        fileHash.update(data)     
# this handles the case where the target is a file:   
    if  os.path.isfile(target): 
        with open(target, 'rb') as f:
            data = f.read() 
            hashing()  
# this handles the case where the target is a directory:
    elif os.path.isdir(target):
        for root, dirs, files in os.walk(target):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    hashing()
tripwireDir()
