# teacher saves results of tests in file in the following format: firstname lastname score
# example in sample_result.txt

from io import StringIO
from os import strerror

class DataException(Exception):
    pass

class BadLine(DataException):
    def __init__(self, line):
        DataException.__init__(self)
        self.line = line
    pass

class FileEmpty(DataException):
    def __init__(self, file_path):
        DataException.__init__(self)
        self.file_path = file_path
    pass


try:

    src_path = input("> Enter path to results file: ")
    src = open(src_path, "r")


    split_lines = [line.split() for line in src.readlines()]
    src.close()
    
    if len(split_lines) == 0:
        raise FileEmpty(src_path)


    for line in split_lines:
        if len(line) != 3: # should be in form (first name, second name, score)
            raise BadLine(line)

    results = {line[0] + ' ' + line[1] : 0 for line in split_lines} # creates dictionary with names, default scores to 0
    print(results)

    try:
        for line in split_lines: # adds scores to dictionary
            results[line[0] + ' ' + line[1]] += float(line[2]) # if len(line) = 3 but type(line[2]) is not float, BadLine raised
    except Exception as exc:
        raise BadLine(line)

    for item in results.items(): # can't go wrong
        print(item[0], '\t', item[1])

except BadLine as exc:
    print("> Error: BadLine ", exc.line)
    exit(exc)

except IOError as exc:
    print("> Error: ", strerror(exc.errno))
    exit(exc.errno)

except FileEmpty as exc:
    print("> Error: the file is empty! ", exc.file_path)
    exit(exc)