import os

### making directories for use in the lab ###

try:
    os.makedirs("tree/c/other_courses/cpp")
    os.makedirs("tree/c/other_courses/python")
    os.makedirs("tree/cpp/other_courses/c")
    os.makedirs("tree/cpp/other_courses/python")
    os.makedirs("tree/python/other_courses/c")
    os.makedirs("tree/python/other_courses/cpp")
except FileExistsError:
    pass

### finished making directories ###

# write a function or method called find that takes two arguments path and dir
# path should accept a relative or absolute path to a directory where the search should start
# dir should be the name of the directory to find
# should output absolute path if directory is found
# should be done recursively, checking all subdirectories in the path

def find(path, directory):
    os.chdir(path)
    for item in os.scandir(): # scandir() returns an iterator of DirEntry objects
        if item.is_dir(): # is_dir() is a DirEntry method, returning True if the object is a directory
            if item.name == directory: # name is a DirEntry attribute returning the filename/directoryname
                print(os.path.abspath(item.path)) # path is a DirEntry attribute returning the path, os.path.abspath() gets the absolute path
            os.chdir(item.path)
            find(os.getcwd(), directory) # iterates through subdirectories
            os.chdir(path) # resets to root of search

find(os.getcwd(), "python")




