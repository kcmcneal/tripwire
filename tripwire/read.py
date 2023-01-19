import hashlib

file = input("what is the name of the file you want to hash? ")
algorithm = input("Which algorithm do you want to use to hash the file? ")

# Open the file in read (binary) mode
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
    print(fileHash)
    
    
    
    '''     
        
    if  os.path.isfile(file): 
        with open(file, 'rb') as f:
            data = f.read()   
            hashObject()

    elif os.path.isdir(file):
        path = file
        dir_list = os.listdir(path)
        with open(path, 'rb') as f:
            data = dir_list
            hashObject()   
        print(dir_list)
        '''