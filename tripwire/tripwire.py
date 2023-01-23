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
    target = input("Which directory is being evaluated?  ")
    record = input("What is the name of the record file?  ")
    algorithm = input("which algorithm would you like to use for hashing? (sha256, sha1, md5) ")
    
        #everything below handles the hashing of files: 

    def hashFile():

    # this handles the case where the target is a file:   
        if  os.path.isfile(target): 
            with open(target, 'rb') as f:
                data = f.read()   
        # Create a new hash object using the specified algorithm
            if algorithm == "sha256":
                fileHash = hashlib.sha256(data)
            elif algorithm == "md5":
                fileHash = hashlib.md5(data)
            elif algorithm == "sha1":
                fileHash = hashlib.sha1(data)
            else:
                raise ValueError(f"Invalid algorithm: {algorithm}")
            print(fileHash.hexdigest())
    # this handles the case where the target is a directory:
        elif os.path.isdir(target):
            for root, dirs, files in os.walk(target):
                for file in files:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'rb') as f:
                        if algorithm == "sha256":
                            fileHash = hashlib.sha256()
                        elif algorithm == "md5":
                            fileHash = hashlib.md5()
                        elif algorithm == "sha1":
                            fileHash = hashlib.sha1()
                        else:
                            raise ValueError(f"Invalid algorithm: {algorithm}")
                        while True:
                            data = f.read(1024)
                            if not data:
                                break
                            fileHash.update(data)
                        print(f'{file}: {fileHash.hexdigest()}')  
    hashFile()
#this is for creating a record file

    

    
    
#read target content and return a hash result using a hash algorithm
# such as:    fileHash = hashlib.md5(data).hexdigest()import hashlib
                    
                    
tripwireDir()
