import shutil
import os


def rm(file):
    isFile = os.path.isfile(file)
    isDir = os.path.isdir(file)
    if not isFile and not isDir:
        print("File or Directory not found!")
        quit()
    if isFile:
        os.remove(file)
        if not os.path.exists(file):
            print("File successfully deleted!")
    elif isDir:
        shutil.rmtree(file)
        if not os.path.exists(file):
            print("Directory successfully deleted!")


def rd(file):
    if not os.path.exists(file):
        print("File not found!")
        quit()
    else:
        if os.path.isdir(file):
            print("Can't read folder")
            quit()
        with open(file) as f:
            print(f.read())


def w(file, content=""):
    if os.path.isdir(file):
        print("Can't write folder")
    else:
        with open(file, "w") as f:
            f.write(content)
        with open(file) as f:
            check_if_written = f.read()
        if check_if_written == content:
            print("Successfully written on file")
        else:
            print("Failed!")
            
def c(name, fileOrDir=""):
    print("You need this function only if you want to create a file without content. But this can also be do if you give in the 'w' write function one parameter. So this function is a additional feature! Note: You can also create a folder if you give as second parameter dir")
    if fileOrDir == "file" or fileOrDir == "":
        with open(name, "w") as f:
            f.close()
    elif fileOrDir == "dir":
        os.mkdir(name)

if __name__ == "__main__":
    print("Please import the module from another file to use it!")

