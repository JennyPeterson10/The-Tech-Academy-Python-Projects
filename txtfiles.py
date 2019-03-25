
import os
import time

# this prints each file within the directory ending with ".txt" and it's corresponding mtime

def listFiles():
    path='C:\\Users\\Jenny\\Documents\\techacademygithub\\Python\\The-Tech-Academy-Python-Projects\\bridges'
    dir = os.listdir(path)
    doctime = time.ctime(os.path.getmtime(path))
    for file in dir:  
        if file.endswith(".txt"):
            print(os.path.join(path,file))
            print(doctime)


if __name__ == "__main__":
    listFiles()
