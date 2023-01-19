import hashlib
import os

def hashFile():
    target = input("What file/folder would you like to hash? ")
    algorithm = input("which algorithm would you like to use for hashing? (sha256, sha1, md5) ")
    # Open the file in read mode 
           
# check if the target input is a file or a directory   

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
        print(fileHash)
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
                    print(f'{file_path}: {fileHash.hexdigest()}')

hashFile()



