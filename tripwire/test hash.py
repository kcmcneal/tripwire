import os
import hashlib

def hash_files_in_directory():
    directory = input("name of file/folder to hash")
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                file_hash = hashlib.sha256()
                while True:
                    data = f.read(1024)
                    if not data:
                        break
                    file_hash.update(data)
                print(f'{file_path}: {file_hash.hexdigest()}')
