import shutil as __shutil
import os as __os
from time import strftime, localtime
import hashlib as __hashlib


def rm(file):
    isFile = __os.path.isfile(file)
    isDir = __os.path.isdir(file)
    if not isFile and not isDir:
        print("File or Directory not found!")
        return False
        quit()
    if isFile:
        __os.remove(file)
        if not __os.path.exists(file):
            print("File successfully deleted!")
            return True
    elif isDir:
        __shutil.rmtree(file)
        if not __os.path.exists(file):
            print("Directory successfully deleted!")
            return True


def rd(file):
    if not __os.path.exists(file):
        print("File not found!")
        return "" # maybe return a warning
        quit()
    else:
        if __os.path.isdir(file):
            print("Can't read folder")
            quit()
        with open(file) as f:
            #print(f.read())
            return f.read()

def w(file, content=""):
    if __os.path.isdir(file):
        print("Can't write folder")
        return False
    else:
        with open(file, "w") as f:
            f.write(content)
        with open(file) as f:
            check_if_written = f.read()
        if check_if_written == content:
            print("Successfully written on file")
            return True
        else:
            print("Failed!")
            return False
            
def c(name, fileOrDir=""):
    if fileOrDir == "file" or fileOrDir == "":
        with open(name, "w") as f:
            f.close()
    elif fileOrDir == "dir":
        __os.mkdir(name)

def inf(file):
    if not __os.path.exists:
        print("File or folder not found!")
    else:
        print("*****Informations*****")
        if __os.path.isfile(file):
            print("Size of file: " + str(__os.path.getsize(file)) + " bytes")
        else:
            ordnergroesse_bytes = sum(__os.path.getsize(__os.path.join(file, datei))
                          for datei in __os.listdir(file)
                          if __os.path.isfile(__os.path.join(file, datei)))
            print("Size of folder: " + str(ordnergroesse_bytes) + " bytes")
        print("Last modified time: " + str(strftime('%Y-%m-%d %H:%M:%S', localtime(__os.path.getmtime(file)))))
        print("Creation time: " + str(strftime('%Y-%m-%d %H:%M:%S', localtime(__os.path.getctime(file)))))


def md5(file):
    with open(file,"rb") as f:
        bytes = f.read() # read file as bytes
        readable_hash = __hashlib.md5(bytes).hexdigest()
        #print(readable_hash)
        return readable_hash


if __name__ == "__main__":
    print("Please import the module from another file to use it!")

