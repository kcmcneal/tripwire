import hashlib

def hash_file(file, algorithm):
    # Open the file in read mode
    with open(file, 'rb') as f:
        data = f.read()    

        # Create a new hash object using the specified algorithm
        if algorithm == "sha256":
            fileHash = hashlib.sha256(data).hexdigest()
        elif algorithm == "md5":
            fileHash = hashlib.md5(data).hexdigest()
        elif algorithm == "sha1":
            fileHash = hashlib.sha1(data).hexdigest()
        else:
            raise ValueError(f"Invalid algorithm: {algorithm}")
    
    return fileHash.hexdigest()
